import numpy as np


def newton_linearization():
    def f1(x, y, z):
        return -5 * x + 4 * y + z

    def f2(x, y, z):
        return 5 * x**2 + 2 * y**2 + 5 * z - 5

    def f3(x, y, z):
        return 5 * x * y - 4 * z

    # вычисление обратной матрицы Якоби
    def inv_jakobi(x, y):
        return 1 / (5 * (10 * x**2 + 57 * x - 4 * (y - 9) * y)) * np.matrix(
            [[-25 * x - 16 * y, 5 * x + 16, 4 * (5 - y)],
             [5 * (8 * x + 5 * y), -5 * (y - 4), 5 * (2 * x + 5)],
             [10 * (5 * x**2 - 2 * y**2), 5 * (5 * x + 4 * y), -20 * (2 * x + y)]
             ]
        )

    def solve(x, y, z, iters=4):
        arr = np.matrix([[x], [y], [z]])
        print('| n |      x      |      y      |      z      |   f1(x,y,z) |  f2(x,y,z)  |  f3(x,y,z)  |')
        for i in range(iters + 1):
            x, y, z = arr[0, 0], arr[1, 0], arr[2, 0]
            s = '| {:1d} | {:11.7f} | {:11.7f} | {:11.7f} | {:11.7f} | {:11.7f} | {:11.7f} |'.\
                format(i, x, y, z, f1(x,y,z), f2(x,y,z), f3(x,y,z))
            print(s)

            # итерационная формула
            arr = arr - inv_jakobi(x, y) * np.matrix([[f1(x, y, z)], [f2(x, y, z)], [f3(x, y, z)]])

    print('Point 1')
    solve(1, 1, 1)
    print('Point 2')
    solve(-1, -1, 1)


def main():
    newton_linearization()


if __name__ == '__main__':
    main()
