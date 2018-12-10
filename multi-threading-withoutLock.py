import threading
import time

def Fact(n):
    print('Thread 1 started')
    f = 1
    for i in range(n,0,-1):
        f = f*i
    print('Factorial of',n,'=',f)


def Square(n):
    print('Thread 2 started')
    sq = n*n
    print('Square of',n,'=',sq)

def Task():
    print('Thread 3 started')
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
print('Processing time: ',time.time()-start_time,'seconds')    
    


