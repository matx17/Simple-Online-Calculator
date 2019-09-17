import main_app 
import unittest

class MyTestCase(unittest.TestCase):

        def setUp(self):
            main_app.app.testing = True
            self.app = main_app.app.test_client()
