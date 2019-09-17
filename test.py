import main_app 
import unittest

class MyTestCase(unittest.TestCase):

        def setUp(self):
            main_app.app.testing = True
            self.app = main_app.app.test_client()
                
        def test_list_sumint(self):
            response = self.app.get('/add?A=2&B=5')
            self.assertMultiLineEqual( '7' , response.data)
        def test_addfloat(self):
            rv =  self.app.get('/add?A=2.3&B=3.3')
            self.assertMultiLineEqual('5.6', rv.data)
        def test_addfrac(self):
            rv =  self.app.get('/add?A=2/3&B=3/3')
            self.assertMultiLineEqual('1.66666666667', rv.data)
        def test_addneg(self):
            rv =  self.app.get('/add?A=2.3&B=-3.3')
            self.assertMultiLineEqual('-1.0', rv.data)        
                
                
