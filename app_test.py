from boddle import boddle
import unittest
#module being tested
import app


class AppTest(unittest.TestCase):
    def test(self):
        req = {'key': 'test'}
        with boddle (json=req):
            assert app.test() == req

    def test_answer_challenge(self):
        req = {'challenge': 'accepted', 'another_var': 'some_string'}
        with boddle (json=req):
            assert app.answer_challenge() == req['challenge']

if __name__ == '__main__':
    unittest.main()
