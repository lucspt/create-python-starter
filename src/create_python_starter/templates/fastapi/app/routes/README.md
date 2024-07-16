# Routes 

This folder contains all of the app's routes. Here are some guidelines to follow when 
implementing a new route. 

## Group routes logically
Make sure that all routes are grouped logically, for example, all `/user` routes
are stored in a `users.py` file. If the appropriate file has yet to be created for 
an endpoint, create a new one. 

If a single file becomes too large, create a folder and separate 
the endpoints appropriately, e.g. by http method like `post.py`, `get.py`,
etc. This folder should contain a `__init__.py` which exports the router
that will be used to register all routes, so they can all be registered at
once. 

## Separate endpoints of different methods

Whenever possible, separate the endpoints you define by their methods. 

E.g. this 

```python
@router.route("/example", methods=["GET", "POST"])
def example(request: Request):
  if request.method == "POST":
      # ... 
  elif request.method == "GET":
      # ...

```

can be refactored like so 

```python
@router.route("/example", methods=["GET"]) # specify method, even if it is just a GET
def get_example():
    # ...

@router.post("/example") # shorthand syntax, if you prefer
def post_example():
    # ...
```
This makes it easier to follow along with, and adds a nice separation of concerns.
