#元组
course=('chinese','math','English','computer')
print(course)
print(course[2])
print(course[-1])
print(course[1:3])
print(course[1:])
print(course [:-1])

print(len(course))

#如果定义之有1个元素的元组，则需要在元素后面加逗号，用来消除数学歧义
t=(1,)

#返回元组中的最大值
score=(2,34,1,23,0.9,34)
print(max(score))