import click
from pathlib import Path
from .helpers import (
    is_valid_folder,
    create_git_repo,
    install_dependencies,
    create_pyproject_toml_file,
)
import sys
from shutil import rmtree, copytree
from .types import TemplateType

PYTHON_TEMPLATE = "python"
FLASK_TEMPALTE = "flask"


@click.command()
@click.option("--name", prompt="What would you like to name your app?")
@click.option(
    "--template",
    type=click.Choice([PYTHON_TEMPLATE, FLASK_TEMPALTE]),
    prompt="What template would you like to create?",
)
def create_app(name: str, template: TemplateType) -> None:
    """Creates a project app with the `name` and `template` arguments given in the cli command"""
    project_path = Path(name).resolve()
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

        package_name = None
        if template == "python":
            package_name = app_name.replace("-", "_").replace(" ", "_")
            package_dir = Path(project_path / "src" / "[package]")
            package_dir.replace(project_path / "src" / app_name)

        create_pyproject_toml_file(
            project_path,
            app_name=app_name,
            template=template,
            package_dir_name=package_name,
        )

        click.echo("Initializing git repository...")
        create_git_repo(project_directory=project_path)

        click.echo("Installing depedencies...")
        install_dependencies(project_directory=project_path)
        
        click.echo()
        click.echo(f"Successfully created project at {project_path}!")
        click.echo()
    except Exception as e:
        click.echo(str(e))
        rmtree(project_path)


if __name__ == "__main__":
    create_app()
