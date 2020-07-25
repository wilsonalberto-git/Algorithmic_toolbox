# python3


def last_digit_of_the_sum_of_squares_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum([f ** 2 for f in fibonacci_numbers]) % 10


def last_digit_of_the_sum_of_squares_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18

    array_f = [0, 1]
    result = [0, 1]
    if n <= 1:
        return array_f[n]
    previousMod = 0
    currentMod = 1
    sm = previousMod + currentMod
    for i in range(60):
        tempMod = previousMod
        previousMod = currentMod % 10
        currentMod = (tempMod + currentMod) % 10
        sm = (sm + currentMod**2) % 10
        result.append(sm)
        array_f.append(currentMod)
    index = (n % 60)
    return result[index]


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_squares_of_fibonacci_numbers(input_n))
    #print(last_digit_of_the_sum_of_squares_of_fibonacci_numbers_naive(input_n))
