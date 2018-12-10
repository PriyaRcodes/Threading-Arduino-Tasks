'''
  Multi Threading using Locks
  This involves 3 threads excluding the main thread.
'''

import threading
import time

lock = threading.Lock()
def Fact(n):
    lock.acquire()
    print('Thread 1 started ')
    f = 1
    for i in range(n,0,-1):
        f = f*i
    print('Factorial of',n,'=',f)
    lock.release()


def Square(n):
    lock.acquire()
    print('Thread 2 started ')
    sq = n*n
    print('Square of',n,'=',sq)
    lock.release()

def Task():
    print('Thread 3 started ')       
    time.sleep(1)                    #represents any task that takes 1 sec
    print('Task done')
    


print('This is the main thread')
n = int(input('Enter a number: '))
start_time = time.time()
T1 = threading.Thread(target=Fact,args=(n,))
T2 = threading.Thread(target=Square,args=(n,))
T3 = threading.Thread(target=Task)
T1.start()
T2.start()
T3.start()

T1.join()
T2.join()
T3.join()
print('All threads have been closed')
print('Processing time taken: ',time.time()-start_time,'seconds')    
