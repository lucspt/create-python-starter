import click
from pathlib import Path
from .helpers import is_valid_folder, copy, create_destination_directory
import sys
from shutil import rmtree
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
    project_path = Path(name).resolve()

    try:
        if project_path.exists() and not is_valid_folder(project_path):
            sys.exit(1)

        click.echo("Creating project directory...")
        copy(template="common", dest=str(project_path))

        dest_dir = create_destination_directory(
            template=template,
            project_path=project_path,
            package_name=None
            if template == "flask"
            else name.replace("-", "_").replace(" ", "_"),
        )

        copy(template=template, dest=str(dest_dir), dirs_exist_ok=True)

    except Exception as e:
        click.echo(str(e))
        rmtree(project_path)


if __name__ == "__main__":
    create_app()
