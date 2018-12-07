#多线程调用threading.Thread方法

from time import ctime,sleep
import threading

#定义写和说的方法
def talk(content,loop):
    for i in range(loop):
        print("Start talk: %s %s" %(content,ctime()))
        sleep(2)

def write(content, loop):
    for i in range(loop):
        print("Start write: %s %s" % (content, ctime()))
        sleep(3)

#定义和加载说和写的线程
threads=[]
t1=threading.Thread(target=talk,args=("hello,51zxw",2))
threads.append(t1)

t2=threading.Thread(target=write,args=("life is short,you need python!",2))
threads.append(t2)

#执行线程

if __name__=="__main__":
    for t in threads:
        t.start()
    for t in threads:
        t.join()
        print("all end %s" %ctime())