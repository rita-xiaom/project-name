import unittest
from calculator import Math

class Test_add(unittest.TestCase):
    def setUp(self):
        print("test start")

    def test_add1(self):
        j=Math(3,5)
        self.assertEqual(j.add(),8)

    def test_add2(self):
        j = Math(3, 5)
        self.assertNotEqual(j.add(),10)

    def test_add3(self):
        self.assertIs("2222","2222")

    def test_add4(self):
        self.assertIn("jd","jdej")

    def test_add5(self):
        j=Math(5,10)
        self.assertTrue(j.add()>10)

    def tearDown(self):
        print("test end")



class Test_sub(unittest.TestCase):
    def setUp(self):
        print("test start")

    def test_sub1(self):
        i = Math(3, 5)
        self.assertEqual(i.sub(), 0)

    def test_sub2(self):
        i = Math(3, 5)
        self.assertNotEqual(i.sub(), 0)

    def tearDown(self):
        print("test end")


if __name__=="__main__":
    suite=unittest.TestSuite()
    suite.addTest(Test_add("test_add5"))
    suite.addTest(Test_sub("test_sub2"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
