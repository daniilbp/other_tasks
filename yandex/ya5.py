import math


n = int(input())
divider = 10 ** 9 + 7
list = [1]

with open('../text.csv', 'a', encoding='utf-8') as file:

    # if n == 1:
    #     good_res = 1
    #
    # else:
    for n in range(2, n+1):

        good_res = 0
        x = n - 1
        for k in range(n):
            if x - k < 2:
                last_el = 0
            else:
                last_el = (math.factorial(x - k) // (2 * math.factorial(x - k - 2)))
            good_res += int(((-1) ** k) * (math.factorial(x) // (math.factorial(k) * math.factorial(x - k))) * (2 ** last_el))
        if good_res > divider:
            good_res = (n * good_res) % divider
        else:
            good_res *= n

        file.write(f'{good_res} ')
        # list.append(good_res)

    print(good_res)
    # print(list[-1])
