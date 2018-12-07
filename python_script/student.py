class Student():
    def __init__(self,city,name):
        self.name=name
        self.city=city
        print("my name is %s and come from %s" %(name,city))

    def talk(self):
        print("hello,everybody")

stu1=Student("harry","beijing")
stu1.talk()

stu2=Student("Bob","shanghai")
stu2.talk()