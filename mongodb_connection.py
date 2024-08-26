# pip install pymongo

from pymongo import MongoClient

client = MongoClient(host="localhost", port=27017)

# 데이터베이스 이름 목록 반환
print(client.list_database_names())

# db 접근
db = client['test']
print(db)

# collection
collection = db['NewsText']
print(collection)


# collection에 item 
import datetime
#item = {'title':"패스트캠퍼스 주가 일시 상승",
#        "text":"패스트캠퍼스의 주가가 일시적으로 상승했다. 장중 최고치는...",
#        "date":datetime.datetime.now()}

#insert_id = collection.insert_one(item).inserted_id
#print(insert_id)

# collection item 조회
print(collection.find_one())