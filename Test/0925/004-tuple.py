#元组的数据一旦定义，不能再修改

course=('chinese','math','english','computer')
print(course)

print(course[-1])

print(course[1:3])
#查元组的元素的个数
print(len(course))

#定义只有一个元素的元组，则需要再元素后面加逗号，用来消除数学歧义
t=(1,)

#返回元组中最大/小的值
score=(12,46,894,13,457)
# print(max(score))
# print(min(score))

maxscore=max(score)
print(maxscore)

minscore=min(score)
print(minscore)
