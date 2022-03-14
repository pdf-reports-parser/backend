import logging

from service import settings
from service.app import create_app


def main():
    logging.basicConfig(level=logging.DEBUG)
    app = create_app()
    app.run(host=settings.APP_HOST, port=settings.APP_PORT, debug=False)


if __name__ == '__main__':
    main()
