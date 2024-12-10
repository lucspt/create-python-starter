import sys
from pathlib import Path
from shutil import copytree, rmtree

import click

from .helpers import (
    configure_mkdocs_yaml,
    create_git_repo,
    create_pyproject_toml_file,
    install_dependencies,
    is_valid_folder,
    pin_python_version,
)
from .types import TemplateType

PYTHON_TEMPLATE = "python"
FAST_API_TEMPLATE = "fastapi"


@click.command()
@click.argument("project", required=False)
@click.option(
    "--name",
    help="The name of the project",
)
@click.option(
    "--template",
    type=click.Choice([PYTHON_TEMPLATE, FAST_API_TEMPLATE]),
    help="The project's template",
)
def create_app(project: str, name: str, template: TemplateType) -> None:
    """Create a python project with the specified name and template"""

    project_name = project if project else name

    if not project_name:
        project_name = click.prompt("What would you like to name your app?")

    if not template:
        template = click.prompt(
            "What template would you like to create? (python, fastapi)"
        )

    project_path = Path(project_name).resolve()
    app_name = project_path.name

    try:
        if not is_valid_folder(project_path):
            sys.exit(1)

        click.echo()

        click.echo("Creating project directory...")
        templates_dir = Path(__file__).resolve().parent / "templates"

        copytree(templates_dir / "common", str(project_path), dirs_exist_ok=True)

        template_dir = templates_dir / template
        copytree(template_dir, project_path, dirs_exist_ok=True)

        package_name = app_name.replace("-", "_").replace(" ", "_")

        if template == "python":
            package_dir = Path(project_path / "src" / "[package]")
            package_dir = package_dir.replace(project_path / "src" / package_name)
            Path(package_dir / "py.typed").touch()

        pin_python_version(project_path, "3.12.3")

        devdeps, deps = create_pyproject_toml_file(
            project_path,
            app_name=package_name,
            template=template,
            package_dir_name=package_name,
        )

        configure_mkdocs_yaml(
            project_path,
            site_name=package_name.replace("_", " ").title(),
            template=template,
        )

        click.echo("Initializing git repository...")
        create_git_repo(project_directory=project_path)

        install_dependencies(
            project_directory=project_path, dev_dependencies=devdeps, dependencies=deps
        )

        click.echo()
        click.echo(f"Successfully created project at {project_path}!")
        click.echo()
    except Exception as e:
        click.echo(str(e))
        rmtree(project_path)


if __name__ == "__main__":
    create_app()
