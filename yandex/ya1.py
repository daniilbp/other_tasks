# с инета... -> правильно
n = int(input())  # 1 <= n <= 100 000 | Amount of tanks
Volumes = list(map(int, input().split()))  # Volume of each tank
answer = 0
maximal = Volumes[0]
for i in range(len(Volumes)):
    maximal = max(Volumes[i], maximal)
    if Volumes[i] < maximal:
        answer = -1
        break
print(max(Volumes) - min(Volumes) if answer == 0 else answer)

# мой вариант часа 4 потратил и неверно, где-то есть баг ах-ха-ха -> неправильно понята задача!!!
# (решение согласно мной понятому заданию корректно!)
# n = 2
# a_i_str = '1 2'
# # n = int(input())
# # a_i_str = input()
#
# try:
#     if 1 <= n <= 1e5:
#         a_i = a_i_str.split()
#
#         for number in a_i:
#             if 1 > int(float(number)) or int(float(number)) > int(1e9):
#                 raise ValueError
#         else:
#             a_l = int(float(a_i[0]))
#             a_r = int(float(a_i[-1]))
#
#             if a_l == a_r and a_i.count(a_i[0]) == n:
#                 print(0)
#             elif a_l < a_r and a_i.count(a_i[0]) + a_i.count(a_i[-1]) == n:
#                 for i, a in enumerate(a_i):
#                     if a == a_i[0]:
#                         if i > a_i.index(a_i[-1]):
#                             print(-1)
#                             break
#                 else:
#                     print(a_r - a_l)
#             else:
#                 print(-1)
#     else:
#         print(-1)
# except (ValueError, TypeError):
#     print(-1)
