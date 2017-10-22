from boddle import boddle
import unittest
#module being tested
import app


class AppTest(unittest.TestCase):
    def test_return_key(self):
        req = {'key': 'test'}
        with boddle (json=req):
            assert app.return_key() == req

if __name__ == '__main__':
    unittest.main()
