# pip install gdeltdoc
# pip install newspaper3k

# gdeltdoc api > url > crawling
# https://github.com/alex9smith/gdelt-doc-api
# keyword에 대한 news를 검색 > 

# newspaper3k > crawling하는 회사 패키지  
# !pip install lxml==4.8.0

from gdeltdoc import GdeltDoc, Filters
from newspaper import Article   # URL 통한 crawling

f = Filters(
    keyword = ["microsoft","openai","ai","AGI"],
    start_date = "2023-11-01",
    end_date = "2024-08-01",
    domain = ["nytimes.com","aitimes.com"], # ["bbc.co.uk", "nytimes.com"]
    country = ["KR","US"],          # ["UK", "US"],
    num_records=250
)

gd = GdeltDoc()
articles = gd.article_search(f)

# 데이터프레임 형태로 출력 (제한 250개)
# # 쿼리를 specific하게 만들거나, date를 하루만 주거나 
#print(articles.iloc[0,:])  # 헤더
print(articles)


url = articles.loc[1, "url"]
print(articles.loc[1, "title"])
print('---------------------------')
article = Article(url)
article.download()
article.parse()
print(article.text)
