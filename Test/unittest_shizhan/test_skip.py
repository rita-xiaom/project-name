import unittest
from calculator import *

class Test_StartEnd(unittest.TestCase):
    def setUp(self):
        print("test start")

    def tearDown(self):
        print("test end")

class Testadd(Test_StartEnd):
    @unittest.skipUnless(0>1,"skip test_a")
    def test_a(self):
        a=Math(3,5)
        self.assertNotEqual(a.add(), 10)
    @unittest.skipIf(4>3,"skip test_c")
    def test_c(self):
        a=Math(2,5)
        self.assertEqual(a.add(),7)
# @unittest.skip("Testsub")
class Testsub(Test_StartEnd):
    @classmethod
    def setUpClass(cls):
        print("Class module start test>>>>>>>>>")

    @classmethod
    def tearDownClass(cls):
        print("Class module test end <<<<<<<<")
    def test_b(self):
        a=Math(3,5)
        self.assertNotEqual(a.add(), 10)
    @unittest.expectedFailure
    def test_d(self):
        a = Math(3, 5)
        self.assertNotEqual(a.add(), 10)



if __name__ == '__main__':
    unittest.main()