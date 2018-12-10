'''
Plotting an array of values and real time data in two separate windows.
'''
from matplotlib import pyplot as plt
from matplotlib import animation as animation
from matplotlib import style
import random

f1 = plt.figure()
f2 = plt.figure()


def plotFixed():
    x1 = [1,2,3,4,5]
    y1 = [2,4,6,8,10]

   
    axis1 = f1.add_subplot(1,1,1)
    
    axis1.plot(x1,y1,'r-')
    plt.xlabel('x-values')
    plt.ylabel('y-values')
    plt.title('Plot 1\nArray of values')
    f1.show()  

def plotRealTime(interval):

    x2 = []
    y2 = []
    for i in range(21):                                             #To generate random data for plotting
        x2.append(i)
        y2.append(random.randint(0,20))                             #used randint() so that the values keep changing everytime its called
       
    
    axis2 = f2.add_subplot(1,1,1)
    axis2.clear()                                                   #To clear the previous graph
    axis2.plot(x2,y2,'o-')
    plt.xlabel('x-values')
    plt.ylabel('y-values')
    plt.title('Plot 2\nRealtime')
    

    
plotFixed()
animate = animation.FuncAnimation(f2,plotRealTime,interval = 2000)  #The graph updates every 2 sec
f2.show()   




