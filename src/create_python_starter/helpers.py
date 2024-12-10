from pathlib import Path
from subprocess import DEVNULL, STDOUT, run
from typing import Any, Optional

import click

from .types import TemplateType


def is_valid_folder(root: Path) -> bool:
    """Checks if a folder is valid for template creation, given the path to it.

    Args:
        root (Path): A `pathlib.Path` Posix Path pointing to the folder location

    """
    if root.exists():
        conflicts = list(root.iterdir())
        if conflicts:
            click.echo("The directory contains files that could conflict")
            click.echo()
            for c in conflicts:
                if Path(c).is_dir():
                    click.echo(f"   {c}/")
                else:
                    click.echo(f"   {c}")
            click.echo()
            click.echo(
                "Either try using a new directory name, or remove the files listed above."
            )
            return False
    return True


def pin_python_version(root: Path, version: str) -> None:
    f = root / ".python-version"
    f.touch()
    f.write_text(version)


def create_pyproject_toml_file(
    root: Path,
    app_name: str,
    template: TemplateType,
    package_dir_name: Optional[str] = None,
) -> tuple[list[str], list[str]]:
    """Creates a pyproject.toml file at in the top level of the `root` directory"""
    if template == "python" and package_dir_name is None:
        raise ValueError(
            "Must specify `package_dir_name` argument when app template is not `fastapi`"
        )
    file_location = root / "pyproject.toml"
    file_location.touch(exist_ok=True)
    if template == "fastapi":
        dependencies = [
            "dependencies = [\n",
            '   "fastapi==0.115.6",\n',
            '   "pydantic-settings>=2.3.4",\n',
            "]\n",
        ]
    else:
        dependencies = ["dependencies = []\n"]
    with open(file_location, "w") as f:
        # project meta
        f.writelines(
            [
                "[project]\n",
                f'name = "{app_name}"\n',
                'version = "0.1.0"\n',
                'description = "Add your description here"\n',
                "authors = []\n",
                *dependencies,
                'readme = "README.md"\n',
                'requires-python = ">= 3.10"\n',
                "\n",
            ]
        )

        dev_dependencies = [
            "dev-dependencies = [\n",
            '   "mypy>=1.10.1",\n',
            '   "pytest-cov>=5.0.0",\n',
            '   "ruff>=0.5.0",\n',
            '   "mkdocs>=1.6.0",\n',
            '   "mkdocstrings[python]>=0.25.1",\n',
            '   "mkdocs-material>=9.5.29",\n',
            '   "commitlint>=1.1.0",\n',
        ]

        if template == "fastapi":
            dev_dependencies.append('   "httpx>=0.27.0",\n')

        dev_dependencies.append("]\n\n")

        # rye
        f.writelines(
            [
                "[tool.rye]\n",
                "managed = true\n",
                *dev_dependencies,
            ]
        )

        # rye scripts
        lines = ["[tool.rye.scripts]\n"]
        cov_folder = "src/"
        if template == "fastapi":
            lines.extend(
                [
                    """prod = { cmd = "fastapi run", env = { FAST_API_ENV = "production" }}\n""",
                    """dev = { cmd = "fastapi dev app/main.py", env = { FAST_API_ENV = "development" } }\n""",
                ]
            )

            cov_folder = "app/"
        lines.extend(
            [
                f'test = {{ cmd = "pytest --cov={cov_folder} tests/" }}\n',
                f'test-ui = {{ cmd = "pytest --cov={cov_folder} --cov-report=html tests/" }}\n',
                "\n",
                *[
                    "fix = { chain = [\n",
                    '   "lint:ruff",\n',
                    '   "ruff format",\n',
                    "]}\n",
                ],
                "\n",
                '"lint:ruff" = { cmd = "ruff check --fix" }\n',
                *[
                    "lint = { chain = [\n",
                    '   "lint:ruff",\n',
                    '   "mypy ."\n',
                    "]}\n",
                ],
                "\n",
                '"docs:serve" = { cmd = "mkdocs serve -f mkdocs.yml" }\n',
                "\n",
            ]
        )
        f.writelines(lines)

        # build-system
        f.writelines(
            [
                "[build-system]\n",
                'requires = ["hatchling"]\n',
                'build-backend = "hatchling.build"\n',
                "\n",
            ]
        )

        # ruff format config
        f.writelines(["[tool.ruff.format]\n", "docstring-code-format = true\n", "\n"])

        # ruff lint config
        f.writelines(
            [
                "[tool.ruff.lint]\n",
                "select = [\n",
                "   # isort\n",
                '   "I",\n',
                "   # remove unused imports\n",
                '   "F401",\n',
                "]\n",
                "\n",
            ]
        )

        # ruff import sorting
        f.writelines(
            [
                "[tool.ruff.lint.isort]\n",
                "length-sort = true\n",
                "length-sort-straight = true\n",
                "combine-as-imports = true\n",
                f"""known-first-party = ["{app_name}", "tests"]\n""",
                "\n",
            ]
        )

        # pytest options
        f.writelines(["[tool.pytest.ini_options]\n", 'testpaths = ["tests"]\n', "\n"])

        # coverage options
        f.writelines(["[tool.coverage.report]\n", "fail_under = 90\n", "\n"])

        # hatch metadata
        f.writelines(
            [
                "[tool.hatch.metadata]\n",
                "allow-direct-references = true\n",
                "\n",
            ]
        )

        # wheel build target
        lines = [
            "[tool.hatch.build.targets.wheel]\n",
        ]
        if template == "fastapi":
            lines.append('packages = ["app"]\n')
        else:
            lines.append(f'packages = ["src/{package_dir_name}"]\n')
        f.writelines(lines)
    return dev_dependencies[1:-1], dependencies[1:-1]


def configure_mkdocs_yaml(root: Path, site_name: str, template: TemplateType) -> None:
    loc = root / "mkdocs.yml"

    loc.touch(exist_ok=True)

    with open(loc, "r+") as f:
        lines = f.readlines()
        f.seek(0)
        lines[0] = f"site_name: {site_name} Documentation"
        f.writelines(lines)


def exec_command(
    cmd_args: list[str] | str,
    cwd: Optional[Path | str] = None,
    check: bool = True,
    **kwargs: Any,
) -> None:
    run(cmd_args, cwd=cwd, stderr=STDOUT, stdout=DEVNULL, check=check, **kwargs)


def install_dependencies(
    project_directory: Path, dev_dependencies: list[str], dependencies: list[str]
) -> None:
    """Install dependencies with rye"""
    try:
        click.echo("Installing depedencies...\n")
        click.echo(f"Dev dependencies:\n{''.join(dev_dependencies)}")
        if dependencies:
            click.echo(f"Dependencies:\n{''.join(dependencies)}")
        exec_command(["rye", "sync", "--all-features"], cwd=project_directory)
    except Exception as e:
        raise Exception(
            f"""
            
            Could not install dependencies with `rye`, are you sure you have it installed?
            
            Error: {e}
            
            See more at: https://rye.astral.sh/
            
            """
        )


def create_git_repo(project_directory: Path) -> None:
    """Create a git repo and setup git config"""
    try:
        exec_command(["git", "init", "."], cwd=project_directory)
        exec_command(["git", "add", "-A"], cwd=project_directory)
        exec_command(["sh", "./scripts/prepare"], cwd=project_directory)
        exec_command(["git", "commit", "-am", "Initial commit", "--no-verify"], cwd=project_directory)
    except Exception as e:
        raise Exception(
            f"""
            
            Failed to initialize a git repository. 
            
            Error: {e}
            
            """
        )
