# Create Python Starter

Hey, welcome to our python project scaffolder, `create-python-starter`!

It is a cli tool that creates a templated python project with many batteries included,
like:

- [rye](https://rye.astral.sh/)
- [ruff](https://docs.astral.sh/ruff/)
- [mypy](https://mypy.readthedocs.io/en/stable/index.html)
- git pre-commit hook (testing, linting, formatting, etc)

## Installation

First, you will have to [install pipx](https://pipx.pypa.io/stable/installation/).

Once you have it installed you can run:

```text
pipx install <INSERT_LINK_HERE>
```

## Usage

After installing, You can create a new project interactively by running:

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

To answer, just type and click enter.

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

## Choosing a project template.

When creating a project, you will be prompted for the template you want to create.

The two options are `fastapi` and `python`.

To create a new `FastAPI` service, choose `fastapi`. To create a new Python library, choose `python`.

## Folder location inference

**Note**: the location of the project will be inferred through the `name` argument. So if you choose a project name of
`my-project`, the project will be created in a new directory named `my-project` in the same folder you ran the command in.
If, for example, you specified a name of `.`, the tool will infer that the name of the project is the name of the current directory.
You can not make a new project in a non-empty directory.
