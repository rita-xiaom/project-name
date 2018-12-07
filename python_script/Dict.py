
#字典值
student={1:'mack',2:'jack',3:'bob',4:'micle'}
print(student[2])

#增加
student[5]='senzhen'
print(student)

#修改
student[2]='zz'
print(student)

#删除
del student[2]
print(student)

#清空字典值
student.clear()
print(student)

#删除字典
del student