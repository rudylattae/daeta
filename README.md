daeta
=====

Datastorage and access from another perspective.

Just starting out. 

The aim is to be able to have a simple container that I can shove data into. The implementation persistence layer 
would be whatever, but the api would allow me to pretend like I am talking to a schemaless+nosql backend.

Features
---------

- [ ] No need to define a model, just work with python dicts (think JSON)
- [ ] Quick CRUD; very light on the "R" implementation
- [ ] Multiple backend implementations - some may expose additional features beyond common
- [ ] Simple and flexible API
- [ ] Auto schema migrations when data structure changes
- [ ] Pipe data from one backend to another

Backends
----------

Loosly based on how I expect to tackle the project

- In Memory
- SQLite
- MongoDb
- MySql
- ... more


Example Usage: In Memory Stash
--------------------------------

To play around, you can just create a stash (aka collection or table) and just shove data into it

We need a story to drive the example so... let's say you want to keep track of things you have at home
    
    # you create a stash for your stuff
    >>> from daeta import Stash
    >>> stuff = Stash('home_inventory')

    # for starters, you have nothing
    >>> stuff.all()
    []

    # so you go out and buy a bunch of crap
    >>> stuff.add(dict(name='TV', cost=25.00))
    >>> stuff.add(dict(name='Leather Sofa', cost=200.00))
    >>> stuff.add(dict(name='Desk', cost=5.00))

    # now you are living la vida crapola!
    >>> len(stuff.all())
    3


