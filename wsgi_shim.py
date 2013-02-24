# Target wsgi_shim:app with a wsgi server to run the app. wsgi needs a variable to use for requests.

from app import create_app, connect_all

app = create_app()
connect_all(app)
