# N, c_i, r_i, K, s_j = 4, [1, 2, 3, 4], [1, 2, 1, 2], 5, [1, 2, 3, 1, 4]
# N, c_i, r_i, K, s_j = 3, [42, 3, 14], [1, 3, 3], 4, [3, 14, 14, 3]

N = int(input())
c_i = [int(el) for el in input().split()]
r_i = [int(el) for el in input().split()]
K = int(input())
s_j = [int(el) for el in input().split()]

dct = {c_i[i]: r_i[i] for i in range(N)}
count = 0

for i in range(K-1):
    if dct[s_j[i]] != dct[s_j[i+1]]:
        count += 1

print(count)
