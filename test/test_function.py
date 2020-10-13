import main
import unittest
import calculator

class mainTestCase(unittest.TestCase):
    def first_input(self):
        self.args = (-n, 1)
        
    def testDown(self):
        self.args = None
    
    def test(self):
        expected = 0.5;
        result = main(*self.args);
        self.assertEqual(expected, result);


if _name_ == '_main_':
    unittest.main()