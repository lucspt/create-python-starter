from pathlib import Path
import click
from .types import TemplateType
from typing import Optional, Any
from subprocess import run, STDOUT, DEVNULL


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


def create_pyproject_toml_file(
    root: Path,
    app_name: str,
    template: TemplateType,
    package_dir_name: Optional[str] = None,
) -> None:
    """Creates a pyproject.toml file at in the top level of the `root` directory"""
    if template == "python" and package_dir_name is None:
        raise ValueError(
            "Must specify `package_dir_name` argument when app template is not `flask`"
        )
    file_location = root / "pyproject.toml"
    file_location.touch(exist_ok=True)
    if template == "flask":
        dependencies = [
            "dependencies = [\n",
            '   "flask>=3.0.3",\n',
            '   "flask-talisman>=1.1.0",\n' "]\n",
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
                'requires-python = ">= 3.12"\n',
                "\n",
            ]
        )

        # rye
        f.writelines(
            [
                "[tool.rye]\n",
                "managed = true\n",
                # keep like this for indentation reasons
                "dev-dependencies = [\n",
                '   "mypy>=1.10.1",\n',
                '   "pytest-cov>=5.0.0",\n',
                '   "ruff>=0.5.0",\n' "]\n",
                "\n",
            ]
        )

        # rye scripts
        lines = ["[tool.rye.scripts]\n"]
        cov_folder = "src/"
        if template == "flask":
            lines.append('dev = { cmd = "flask run --port 8000 --debug" }\n')
            cov_folder = "app/"
        lines.extend(
            [
                f'test = {{ cmd = "pytest --cov={cov_folder} tests/" }}\n',
                f'test-ui = {{ cmd = "pytest --cov={cov_folder} --cov-report=html tests/" }}\n',
                "fix = { chain = [\n",
                '   "ruff check --fix --quiet",\n',
                '   "format:ruff",\n',
                "]}\n",
                '"format:ruff" = "ruff format"\n',
                "\n",
                '"lint" = "ruff check --fix"\n',
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

        # ruff options
        f.writelines(["[tool.ruff.format]\n", "docstring-code-format = true\n", "\n"])

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
        if template == "flask":
            lines.append('packages = ["app"]\n')
        else:
            lines.append(f'packages = ["src/{package_dir_name}"]\n')
        f.writelines(lines)


def exec_command(
    cmd_args: list[str] | str,
    cwd: Optional[Path | str] = None,
    check: bool = True,
    **kwargs: Any,
) -> None:
    run(cmd_args, cwd=cwd, check=check, stderr=STDOUT, stdout=DEVNULL, **kwargs)


def install_dependencies(project_directory: Path) -> None:
    """Install dependencies with rye"""
    try:
        exec_command(["rye", "sync"], cwd=project_directory)
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
        exec_command(["git", "commit", "-am", "Initial commit"], cwd=project_directory)
        exec_command("source ./scripts/prepare", shell=True, cwd=project_directory)
    except Exception as e:
        raise Exception(
            f"""
            
            Failed to initialize a git repository. 
            
            Error: {e}
            
            """
        )
