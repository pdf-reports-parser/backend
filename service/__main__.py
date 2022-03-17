import typer

from service import models
from service.app import create_app
from service.config import AppConfig

typer_app = typer.Typer(help='PdF-Parser service manager.')
app_config = AppConfig()


@typer_app.command(help='Create db scheme')
def create_db():
    models.create_schema()


@typer_app.command(help='Start base service.')
def run():
    app = create_app()
    app.run(host=app_config.APP_HOST, port=app_config.APP_PORT, debug=False)


if __name__ == '__main__':
    typer_app()
