# N, X, T, a_i = 3, 5, 2, [5, 10, 6]
# N, X, T, a_i = 5, 19, 32, [36, 10, 72, 4, 50]
# N, X, T, a_i = 4, 25, 10, [1, 10, 42, 9]
# N, X, T, a_i = 4, 25, 0, [1, 10, 42, 25]
N, X, T, a_i = 4, 0, 0, [1, 10, 42, 25]

# N, X, T = map(int, input().split())
# a_i = list(map(int, input().split()))

sort_lst_in_lst = sorted([[abs(el - X), el] for el in a_i])
answer = []

i = 0

if X == 0 and T == 0:
    print(0)
else:
    try:
        while T > 0:
            T -= sort_lst_in_lst[i][0]
            if T >= 0:
                answer.append(a_i.index(sort_lst_in_lst[i][1]) + 1)
                i += 1

        if T == 0 and sort_lst_in_lst[0][1] == X:
            answer.append(a_i.index(sort_lst_in_lst[0][1]) + 1)

        x = len(answer)
        print(int(x))
        if x != 0:
            for el in answer:
                print(el, end=' ')
    except RuntimeError:
        print(0)
