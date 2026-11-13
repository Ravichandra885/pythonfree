import unittest 
from app import add
class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(20,20),20)
if __name__=='__main__':
    unittest.main()