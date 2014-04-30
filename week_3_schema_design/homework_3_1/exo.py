import pymongo
from operator import itemgetter

client = pymongo.MongoClient()
db = client.school
collection = db.students

for student in collection.find():
    scores = student['scores']

    lowest = None
    for score in scores:
        if score['type'] == 'homework' :
            if not lowest:
                lowest = score
            elif lowest['score'] > score['score']:
                lowest = score

    if lowest:
        scores.pop(map(itemgetter('score'), scores).index(lowest['score']))

    collection.update({'_id': student['_id']}, {'$set' : {'scores' : scores}})

