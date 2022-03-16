import logging

import typer

from service import models, settings
from service.app import create_app

typer_app = typer.Typer(help='PdF-Parser service manager.')


@typer_app.command('create_db')
def create_db():
    """
    Enter a command "create_db" - to create db scheme
    """
    models.create_scheme()
    typer.echo('done')


@typer_app.command('run')
def run():
    """
    Enter a command "run" - to start base service
    """
    logging.basicConfig(level=logging.DEBUG)
    app = create_app()
    app.run(host=settings.APP_HOST, port=settings.APP_PORT, debug=False)


if __name__ == '__main__':
    typer_app()
