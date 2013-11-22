daeta
=====

Datastorage and access from another perspective.

Just starting out. 

The aim is to be able to have a simple container that I can shove data into. The implementation persistence layer 
would be whatever, but the api would allow me to pretend like I am talking to a schemaless+nosql backend.

Features
---------

- No need to define a model, just work with python dicts (think JSON)
- Quick CRUD; very light on the "R" implementation
- Multiple backend implementations - some may expose additional features beyond common
- Simple and flexible API
- Auto schema migrations when data structure changes
- Pipe data from one backend to another

Backends
----------

Loosly based on how I expect to tackle the project

- In Memory
- SQLite
- MongoDb
- MySql
- ... more


Example Usage: In Memory
--------------------------

    >>> import daeta
    >>> print 2
    2



