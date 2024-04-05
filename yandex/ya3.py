def distance(k, a, n): # 3, [3 2 5 1 2], 5
    a_sorted = sorted(a) # [1 2 2 3 5]
    s = sum(a_sorted[1:k + 1]) - k * a_sorted[0] # 2+2+3=7 - 3*1=3 = 4
    answer = {a_sorted[0]: s} # {1: 4}
    left = 0  # количество чисел слева от исходного числа в отсортированном массиве, которые ближе всего к нему
    right = k  # количество чисел справа =3

    for i in range(1, n):
        left += 1 # 1 2 3 4
        right -= 1 # 2 1 0 -1
        dif = a_sorted[i] - a_sorted[i - 1]  # разница прошлого числа и нынешнего (a_sorted[i] и a_sorted[i-1]) = 2 - 1 = 1 0 1 2
        s = s - dif * right + dif * (left - 1)  # -1 тк разница между a_sorted[i] и a_sorted[i-1] осталось та же = 4 - 1*2 +(1-1) = 2 2 4 12
        while right + i + 1 < n: # 2+1+1 = 4 4 < 5
            l = a_sorted[i] - a_sorted[i - left] # 2 - 1 = 1 1 2 4
            r = a_sorted[i + right + 1] - a_sorted[i] # 5 - 2 = 3 3 2 0
            if l > r:  # если расстояние до левого больше, чем до правого, то двигаем окно k вправо 1 > 3
                right += 1 # 0
                left -= 1 # 3
                s -= (l - r)  # и пересчитываем сумму
            else:
                break
        answer[a_sorted[i]] = s # {1:4, 2:2, 2:2, 3:4, 4:9

    for num in a:
        print(answer[num], end=' ')


def distance2(k, a, n): # 3, [3 2 5 1 2], 5
    a_sorted = sorted(a) # [1 2 2 3 5]
    s_first = abs(a_sorted[0] * k - sum(a_sorted[1:k+1])) # s для 1ого эл. в отсортированном списке
    answer = {a_sorted[0]: s_first}
    left, right = 0, k
    for i in range(1, n):
        left += 1
        right -= 1
        while i + right + 1 < n:
            l = a_sorted[i] - a_sorted[i-left]
            r = a_sorted[i+right+1] - a_sorted[i]
            if l > r:
                left -= 1
                right += 1
            else:
                break

        i_lst = a_sorted[i-left:i+right+1]
        i_lst.remove(a_sorted[i])
        s = sum(abs(a_sorted[i] - el) for el in i_lst)
        answer[a_sorted[i]] = s

    for num in a:
        print(answer[num], end=' ')


if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    distance(k, a, n)
    distance2(k, a, n)

# 4 2
# 1 2 3 4
# 3 2 2 3
# 5 3
# 3 2 5 1 2
# 4 2 8 4 2
# 6 2
# 3 2 1 101 102 103
# 3 2 3 3 2 3
