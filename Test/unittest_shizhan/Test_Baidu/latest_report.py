import os
report_dir='./test_report'
#列举test_report目录下的所有文件（名），结果以列表形式返回。
lists=os.listdir(report_dir)
print(lists)
#sort按key的关键字进行升序排序，lambda的入参fn为lists列表的元素，
# 获取文件的最后修改时间，所以最终以文件时间从小到大排序
#最后对lists元素，按文件修改时间大小从小到大排序。
lists.sort(key=lambda fn:os.path.getatime(report_dir+'\\'+fn))
print("the latest report is "+lists[-1])
#获取最新文件的绝对路径，列表中最后一个值,文件夹+文件名
file=os.path.join(report_dir,lists[-1])
print(file)