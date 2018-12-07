#数组
student=['jck','bob','harry','mark']
print(student)

#通过索引来查看列表元素
print(student[0])

print(student[-1])

#超出数组，数组越界
# print(student[4])

#添加元素

#在最后一个位置添加
student.append('51zxw')
print(student)


#在指定位置添加元素
student.insert(1,'hello')
print(student)


#修改元素

student[0]='ssss'
print(student)

#删除元素

#在末尾删除元素
student.pop()
print(student)

#指定位置元素删除

student.pop(2)
print(student)

