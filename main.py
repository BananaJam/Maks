import numpy as np
from math import fabs

Eps = 10**-7

def vurod():
    print('Vurod.')
    exit()
    
def result(result):
    print('Result:', result)
'''
#input block
A = []
B = []
a = [[0],[0]]
a = np.array(a)
b = [[0]]
b = np.array(b)
while not ((len(a) == len(b)) and (a.shape == (3, 3) or a.shape == (2, 2) or a.shape == (1, 1))):
    print('Введіть коректну кількість  коефіцієнтів та вільних членів')
    A = []
    B = []
    a = [[0],[0]]
    b = [[0]]
    a = np.array(a)
    b = np.array(b)
    print('Введіть по черзі коефіцієнти при невідомих (натискаючи enter між кожним рядком). Щоб завершити, введіть порожній рядок.')
    while True:
        r = input ('Наступний рядок > ')
        if not r.strip ():
            break
        A.append(list(map(float, r.split())))
        a = np.array(A)
    print('Введіть по черзі рядки  вільних членів (натискаючи enter між кожним рядком). Щоб завершити, введіть порожній рядок.')
    while True:
        r = input ('Наступний рядок > ')
        if not r.strip():
            break
        if len(r.split()) != 1:
            print('Рядок вільних членів може приймати лише 1 значення')
        else:
            B.append(list(map(float, r.split())))
            b = np.array(B)
'''
def main(a, b, Eps):
    x = []
    N = a.shape[0]

    if a.shape == (1,):
        if fabs(a[0]) <= Eps:
            vurod()
        else:
            x = b[0] / a[0]
            result(x)
    else:
        i = 0
        while True:
            k = i
            R = fabs(a[i, i])
            j = i + 1
            while j < N:
                if fabs(a[j, i]) > R:
                    k = j
                    R = a[j, i]
                j += 1
            if R < Eps:
                vurod()
            else:
                if k != j:
                    R, b[k], b[i] = b[k], b[i], R
                    j = i
                    while j < N:
                        R, a[k, j], a[i, j] = a[k, j], a[i, j], R
                        j += 1
                R = a[i, i]
                b[i] = b[i] / R
                j = 0
                while j < N:
                    a[i, j] = a[i, j] / R
                    j += 1
                k = i + 1
                while k < N:
                    j = 0
                    R = a[k, j]
                    b[k] = b[k] - R * b[i]
                    a[k, i] = 0
                    j = i + 1
                    while j < N:
                        a[k, j] = a[k, j] - R * a[i, j]
                        j += 1
                    k += 1
                i += 1
                if i > N - 1:
                    if a[N - 1, N - 1] < Eps:
                        vurod()
                    else:
                        x.append(b[N - 1] / a[N - 1, N - 1])
                        i = N - 1
                        while i >= 1:
                            R = b[i]
                            j = i + 1
                            while j < N:
                                R = R - a[i, j] * x[j]
                                j += 1
                            x.insert(i, R)
                            i -= 1
                        result(x)
                        
a = np.array([
    [1, 3, 2],
    [2, -4, -1],
    [3, 3, 1]
])

b = np.array([5, -5, -4])

main(a, b, Eps)