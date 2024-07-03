def hello_world() -> dict[str, str]:
    return {"hello": "world"}


if __name__ == "__main__":
    print(**hello_world())
