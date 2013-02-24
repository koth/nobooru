# -*- coding: utf-8 -*-
import HTMLParser
import lxml.html


class NoSuchForm(Exception):
    pass


class HTMLDocument(object):

    def __init__(self, data):
        self.root = lxml.html.fromstring(data)

    @classmethod
    def from_response(cls, response):
        return cls(response.data)

    def form(self, key):
        """
        Return a form Element with a given id or index.
        :param key: The id attribute of the form, or the index in the list of all forms on the page, or a Form instance.
        :type key: int or str or Form
        :return: an HTML form as an lxml Element
        :rtype: Element
        """

        # TODO: Handle a missing form by index better, same as below by xpath.
        if isinstance(key, int):
            return self.root.forms[key]

        if not isinstance(key, basestring):
            key = key.html_id

        xpath = "//form[@id='{form_name}']".format(form_name=key)
        forms = self.root.xpath(xpath)

        if forms:
            return forms[0]
        else:
            raise NoSuchForm(
                "No form found by the following xpath: {xpath}".format(xpath=xpath)
            )

    def xpath(self, xpath):
        return self.root.xpath(xpath)


def decode(html):
    return HTMLParser.HTMLParser().unescape(html)
