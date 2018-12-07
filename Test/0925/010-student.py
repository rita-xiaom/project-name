class Student():
    def __init__(self,name,city):
        self.name=name
        self.city=city
        print("my name is %s and come from %s" %(name,city))
    def talk(self):
        print("hello,51zxw")

stu1=Student('jack','beijing')
stu1.talk()

stu2=Student('mark','shanghai')
stu2.talk()

