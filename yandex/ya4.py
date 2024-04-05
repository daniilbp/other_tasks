from sympy.core.cache import cacheit
from sympy import binomial
import numpy as np
import math


# @cacheit
# def a2(n):
#     return 1 if n == 0 else 2**binomial(n, 2) - np.sum(a2(k)*binomial(n, k) for k in range(n))
#
#
# n_graph = int(input())
# res = n_graph * a2(n_graph-1)
# print('full:', res)
#
# if res > 10 ** 9 + 7:
#     res = res % (10 ** 9 + 7)
# print('cut:', res)


n = int(input())

if n == 1:
    good_res = 1
elif n == 2:
    good_res = 0
elif n == 3:
    good_res = 3
else:
    # good_res = 3
    # upper = 1
    # res = 4
    for el in range(4, n+1):
        # if good_res > 10 ** 9 + 7:
        #     good_res = (el * res) % (10 ** 9 + 7)
        # else:
        #     good_res = el * res # 16 205
        # print(good_res)
        #
        # m = int(math.factorial(el) // (2 * math.factorial(el - 2))) # 6 10
        # upper += (el - 1) # 4 8
        # print(upper)
        # res = 0
        # for k in range(upper+1):
        #     res += int(math.factorial(m) // (math.factorial(k) * math.factorial(m - k))) # 57 1013
        # print(res)
        # res -= good_res # 41 808
        # print(res)
        good_res = 0
        for k in range(n):
            good_res += int(((-1) ** k) * (math.factorial(n-1) // (math.factorial(k) * math.factorial(n - 1 - k))) * (2 ** (math.factorial(n-1-k) // 2 * (math.factorial(n - 1 - k - 2)))))
        good_res %= (10 ** 9 + 7)
        print('Кол-во вершин:', n, '|Кол-во ребер:', m, '|Верхняя граница:', upper, '|Кол-во графов:', nums_graphs)
print(good_res)

# print(good_res)

# else:
#     m = int(math.factorial(n) // (2 * math.factorial(n - 2)))
#     nums_graphs = (2 ** m) % (10 ** 9 + 7)
#     print('Кол-во вершин:', n, 'Кол-во ребер:', m, '| Кол-во графов:', nums_graphs)



