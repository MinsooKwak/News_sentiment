# pip install openai==0.28
import config
import openai
from gdeltdoc import GdeltDoc, Filters
from newspaper import Article

# secret key
open_ai_key = config.OPEN_AI_API_KEY

# API > openai 인증
openai.api_key = open_ai_key

model = "gpt-3.5-turbo-0125"
gd = GdeltDoc()

# 함수화
def chatgpt_generate(query):
    
    # 포맷
    messages = [{
        "role":"system",
        "content":"You are a helpful assistant."
    },
    {
        "role":"user",
        "content": query
    }]

    # 응답
    response = openai.ChatCompletion.create(model=model, messages=messages)
    answer = response['choices'][0]['message']['content']
    return answer

def get_url(keyword):
    "keyword 입력받은 뉴스 데이터프레임"
    f = Filters(
        start_date="2024-07-01",
        end_date="2024-08-01",
        num_records=10,
        keyword=keyword,
        domain="nytimes.com",
        country="US"
    )

    articles = gd.article_search(f)
    return articles

def url_crawling(df):
    urls = df["url"]
    titles = df['title']
    texts = []
    for url in urls:
        article = Article(url)
        article.download()
        article.parse()
        texts.append(article.text)
    return texts


#text = "패스트캠퍼스 주가는 상승했는데 반해, 세컨드캠퍼스의 매출은 하락세다."
prompt ="""
아래 뉴스에서 기업명을 모두 추출하고, 기업에 해당하는 감성을 분석하시오.
각 감성의 스코어링을 하시오. 각 스코어의 합은 1이 되어야 합니다. 소수점 첫번째까지만 생성하세요.
출력 포맷은 리스트이며, 세부 내용은 다음과 같습니다.
반드시 출력포맷만을 생성하시오. 그 이외의 단어나 설명은 생성하지 마시오.

[{"organization":<기업명>, "positive":0~1, "negative":0~1, "neutral":0~1}, ...]

뉴스: 
"""
# 리스트 형태로 받아서 > 파이썬 객체로 만들 수 있음 

#print(prompt+text)

#answer = chatgpt_generate(prompt+text)
#print(answer)

result = []
orgs = ['microsoft','apple','openai']
for org in orgs:
    df = get_url(org)
    #print(len(df)) # 검색 결과 하나도 없으면 0 
    texts = url_crawling(df)
    #print(len(texts))
    for text in texts:
        answer = chatgpt_generate(prompt+text)
        result.append(eval(answer))
    print(result)
        
#print(prompt+texts[0])
#print('-----------')
#print(answer)
#print('')
#print(eval(answer))