#!/usr/bin/env python
# -*- coding: utf-8 -*-
from argparse import ArgumentParser
import config
import os

parser = ArgumentParser()
parser.add_argument(
    "-d", "--debug",
    help="Run with flask debugging enabled. Do not do this in production.",
    action="store_true",
)

parser.add_argument("-p", "--port", help="Port to serve the app on.", type=int, default=5000)


def run(debug=False, **kw):
    import app

    app_instance = app.create_app()
    app.connect_all(app_instance)

    # Create the sqlite database if it doesn't exist.
    if debug and not os.path.exists(config.SQLITE_DB_FILE):
        import database
        database.init_db()

    app_instance.run(debug=debug, **kw)


def main():
    args = parser.parse_args()

    if args.debug:
        print "Running in debug mode."

    run(debug=args.debug, host='0.0.0.0', port=args.port)


if __name__ == '__main__':
    main()
