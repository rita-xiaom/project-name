from calculator import *
from StartEnd import *

class Test_sub(Setup_tearDown):
    def test_sub1(self):
        j=Math(2,4)
        self.assertEqual(j.add(),2)

    def test_sub2(self):
        j=Math(8,8)
        self.assertEqual(j.add(),0)