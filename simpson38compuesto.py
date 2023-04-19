import math
funciones=["f(x)= 1+sin(4x)*e^(-x)\t","f(x)= sin(pi*x)\t\t","f(x)= 1+cos(4x)*e^(-x)\t","f(x)= sin(x^1/2)\t","f(x)= e^(x^2)\t\t"]
num_itera=[3,6,100,1000]

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

def f(x,j):
    
    if(j==0):
        f=1 + (math.exp(-x))*(math.sin(4*x));
    if(j==1):
        f=math.sin(math.pi*x)
    if(j==2):
        f=1 + (math.exp(-x))*(math.cos(4*x));
    if(j==3):
        f=(math.sin(x**(1/2)));
    if(j==4):
        f=math.exp(x**2);
    
    return f

def Simpson38compuesto(a,b,n,j):
    
    h=(b-a)/(n)
    s=f(a,j)+f(b,j)
    for i in range (1,n):
        if (i%3==0):
            s+=2*f(a+(h*i),j)
        else:
            s+=3*f(a+(h*i),j)
    s*=((3*h)/8)
    
    return s
def main():
    for j in num_itera:
        print("------------------------------------------------------------------------")
        print("Numero de iteraciones: ", j)
        
        for i in range (0,5):
            if (i<4):
                print (funciones[i],"a=0 b=1\t: %0.8f" % Simpson38compuesto(0,1,j,i),"\nPorcentaje de error: %0.8f" % error(i,Simpson38compuesto(0,1,j,i)),"\n")
            else:
                print (funciones[i],"a=0 b=1/2\t: %0.8f" % Simpson38compuesto(0,0.5,j,i),"\nPorcentaje de error: %0.8f" % error(i,Simpson38compuesto(0,0.5,j,i)),"\n")
main()       

