import numpy as np
import matplotlib.pyplot as plt


def Vihmavari():
    x1=np.arange(-12,12.5,0.5)
    y1=-(1/18)*x1**2+12
    x2=np.arange(-4,4.5,0.5)
    y2=-(1/8)*x2**2+6
    x3=np.arange(-12,-3.5,0.5)
    y3=-(1/8)*(x3+8)**2+6
    x4=np.arange(4,12.5,0.5)
    y4=-(1/8)*(x4-8)**2+6
    x5=np.arange(-4,0,0.5)
    y5=2*(x5+3)**2-9
    x6=np.arange(-4,1,0.5)
    y6=1.5*(x6+3)**2-10
    plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6)
    plt.title("Vihmavari")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.grid(True)
    plt.show()

def konn():
    x1=np.arange(-7,7.5,0.5)
    y1=(3/49)*x1**2+8
    x2=np.arange(-7,7.5,0.5)
    y2=(4/49)*x2**2+1
    x3=np.arange(-6.8,-1.5,0.5)
    y3=-0.75*(x3+4)**2+11
    x4=np.arange(2,7,0.5)
    y4=-0.75*(x4-4)**2+11
    x5=np.arange(-5.8,-2.5,0.5)
    y5=-(x5+4)**2+9
    x6=np.arange(2.8,6,0.5)
    y6=-(x6-4)**2+9
    x7=np.arange(-4,4.5,0.5)
    y7=(4/9)*x7**2-5
    x8=np.arange(-5.2,5.5,0.5)
    y8=(4/9)*x8**2-9
    x9=np.arange(-7,-2.5,0.5)
    y9=(1/16)*(x9+3)**2-6
    x10=np.arange(2.8,7.5,0.5)
    y10=-(1/16)*(x10-3)**2-6
    x11=np.arange(-7,0.5,0.5)
    y11=(1/9)*(x11+4)**2-11
    x12=np.arange(0,7.5,0.5)
    y12=(1/9)*(x12-4)**2-11
    x13=np.arange(-7,-4,0.5)
    y13=-(x13+5)**2
    x14=np.arange(4.5,7.5,0.5)
    y14=-(x14-5)**2
    x15=np.arange(-3,3.5,0.5)
    y15=(2/9)*x15**2+2
    plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,x11,y11,x12,y12,x13,y13,x14,y14,x15,y15)
    plt.title("Koon")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.grid(True)
    plt.show()

def kala():
    x1 = np.arange(0, 9.5, 0.5)
    x2 = np.arange(-10, 0.5, 0.5)    
    x3 = np.arange(-9, -2.5, 0.5)
    x4 = np.arange(-3, 9.5, 0.5)    
    x5 = np.arange(5, 9, 0.5)
    x6 = np.arange(5, 8.5, 0.5)    
    x7 = np.arange(-13, -8.5, 0.5)
    x8 = np.arange(-15, -12.5, 0.5)    
    x9 = np.arange(-15, -10, 0.5)
    x10 = np.arange(3,4,0.5)
    y1= (2/27)*x1*x1-3    
    y2= 0.04*x2*x2-3
    y3= (2/9)*(x3+6)**2+1    
    y4= (-1/12)*(x4-3)**2+6
    y5= (1/9)*(x5-5)**2+2    
    y6= (1/8)*(x6-7)**2+1.5
    y7= -0.75*(x7+11)**2+6
    y8= (-0.5)*(x8+13)**2+3
    y9= [1]*len(x9)   
    y10= [3]*len(x10)
    plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10)    
    plt.title("Kala")
    plt.ylabel("y")    
    plt.xlabel("x")
    plt.grid(True)    
    plt.show()
