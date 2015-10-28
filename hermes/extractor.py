from __future__ import unicode_literals
import json, httplib2
from django.utils.http import urlencode
from django.utils.html import strip_tags
from django.conf import settings
import myql

class TermExtractor(object):

    api_readability_parser_url = "http://www.readability.com/api/content/v1/parser"
    api_yql_url = "http://query.yahooapis.com/v1/public/yql"

    query = 'select * from search.termextract where context=@text'

    def __init__(self, url):
        self.url = url
        self.httplib = httplib2.Http()

        resp, content = self.httplib.request( "%s?%s" % (self.api_readability_parser_url, urlencode({ 'token' : settings.READABILITY_KEY, 'url': url })))
        self.metadatas = json.loads(content)

    def get_terms(self):
        #html_parser = HTMLParser.HTMLParser()
        #content = strip_tags(html_parser.unescape(self.metadatas['content'])).replace("\n", "")
        content = "bla bla"
        y = myql.MYQL()
        result = y.rawQuery(self.query, {'text': content.encode('utf-8')})
        print(result)
        return result.results['Result']

    def get_excerpt(self):
        return self.metadatas['excerpt']

    def get_title(self):
        return self.metadatas['title']