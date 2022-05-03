import unittest

from app.models import Sources


class test_sources(unittest.TestCase):
    '''
    This test class is for testing the behaviour of the Sources class
    '''
    def setUp(self):
        '''
        Set up method that runs before every test
        '''
        self.new_source = Sources("bbc-news", "BBC News")
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Sources))