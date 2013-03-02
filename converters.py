from werkzeug.routing import BaseConverter


class RegexConverter(BaseConverter):
    """
    Allows the use of regexps directly in flask routes

    Taken from http://stackoverflow.com/questions/5870188/does-flask-support-regular-expressions-in-its-url-routing

    Example:

    @app.route('/<regex("[abcABC0-9]{4,6}"):uid>-<slug>/')
    def example(uid, slug):
        return "uid: %s, slug: %s" % (uid, slug)

    """
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]

    @classmethod
    def register(cls, app):
        """
        Register this converter with a Flask app.
        
        :param app: Flask application to register with.
        """
        app.url_map.converters["regex"] = cls