import unittest
from calculator import *

class Test_StartEnd(unittest.TestCase):
    def setUp(self):
        print("test start")

    def tearDown(self):
        print("test end")

class Testadd(Test_StartEnd):
    def test_a(self):
        a=Math(3,5)
        self.assertNotEqual(a.add(), 10)
    def test_c(self):
        a=Math(2,5)
        self.assertEqual(a.add(),7)

class Testsub(Test_StartEnd):
    def test_b(self):
        a=Math(3,5)
        self.assertNotEqual(a.add(), 10)

    def test_d(self):
        a = Math(3, 5)
        self.assertNotEqual(a.add(), 10)



if __name__ == '__main__':
    unittest.main()