import typer

from service import db, models, settings
from service.app import create_app

typer_app = typer.Typer(help='PdF-Parser service manager.')


def change_settings():
    settings.RUN_TYPE = 'local'
    db.engine = db.set_engine()


@typer_app.command(help='Enter a command "create-db" - to create db scheme')
def create_db(local_start: bool = typer.Option(False, '--local', '-l', help='start local DB')):
    if local_start:
        change_settings()
    print(settings.DB_URL[settings.RUN_TYPE])
    models.create_scheme()
    typer.echo('done')


@typer_app.command(help='Enter a command "run" - to start base service.')
def run(local_start: bool = typer.Option(False, '--local', '-l', help='start local service')):
    if local_start:
        change_settings()
    app = create_app()
    app.run(
        host=settings.APP_HOST,
        port=settings.PORT[settings.RUN_TYPE],
        debug=False
    )


if __name__ == '__main__':
    typer_app()
