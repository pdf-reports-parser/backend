import typer

from service import models, settings
from service.app import create_app

typer_app = typer.Typer(help='PdF-Parser service manager.')


@typer_app.command(help='Create db scheme')
def create_db():
    models.create_schema()


@typer_app.command(help='Start base service.')
def run():
    app = create_app()
    app.run(host=settings.APP_HOST, port=settings.APP_PORT, debug=False)


if __name__ == '__main__':
    typer_app()
