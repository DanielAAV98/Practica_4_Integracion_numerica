import math

def error (j,x):
    
    if(j==0):
        e=abs(1-x/1.3082506046426)*100
    if(j==1):
        e=abs(1-x/0.63661977237)*100
    if(j==2):
        e=abs(1-x/1.00745963140)*100
    if(j==3):	
        e=abs(1-x/0.60233735788)*100
    if(j==4):
        e=abs(1-x/0.5449871)*100
        
    return e

def f(x):
    #f = 1 + (math.exp(-x))*(math.sin(4*x))
    #f=math.sin(math.pi*x)
    #f=1 + (math.exp(-x))*(math.cos(4*x));
    #f=(math.sin(x**(1/2)));
    f=math.exp(x**2);
    return f

def h(n,a,b):
    h = (b-a)/n
    return h

def trapecio (a,b):
    s = (h(1,a,b)/2) * (f(a)+f(b))
    return s

def simpson13(a,b):
    s = (h(2,a,b)/2) * (f(a)+4*f(a+h(2,a,b))+f(b))
    return s

def simpson38(a,b):
    s = (h(3,a,b)*3/8) * (f(a)+3*f(a+h(3,a,b))+3*f(a+h(3,a,b)*2)+f(b))
    return s

def boole(a,b):
    s = (h(4,a,b)*2/45) * (7*f(a)+32*f(a+h(4,a,b))+12*f(a+h(4,a,b)*2)+32*f(a+h(4,a,b)*3)+7*f(b))
    return s

def main ():
    a = float(input("limite inferior: "))
    b = float(input("limite superior: "))
    print("--------------------------")
    print("Trapecio: ", "\t%0.8f" %trapecio(a,b),"error:\t%0.8f" %error(4,trapecio(a,b)),"\nSimpson 1/3: ","\t%0.8f" %simpson13(a,b),"error:\t%0.8f" %error(4,simpson13(a,b)),"\nSimpson 3/8: ","\t%0.8f" %simpson38(a,b),"error:\t%0.8f" %error(4,simpson38(a,b)),"\nBoole: ","\t%0.8f" %boole(a,b),"error:\t%0.8f" %error(4,boole(a,b)))
main()