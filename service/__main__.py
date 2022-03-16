import typer

from service import models, settings
from service.app import create_app

typer_app = typer.Typer(help='PdF-Parser service manager.')


@typer_app.command(help='Enter a command "create-db" - to create db scheme')
def create_db(local_start: bool = typer.Option(False, '--local', '-l', help='start local DB')):
    if local_start:
        typer.echo('set new net param')
    models.create_scheme()


@typer_app.command(help='Enter a command "run" - to start base service.')
def run(local_start: bool = typer.Option(False, '--local', '-l', help='start local service')):
    if local_start:
        typer.echo('set new net param')
    app = create_app()
    app.run(
        host=settings.APP_HOST,
        port=settings.PORT,
        debug=False
    )


if __name__ == '__main__':
    typer_app()
