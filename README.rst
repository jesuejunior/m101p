=============
MongoDB M101P
=============
Homework 1.1

.. code-block:: javascript

    > db.hw1.find().pretty()
    {
        "_id" : ObjectId("50773061bf44c220307d8514"),
            "answer" : 42,
                "question" : "The Ultimate Question of Life, The Universe and Everything"
    }

Homework 1.2

.. code-block:: shell

    > python hw1-2.py
    The answer to Homework One, Problem 2 is 1815

Homework 1.3

.. code-block:: shell

    > curl http://localhost:8080/hw1/50
    53

Homework 2.1

Import data

mongoimport --drop -d students -c grades grades.json

> db.grades.find({'score': {$gte:65}}).sort({score: 1}).limit(1)
{ "_id" : ObjectId("50906d7fa3c412bb040eb5cf"), "student_id" : 22, "type" : "exam", "score" :
65.02518811936324 }

Homework 2.2

execute 

python hw2_2.py

then

> db.grades.aggregate( { '$group' : { '_id' : '$student_id', 'average' : { $avg : '$score' } } }, {
'$sort' : { 'average' : -1 } }, { '$limit' : 1 } )
{ "_id" : 54, "average" : 96.19488173037341 }

Tips and Tricks for MongDB
--------------------------

Array query(Equality Matches on Arrays)
+++++++++++++++++++++++++++++++++++++++

- On the entire array

    > db.collection.find({"actor": ["wsx", "edc"]})

- Based on any element

    > db.collection.find({"actor": "wsx"})

- Based on a specific element

    > db.collection.find({ "actor.0": "wsx" })

- More complex matches using operators

* Cursors just returns 101 documents or until 1MB in the total of documents
* Projection is the better way to limit fields to query return. i.e:

... code-block:: javascript

    > db.collection.find({title: "abc"},{ title: 1, _id: 0})

It'll return just a title field excluding _id.

LINKS
+++++

* http://json.org/
* http://bsonspec.org/
* http://api.mongodb.com/python/current/
* https://docs.mongodb.com/manual/reference/operator/query/
