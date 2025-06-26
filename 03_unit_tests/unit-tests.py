import unittest

class TestString(unittest.TestCase):
    def testString(self):
        self.assertEqual('foo'.upper(), 'FOO')
    
if __name__ == '__main__':
    unittest.main()