from boddle import boddle
import unittest
#module being tested
import app


class AppTest(unittest.TestCase):
    def test(self):
        req = {'key': 'test'}
        with boddle (json=req):
            assert app.test() == req

    def test_handle_event(self):
        req = {'challenge': 'accepted', 'another_var': 'some_string'}
        with boddle (json=req):
            assert app.handle_event() == req['challenge']

if __name__ == '__main__':
    unittest.main()
