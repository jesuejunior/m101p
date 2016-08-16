# encoding: utf-8

import time
import pymongo
from pymongo import MongoClient

conn = MongoClient('localhost', 27017)
db = conn.students
start = time.time()

# One option
# hw = db.grades.find({'type': 'homework'})
# for item in hw:
#     for rem in db.grades.find({'type': 'homework'}):
#         if item['student_id']  ==  rem['student_id']:
#             if rem['score'] < item['score']:
#                 r = db.grades.remove(rem)
#                 print(r)
#

# two option
hw = db.grades.find({"type": "homework"}).sort("student_id").sort("score")
for item in hw:
    result = db.grades.delete_one(item)
    print(result.deleted_count)

end = time.time()
print('Final elapsed: ', end - start)
