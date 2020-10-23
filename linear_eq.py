import matplotlib.pyplot as plt
import sympy as simp
import re


'''
Linear Eq formula = y = ax + b 
'''

#eq1 = a1x + b1y + c1 = 0
#eq2 = a2x + b2y + c2 = 0

# equation solver
def solve_eq(a1 , b1 , c1 , a2 , b2 , c2):
    x = simp.Symbol('x')
    y = simp.Symbol('y')
    eq = (a1 * x + b1 * y + c1 , a2 * x + b2 * y + c2)
    global sol
    sol = simp.solve(eq , x , y)
    print(sol)
    m = re.match(r'^{x: (\d+), y: (\d+)' , str(sol))
    if m:
        return m.group(1) , m.group(2)


# defining the main plotting function
def Linear_eq(a,b,clr):
    x = list(range(0,11))
    y = [(a * ints + b) for ints in x]
    print(y)
    plt.plot(x , y ,label = 'linear' ,linestyle = '-' ,color= clr)


solx , soly = solve_eq(1 , -1 , -2 , -1 , -1 , 8)
Linear_eq(1,-2,'r')
Linear_eq(-1,8,'b')
plt.annotate('(%s,%s)'%(solx,soly) , (float(solx),float(soly)))
plt.show()






