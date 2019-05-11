import numpy as np
import matplotlib.pyplot as plt

class PointData(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def getPoint(self):
        return (self.x, self.y)

def GongZhenFunc(n):
    y=1.08722 * (70000*20 - n*n - (float)(n/3.0)*(n/3.0) - (float)(n/5.0)*(n/5.0) -
    (float)(n/8.0)*(n/8.0) - (float)(250000-(n-499)*(n-499))*2.2)
    return (n,y)

def eocgongzhen(n ):
    return 0.945 * (40000*20 - n*n - (float)(n/3)*(n/3) - (float)(n/5)*(n/5) -
    (float)(n/8)*(n/8) - (float)(250000-(n-499)*(n-499))*2.2)


if __name__ == "__main__":
    '''
    x = np.linspace(0, 2 * np.pi, 100)
    y1, y2 = np.sin(x), np.cos(x)
 
    plt.plot(x, y1)
    plt.plot(x, y2)
 
    plt.title('line chart')
    plt.xlabel('x')
    plt.ylabel('y')
 
    plt.show()
    '''
    '''
    sum = 0.0
    xslice = [] 
    yslice = []
    for i in range(1000):
        res = GongZhenFunc(i)
        sum = sum + res[1]
        yslice.append(res[1])
        xslice.append(i)
        print("tokennum is %f,  totalnum is %f" %(res[1], sum))

    
    
    plt.plot(xslice, yslice)
    plt.title('gognzhen chart')
    plt.xlabel('x')
    plt.ylabel('y')
    #plt.legend()
    plt.show()    
    '''

    sum = 0.0
    xslice = [] 
    yslice = []
    for i in range(465):
        res = eocgongzhen(i)
        sum = sum + res
        yslice.append(res)
        xslice.append(i)
        print("tokennum is %f,  totalnum is %f" %(res, sum))
    
    plt.plot(xslice, yslice)
    plt.title('gognzhen chart')
    plt.xlabel('x')
    plt.ylabel('y')
    #plt.legend()
    plt.show()    
