import numpy as np


def euler():
    def f(x, y):
        return -y + x**2 -2

    x_left = -2
    x_right = 2

    x_0 = x_left
    y_0 = 6
    hs = [1, 0.5, 0.4]

    for h in hs:
        x = x_0
        y = y_0

        print(f'h = {h}')
        print(' i |      x     |      y     |')

        for i in range(len(np.linspace(x_left, x_right, int((x_right-x_left)/h)+1))):
            x_next = x + h
            y_next = y + h * f(x, y)
            print('{:2d} | {:10.6f} | {:10.6f} |'.format(i, x, y))


            x = x_next
            y = y_next


def runge_kutta():
    def f(x, y):
        return -y + x**2 -2

    x_left = -2
    x_right = 2

    x_0 = x_left
    y_0 = 6
    hs = [1, 0.5]

    for h in hs:
        x = x_0
        y = y_0

        print(f'h = {h}')
        print(' i |      x     |      y     |      K1    |      K2    |      K3    |      K4    |')

        for i in range(len(np.linspace(x_left, x_right, int((x_right-x_left)/h)+1))):
            K1 = f(x, y)
            K2 = f(x + h/2, y + h/2 * K1)
            K3 = f(x + h/2, y + h/2 * K2)
            K4 = f(x + h, y + h * K3)

            x_next = x + h
            y_next = y + h/6 * (K1 + 2*K2 + 2*K3 + K4)
            print('{:2d} | {:10.7f} | {:10.7f} | {:10.7f} | {:10.7f} | {:10.7f} | {:10.7f} |'.format(i, x, y, K1, K2, K3, K4))


            x = x_next
            y = y_next



def finite_difference():
    def K(x):
        return 1

    def L(x):
        return -1

    def M(x):
        return -3

    def F(x):
        return -2 * x**2 - x - 5


    h = 0.2
    x_left = 2
    x_right = 3
    x = np.linspace(x_left, x_right, int((x_right-x_left)/h)+1)
    R = 0
    S = 1
    T = 2/5
    V = 0
    W = 1
    Z = -1

    a = 0
    b = -R/h + S
    c = R/h
    d = T

    print('b1={}, c1={}, d1={}'.format(b, c, d))
    print('i |     a       |       b     |      c      |       d     |')
    print('1 | {:11.7f} | {:11.7f} | {:11.7f} | {:11.7f} |'.format(a, b, c, d))
    for i in range(1, len(x)-1):
        a = K(x[i]) / (h**2) - L(x[i]) / (2 * h)
        b = -2 * K(x[i]) / (h**2) + M(x[i])
        c = K(x[i]) / (h**2) + L(x[i]) / (2 * h)
        d = F(x[i])
        print('{:1d} | {:11.7f} | {:11.7f} | {:11.7f} | {:11.7f} |'.format(i+1, a, b, c, d))

    a = V/h
    b = -V/h - W
    c = 0
    d = -Z
    print('{:1d} | {:11.7f} | {:11.7f} | {:11.7f} | {:11.7f} |'.format(len(x), a, b, c, d))


def euler_second():
    def f(x, y, z):
        return 2 * z - 3 * y - 2 * x + 3

    x_left = 1
    x_right = 3
    
    hs = [0.5, 0.25, 0.2]

    for h in hs:
        x = x_left
        y = -8
        z = 8
        xs = int((x_right-x_left)/h)+1

        print(f'h = {h}')
        print('  i |      x      |      y      |      z      |')

        for i in range(xs):
            x_next = x + h
            y_next = y + h * z
            z_next = z + h * f(x, y, z)

            print(' {:2d} | {:11.7f} | {:11.7f} | {:11.7f} |'.format(i, x, y, z))

            x = x_next
            y = y_next
            z = z_next

        
def runge_kutta_second():
    def f(x, y, z):
        return 2 * z - 3 * y - 2 * x + 3

    x_left = 1
    x_right = 3
    
    hs = [0.5, 0.25]

    for h in hs:
        x = x_left
        y = -8
        z = 8
        xs = int((x_right-x_left)/h)+1

        print(f'h = {h}')
        print('  i |      x      |      y      |      z      |     K1y     |     K2y     |     K3y     |     K4y  '
              '   |     K1z     |     K2z     |     K3z     |     K4z     |')

        for i in range(xs):
            K1y = z
            K1z = f(x, y, z)
            K2y = z + h/2 * K1z
            K2z = f(x + h/2, y + h/2 * K1y, z + h/2 * K1z)
            K3y = z + h/2 * K2z
            K3z = f(x + h/2, y + h/2 * K2y, z + h/2 * K2z)
            K4y = z + h*K3z
            K4z = f(x + h, y + h * K3y, z + h * K3z)

            x_next = x + h
            y_next = y + h/6 * (K1y + 2*K2y + 2*K3y + K4y)
            z_next = z + h/6 * (K1z + 2*K2z + 2*K3z + K4z)

            print(' {:2d} | {:11.7f} | {:11.7f} | {:11.7f} | {:11.7f} | {:11.7f} | {:11.7f} | {:11.7f} | {:11.7f} | '
                  '{:11.7f} | {:11.7f} | {:11.7f} |'.format(i, x, y, z, K1y, K2y, K3y, K4y, K1z, K2z, K3z, K4z))

            x = x_next
            y = y_next
            z = z_next




def main():
    print('euler')
    euler()
    print('runge_kutta')
    runge_kutta()
    print('euler_second')
    euler_second()
    print('runge_kutta_second')
    runge_kutta_second()
    print('finite')
    finite_difference()

if __name__ == '__main__':
    main()
