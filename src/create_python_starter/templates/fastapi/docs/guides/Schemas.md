# Schemas

Whenever you need to define a json schema for a route (or any other purpose)
define them in the `schemas` directory. You should always define schemas for
routes that receive any type of payload in query strings, json, or form data,
etc, so that they can be validated.

We (and `FastAPI`) use [pydantic](https://docs.pydantic.dev/latest/#pydantic-examples) to create our schemas.

Here's what that looks like in action:

```python
from pydantic import BaseModel, ConfigDict

class User(BaseModel):
    model_config = ConfigDict(extra="forbid") # forbid any other fields from the schema
    username: str
    password: str

@router.post("/login")
def login(user: User):
  # login user...
```

It's a really fun library, Read up on the their [docs](https://docs.pydantic.dev/latest/) for more!
