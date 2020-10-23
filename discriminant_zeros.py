import math

# formula for graph: ax2 + bx + c = 0
# formula for zeros: (-b +- _/D)2a

def g_inputs():
    global a
    a = int(input('Please provide value for a: '))

    global b
    b = int(input('Please provide value for b: '))

    global c
    c = int(input('Please provide value for c: '))


def discriminant_and_zeros():
    b2 = math.pow(b , 2)
    ac = 4*a*c
    D = b2 - ac
    print('Your discriminant is:', D , '\n')

    squr_D = math.sqrt(D)
    positive_multiply = -b + squr_D
    mul_a = 2 * a
    first_root = positive_multiply / mul_a
    print('Your first root is: ', first_root , '\n')

    negative_multiply = -b - squr_D
    multi_a = 2 * a
    first_root = negative_multiply / multi_a
    print('Your first root is: ', first_root)

def run():
    g_inputs()
    discriminant_and_zeros()