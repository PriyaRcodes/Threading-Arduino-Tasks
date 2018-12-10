'''
This is without using multithreading.
'''

import time
def Fact(n):
    print('Function 1 started')
    f = 1
    for i in range(n,0,-1):
        f = f*i
    print('Factorial of',n,'=',f)

def Square(n):
    print('Function 2 started')
    sq = n*n
    print('Square of',n,'=',sq)
   

def Task():
    print('Function 3 started')
    time.sleep(1)                    #represents any task that takes 1 sec
    print('Task done')
    


print('This is the main function')
n = int(input('Enter a number: '))
start_time = time.time()
Fact(n)
Square(n)
Task()

print('Processing time : ',time.time()-start_time,'seconds')    

