# f=open('555.txt','r')
# lines=f.readlines()
# print(lines)
#
# for line in lines:
#     print(line.split(':')[0])



# encoding: UTF-8
# import csv
# csv_file=csv.reader(open('444.csv','r'))
#
# print(csv_file)
#
# for stu in csv_file:
#     print(stu[2])


import csv
stu1=['tom',29,'shangrao']
stu2=['berry',25,'xiangjiang']
#打开文件
out=open('444.csv','a',newline='')
#设定写入模式
new_write=csv.writer(out,dialect='excel')
#写入具体内容
new_write.writerow(stu1)
new_write.writerow(stu2)
#提示写入完成
print("write over!")