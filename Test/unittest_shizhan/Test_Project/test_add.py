from calculator import *
from StartEnd import *

class Test_add(Setup_tearDown):
    def test_add1(self):
        j=Math(2,4)
        self.assertEqual(j.add(),6)

    def test_add2(self):
        j=Math(8,8)
        self.assertEqual(j.add(),10)