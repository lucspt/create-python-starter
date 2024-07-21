# Create Python Starter

Hey, welcome to our python project scaffolder, `create-python-starter`!

It is a cli tool that let's creates a templated python project with many batteries included,
like:

- [rye](https://rye.astral.sh/)
- [ruff](https://docs.astral.sh/ruff/)
- [mypy](https://mypy.readthedocs.io/en/stable/index.html)
- git pre-commit hooks (testing, linting, formatting, etc)

You can create a new project interactively by running:

```text
create_python_starter
```

You will be asked for the name of your project:

```text
What would you like to name your app?:
```

And then what template you would like to create:

```text
What template would you like to create? (python, fastapi):
```

These prompts ask you to type in your answers.

To create a new `FastAPI` service, choose `fastapi`. To create a new Python library, choose `python`.

You can also use command line arguments for a non-interactive experience:

```text
create_python_starter --name [project-name] --template [project-template]
```

Here are all the available options:

```text
Options:
  --name TEXT
  --template [python|fastapi]
```

# Folder location inference

**Note**: the location of the project will be inferred by the `name` argument. So if your choose a project name of
`my-project`, the scaffolder will create a new directory named `my-project` in the same folder you called the command in.
If, for example you specified a name of `.`, the tool will infer that the name of the project is the name of the current directory.
You can not make a new project in a non-empty directory.
