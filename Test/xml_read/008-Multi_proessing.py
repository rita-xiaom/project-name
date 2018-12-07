#多进程调用multiprocessing.Process方法

from time import ctime,sleep
import multiprocessing


#定义说和读的方法
def talk(content,loop):
    for i in range(loop):
        print("start talk: %s %s" %(content,ctime()))
        sleep(2)

def write(content,loop):
    for i in range(loop):
        print("start write: %s %s" %(content,ctime()))
        sleep(3)
#定义和加载进程

proess=[]
p1=multiprocessing.Process(target=talk,args=('hello,tom',2))
proess.append(p1)

p2=multiprocessing.Process(target=write,args=('python3',2))
proess.append(p2)

#执行进程
if __name__=='__main__':
    for p in proess:
        p.start()
    for p in proess:
        p.join()
        print("all proces is run %s" %ctime())