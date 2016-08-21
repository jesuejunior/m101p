# encoding: utf-8
import time
import pymongo
from pymongo import MongoClient


start = time.time()
conn = MongoClient('localhost', 27017)
db = conn.school

for item in db.students.find():
    print(item)
    scores = item['scores']
    if len(scores) > 3:
        minimum = min([x['score']  for x in scores if x['type'] == 'homework'])
    # import ipdb;ipdb.set_trace()
        result = db.students.update_one({'_id': item['_id']}, {'$pull': {'scores': {'score': minimum,
            'type': 'homework'}}})
        print(result.__dict__)

end = time.time()

print('Final elapsed: ', end - start)  
