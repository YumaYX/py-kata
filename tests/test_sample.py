import unittest

from src import modules

class TestSample(unittest.TestCase):
    def setUp(self):
        print("setUp()")

    def tearDown(self):
        print("tearDown()")

    def testSample(self):
        mc = modules.MyClass()
        self.assertEqual("hello", mc.mymethod())
