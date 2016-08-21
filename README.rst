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


Homework 2.3

In line 58 from userDAO.py 

.. code-block:: python

    user = self.users.find_one({'_id': username})

In the line 89 from userDAO.py

.. code-block:: python

    self.users.insert_one(user)

Validating and getting the result

.. code-block:: shell
    
    $ python validate.py
    master [+       0] [a850236] modified untracked
    Welcome to the HW 2.3 validation tester
    Trying to create a test user  TImVMLV
    Found the test user  TImVMLV  in the users collection
    User creation successful.
    Trying to login for test user  TImVMLV
    User login successful.
    Validation Code is  jkfds5834j98fnm39njf0920f02


Homework 2.4 

.. code-block:: javascript

    > db.movieDetails.find({'year': 2013, 'awards.wins': 0, 'rated': 'PG-13'}).pretty()
    {
        "_id" : ObjectId("5692a3e124de1e0ce2dfda22"),
        "title" : "A Decade of Decadence, Pt. 2: Legacy of Dreams",
        "year" : 2013,
        "rated" : "PG-13",
        "released" : ISODate("2013-09-13T04:00:00Z"),
        "runtime" : 65,
        "countries" : [
            "USA"
        ],
        "genres" : [
            "Documentary"
        ],
        "director" : "Drew Glick",
        "writers" : [
            "Drew Glick"
        ],
        "actors" : [
            "Gordon Auld",
            "Howie Boulware Jr.",
            "Tod Boulware",
            "Chen Drachman"
        ],
        "plot" : "A behind the scenes look at the making of A Tiger in the Dark: The Decadence Saga.",
        "poster" : null,
        "imdb" : {
            "id" : "tt2199902",
            "rating" : 8,
            "votes" : 50
        },
        "awards" : {
            "wins" : 0,
            "nominations" : 0,
            "text" : ""
        },
        "type" : "movie"
    }

Homework 3.1

.. code-block:: shell

    $ cd chapter3/hw3.1

Import data to mongo

.. code-block:: shell

    $ mongoimport --drop -d school -c students students.json

Execute apython program hw3.1

.. code-block:: shell

    $ python hw3.1.py

To see the answer in mongo shell

.. code-block:: javascript

    > db.students.aggregate( [
    ...   { '$unwind': '$scores' },
    ...   {
    ...     '$group':
    ...     {
    ...       '_id': '$_id',
    ...       'average': { $avg: '$scores.score' }
    ...     }
    ...   },
    ...   { '$sort': { 'average' : -1 } },
    ...   { '$limit': 1 } ] )
    { "_id" : 13, "average" : 91.98315917172745 }



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
