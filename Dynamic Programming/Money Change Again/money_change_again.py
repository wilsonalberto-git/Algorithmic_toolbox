# python3


def change_naive(money):
    min_coins = float("inf")

    for num1 in range(money + 1):
        for num3 in range(money // 3 + 1):
            for num4 in range(money // 4 + 1):
                if 1 * num1 + 3 * num3 + 4 * num4 == money:
                    min_coins = min(min_coins, num1 + num3 + num4)

    return min_coins


def change(money):
    INF = 100000
    d = [0, 1, 3, 4]
    k = 3
    M = [0] * (money + 1)

    for j in range(1, money + 1):
        minimum = INF
        coin = 0

        for i in range(1, k + 1):
            if j >= d[i]:
                minimum = min(minimum, 1 + M[j - d[i]])
                coin = i
        M[j] = minimum
    return M[money]


if __name__ == '__main__':
    amount = int(input())
    print(change(amount))
