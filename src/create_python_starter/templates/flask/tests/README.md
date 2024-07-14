# Testing 

We use [pytest](https://docs.pytest.org/en/8.2.x/).

Flask also provides utilites for testing, You can read up on [the guide](
  https://flask.palletsprojects.com/en/2.3.x/testing/
) for more.


[Test commands](#test-commands)
[What to test](#what-to-test)
[Testing routes](#testing-app-routes)
[Testing structure](#testing-structure)

## Test commands 

```bash

# run test with coverage report in terminal
rye run test 

# run test with html report
rye run test-ui
```

If you run the `test-ui` command, it will create an `htmlcov` directory.
Find the `index.html` file inside the directory and open it with a 
[live server](
  https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer
) to view it in your browser.

## What to test

Generally, anything we create should be tested. We strive to keep above 95% coverage 
and it is mandatory to keep at least 90%.

## Testing app routes 

If you look at our [configuration file](./conftest.py) there are two fixtures defined that look 
something like:

```python
@fixture()
def api(app: Flask) -> FlaskClient:
    return app.test_client()
```

Whenever you need to access the flask application and test a route, 
request this fixture and mock a route with one of it's 
`get`, `post`, `put`, etc methods. 

Here's an example of that:

```python
from flask.testing import FlaskClient

def test_root_get(api: FlaskClient) -> None:
    res = api.get("/") # you can access the json data with `res.get_json()`
    assert res.status_code == 200
```

## Testing structure

Feel free to test with classes or functions. When there are a lot of similar tests,
and it is possible, try to group them into their own [class](
  https://docs.pytest.org/en/7.1.x/getting-started.html#group-multiple-tests-in-a-class
). 

