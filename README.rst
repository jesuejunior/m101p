MongoDB M101P

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



Tips and Tricks for MongDB
++++++++++++++++++++++++++

* Array query(Equality Matches on Arrays)
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
