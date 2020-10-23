import matplotlib.pyplot as plt

# equation = y = ax2 + bx + c

def Quadratic_eq(a,b,c,clr):
    x = list(range(-10,11))
    y = [(a * ints ** 2 + b * ints + c) for ints in x]
    print(y)
    plt.plot(x , y , color= clr)
    plt.show()

a = 1
b = 0
c = 0

Quadratic_eq(a,b,c,'r')