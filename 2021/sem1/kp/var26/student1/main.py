import numpy as np


# метод прогонки
def sweep(matrix):
    print('\nМетод прогонки:')
    n = len(matrix)

    # инициализируем нулями
    p = [0.0 for _ in range(n + 1)]
    q = [0.0 for _ in range(n + 1)]

    a = [0.0 for _ in range(n + 1)]
    b = [0.0 for _ in range(n + 1)]
    c = [0.0 for _ in range(n + 1)]
    d = [0.0 for _ in range(n + 1)]

    # получаем коэффициенты из матрицы
    for i in range(0, n):
        if i == 0:
            a[i+1] = 0
        else:
            a[i+1] = matrix[i][i - 1]

        b[i+1] = matrix[i][i]

        if i == n-1:
            c[i+1] = 0
        else:
            c[i+1] = matrix[i][i+1]

        d[i+1] = matrix[i][-1]

    # расчитываем коэффициенты P и Q
    print(f'p_{0}={p[0]}')
    print(f'q_{0}={q[0]}')
    for i in range(1, n + 1):
        p[i] = -c[i] / (b[i] + a[i] * p[i - 1])
        q[i] = (d[i] - a[i] * q[i - 1]) / (b[i] + a[i] * p[i - 1])
        print(f'p_{i}={p[i]}')
        print(f'q_{i}={q[i]}')

    # восстанавливаем ответ
    y = [0.0 for _ in range(n + 1)]
    y[n] = q[n]
    for i in range(n - 1, 0, -1):
        y[i] = q[i] + p[i] * y[i + 1]

    return y


def solve() -> None:
    # y(0,x)
    def f(x: float) -> float:
        return -1 + 10 * np.sin(1.57079633 * x)

    # y(t, -1)
    def f1(t: float) -> float:
        return -11 + t / 4

    # y(t, 3)
    def f2(t: float) -> float:
        return -11 + t ** 2 / 4 - 0.1 * t

    # # -2 * y(t, -1)
    # def f1(t):
    #     return 22 - t / 2

    # # -2 * y(t, 3)
    # def f2(t):
    #     return 22 - t**2 / 2 + 0.2 * t


    # коэффициенты системы
    coeffs = [-1 / 32, -3341 / 80, 211 / 32, -40]

    # шаги по x и t
    hx = 0.8
    ht = 0.025

    # границы x и t
    xleft, xright = -1, 3
    tleft, tright = 0, 0.1

    # вычисление x_i и t_i
    xs = np.linspace(xleft, xright, int((xright - xleft) / hx) + 1)
    ts = np.linspace(tleft, tright, int((tright - tleft) / ht) + 1)

    N = len(xs) - 1

    print('x = ', xs)
    print('t = ', ts)

    # инициализация y_i^0
    y = [f(x) for x in xs]

    for k in range(0, len(ts) - 1):
        print('-' * 20)
        print(f'k = {k}')

        # инициализация матрицы
        M = [[0 for _ in range(N)] for _ in range(N - 1)]

        # заполнение матрицы коэффициентами
        M[0][-1] = coeffs[3] * y[1] - (xs[1] + 4) / (ts[k + 1] + 7) - coeffs[0] * f1(ts[k + 1])
        for i in range(2, N - 1):
            M[i - 1][-1] = coeffs[3] * y[i] - (xs[i] + 4) / (ts[k + 1] + 7)
        M[N - 2][-1] = coeffs[3] * y[N - 1] - (xs[N - 1] + 4) / (ts[k + 1] + 7) - coeffs[2] * f2(ts[k + 1])

        for i in range(N - 2):
            M[i + 1][i] = coeffs[0]
            M[i][i + 1] = coeffs[2]

        for i in range(N - 1):
            M[i][i] = coeffs[1]

        print('M:')
        for line in M:
            for elem in line:
                print('{:13.8f}|'.format(elem), end=' ')
            print()

        # решение системы методом прогонки
        y = sweep(M)
        print('y:')
        print('{:2d}| {:13.8f}|'.format(0, f1(ts[k+1])))
        for i in range(1, len(y)):
            print('{:2d}| {:13.8f}|'.format(i, y[i]))
        print('{:2d}| {:13.8f}|'.format(len(y), f2(ts[k+1])))


def main():
    solve()

if __name__ == '__main__':
    main()
