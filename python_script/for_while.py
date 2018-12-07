#for 循环
student=['mack','bob','tony','tom']
for stu in student:
    print(stu)

#python提供一个range()函数，可以生成一个整数序列，比如range(10)生成的序号是从0开始，小于10的整数

sum = 0
for i in range(11):
    sum=sum+i
print(sum)


#while 循环，只要条件满足，就不断循环，条件不满足时，退出循环

n =10
while n>0:
    n=n-1
    print(n)
print("over")
