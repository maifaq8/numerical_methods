b = [
    [0, 1/7, 11/42],
    [2/11, 0, 1/33],
    [-9/38, -7/38, 0]
]


print("*** МЕТОД ПРОСТЫХ ИТЕРАЦИЙ ***")

max1 = 0.0
max2 = 0.0
for i in range(0, 3):
    temp1 = 0.0
    temp2 = 0.0
    for j in range(0,3):
        temp1 += abs(b[i][j])
        temp2 += abs(b[j][i])

    max1 = max(max1, temp1)
    max2 = max(max2, temp2)


bNorm = min(max1, max2)
print("bNorm: ", bNorm)

beta = [197/42, -203/33, -145/19]
betaNorm = 0.0
for i in range(0, 3):
    betaNorm = max(betaNorm, abs(beta[i]))
print("betaNorm: ", betaNorm)


x = 197/42
y = -203/33
z = -145/19
print(" № |      x      |       y      |       z      |   epsilon   |    delta    |")
print("{:2d} | {:.9f} | {:.9f} | {:.9f} |             |             |".format(0, x, y, z))
for i in range(11):

    xNext = 1/7 * y + 11/42 * z + 197/42
    yNext = 2/11 * x + 1/33 * z - 203/33
    zNext = -9/38 * x - 7/38 * y - 145/19

    epsilon = (bNorm ** (i+1)) / (1 - bNorm) * betaNorm
    xDiff = abs(x - xNext)
    yDiff = abs(y - yNext)
    zDiff = abs(z - zNext)
    delta = max(xDiff, yDiff, zDiff)


    x = xNext
    y = yNext
    z = zNext

    print("{:2d} | {:.9f} | {:.9f} | {:.9f} | {:.9f} | {:.9f} |".format(i+1, x, y, z, epsilon, delta))

print("Подставим полученные на последней итерации значения в исходную систему")

trueRes1 = 197
trueRes2 = -203
trueRes3 = 290

res1 = 42*x - 6*y - 11*z
res2 = -6*x + 33*y - z
res3 = -9*x - 7*y - 38*z


print("42*x - 6*y - 11*z = ", res1)
print("-6*x + 33*y - z = ", res2)
print("-9*x - 7*y - 38*z = ", res3)

print("Отличие от настоящего ответа: ")
print(abs(res1 - trueRes1 ))
print(abs(res2 - trueRes2 ))
print(abs(res3 - trueRes3 ))


print("\n*** МЕТОД ЗЕЙДЕЛЯ ***")
x = 197/42
y = -203/33
z = -145/19
print(" № |      x      |       y      |       z      |   epsilon   |    delta    |")
print("{:2d} | {:.9f} | {:.9f} | {:.9f} |             |             |".format(0, x, y, z))
for i in range(5):
    xNext = 1/7 * y + 11/42 * z + 197/42
    yNext = 2/11 * xNext + 1/33 * z - 203/33
    zNext = -9/38 * xNext - 7/38 * yNext - 145/19

    epsilon = (bNorm ** (i+1)) / (1 - bNorm) * betaNorm
    xDiff = abs(x - xNext)
    yDiff = abs(y - yNext)
    zDiff = abs(z - zNext)
    delta = max(xDiff, yDiff, zDiff)

    x = xNext
    y = yNext
    z = zNext


    print("{:2d} | {:.9f} | {:.9f} | {:.9f} | {:.9f} | {:.9f} |".format(i+1, x, y, z, epsilon, delta))

print("Подставим полученные на последней итерации значения в исходную систему")

trueRes1 = 197
trueRes2 = -203
trueRes3 = 290

res1 = 42*x - 6*y - 11*z
res2 = -6*x + 33*y - z
res3 = -9*x - 7*y - 38*z


print("42*x - 6*y - 11*z = ", res1)
print("-6*x + 33*y - z = ", res2)
print("-9*x - 7*y - 38*z = ", res3)

print("Отличие от настоящего ответа: ")
print(abs(res1 - trueRes1 ))
print(abs(res2 - trueRes2 ))
print(abs(res3 - trueRes3 ))
