import unittest
from calculator import Math

class Test_StartEnd(unittest.TestCase):
    def setUp(self):
        print("test start")

    def tearDown(self):
        print("test end")

class Testadd(Test_StartEnd):
    def test_add(self):
        a=Math(3,5)
        self.assertNotEqual(a.add(), 10)

class Testsub(Test_StartEnd):
    def test_sub(self):
        a=Math(3,5)
        self.assertNotEqual(a.add(), 10)

if __name__=="__main__":
    suite = unittest.TestSuite()
    suite.addTest(Testadd("test_add"))
    suite.addTest(Testsub("test_sub"))
    runner = unittest.TextTestRunner()
    runner.run(suite)


# if __name__ == '__main__':
#     unittest.main()