
import unittest

from app.models import Articles


class test_articles(unittest.TestCase):
    '''
    This test class is for testing the behaviour of the Article class
    '''
    def setup(self):
        '''
        Set up method that runs before every test
        '''
        self.new_article = Articles("2022-05-01T13:52:19.9887887Z", 'https://ichef.bbci.co.uk/news/1024/branded_news/131D9/production/_124379287_p0c49wfd.jpg', "Biden mocks Trump at White House press dinner", "US President Joe Biden has resumed the tradition of speaking at the annual White House Correspondents' Dinner after a six-year presidential hiatus.\r\nHe is the first leader to speak at the event, wher… [+89 chars]", "BBC News", "http://www.bbc.co.uk/news/world-us-canada-61290695", "Joe Biden jokes about former president Donald Trump at the prestigious event hosted by Trevor Noah.")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Articles))

