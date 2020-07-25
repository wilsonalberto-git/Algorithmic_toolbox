# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 5

    array_f = [0, 1]
    if n <= 1:
        return array_f[n]
    previousMod = 0
    currentMod = 1
    for i in range(n-1):
        tempMod = previousMod
        previousMod = currentMod % m
        currentMod = (tempMod + currentMod) % m
        array_f.append(currentMod)
        if currentMod == 1 and previousMod == 0:
            index = (n % (i + 1))
            return array_f[index]
    return currentMod


if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
