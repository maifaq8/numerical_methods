import numpy as np


# отрезок интегрирования
a = 7
b = 11


# вычисление функции в точке
def f(x):
    return (-x - 3) / (x**2 + 3)


def trapezoid():
    print('Формула трапеций')

    # шаги интегрирования
    hs = [1, 0.5, 0.25]

    for h in hs:
        print(f'Вычисляем значение интеграла с шагом {h}')

        xs = [i for i in np.arange(a, b + h/2, h)]
        ys = [f(x) for x in xs]
        print(f'Таблица значений подинтегральной функции для n={len(xs)-1}')
        print('x | ', end='')
        for x in xs:
            print('{:10.7f} |'.format(x), end=' ')
        print()
        print('y | ', end='')
        for y in ys:
            print('{:10.7f} |'.format(y), end=' ')
        print()

        T = ys[0] + ys[-1]
        for i in range(1, len(ys)-1):
            T += 2 * ys[i]
        T *= h / 2
        print('Значение интеграла: {:.7f}'.format(T))
        print('-' * 20)


def simpson():
    print('Формула Симпсона')

    # шаги интегрирования
    hs = [1, 0.5]

    for h in hs:
        print(f'Вычисляем значение интеграла с шагом {h}')

        xs = [i for i in np.arange(a, b + h/2, h)]
        ys = [f(x) for x in xs]
        print(f'Таблица значений подинтегральной функции для n={len(xs)-1}')
        print('x | ', end='')
        for x in xs:
            print('{:10.7f} |'.format(x), end=' ')
        print()
        print('y | ', end='')
        for y in ys:
            print('{:10.7f} |'.format(y), end=' ')
        print()

        T = ys[0] + ys[-1]
        for i in range(1, len(ys)-1, 2):
            T += 4 * ys[i]
        for i in range(2, len(ys) - 2, 2):
            T += 2 * ys[i]
        T *= h / 3
        print('Значение интеграла: {:.7f}'.format(T))
        print('-' * 20)


def spline():
    x = [-5, -2, 1, 4, 7, 9]
    y = [-18, 4, -9, -27, -16, 24]
    h = [-1231231231, 3, 3, 3, 3, 2]
    m = [0, -5.316040, 2.069174, 6.29399, 7.911803, 0]

    # for i in range(1, 5):
    #     print(" {:6.3f} | {:6.3f} | {:6.3f} | {:6.3f} |".format(h[i] / 6, (h[i]+h[i+1])/3, h[i+1]/6, (y[i+1]-y[i])/h[i+1] - (y[i]-y[i-1])/h[i]))


    for i in range(1, 6):
        print(f'S_{i}(x) = {m[i] / (6 * h[i])} * (x-{x[i-1]})^3 +'
              f' {m[i-1] / (6 * h[i])} * ({x[i]}-x)^3 +'
              f' ({(y[i]-m[i] * h[i]**2 / 6) / h[i]}) * (x-{x[i-1]}) +'
              f' {(y[i-1]-m[i-1] * h[i]**2 / 6) / h[i]} * ({x[i]}-x)')

def main():
    spline()


if __name__ == '__main__':
    main()
