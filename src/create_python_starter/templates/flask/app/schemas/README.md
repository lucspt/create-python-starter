# Schemas

Here is the folder where we define our schemas! Whenever you need to define
a json schema for a route (or any other purpose) define them here. You should 
always define schemas for routes that receive any type of payload in the form
of query strings, json, or form data, so that they can be validated.

We use [pydantic](https://docs.pydantic.dev/latest/#pydantic-examples) to create our schemas.

Here's what that looks like in action:

```python
from pydantic import BaseModel, ConfigDict

class User(BaseModel):
    model_config = ConfigDict(extra="forbid") # forbid any other fields from the schema
    username: str
    password: str


# login route in routes/user.py
from http_utils import validate_request

@bp.post("/login")
 # Validate the body with the User schema. Can also validate form and query
@validate_request(body=User)
def login(body: User): # the decorator will pass the result if `body` is requested
  # login user...
```

Read up on the their [docs](https://docs.pydantic.dev/latest/) for more!
