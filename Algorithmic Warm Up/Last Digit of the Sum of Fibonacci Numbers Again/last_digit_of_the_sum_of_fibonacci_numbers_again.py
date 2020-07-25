# python3


def last_digit_of_the_sum_of_fibonacci_numbers_again_naive(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index == 0:
        return 0

    fibonacci_numbers = [0] * (to_index + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, to_index + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers[from_index:to_index + 1]) % 10


def last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index == 0:
        return 0
    from_index = from_index % 60
    to_index = to_index % 60
    if from_index > to_index:
        to_index = to_index + 60
    array_f = [0, 1]
    previousMod = 0
    currentMod = 1
    if from_index < 2:
        sm = previousMod + currentMod
        result = []
    else:
        sm = 0
        result = [0, 1]
    for i in range(2, 120):
        tempMod = previousMod
        previousMod = currentMod % 10
        currentMod = (tempMod + currentMod) % 10
        if i >= from_index and i<= to_index:
            sm = (sm + currentMod) % 10
            result.append(sm)
        array_f.append(currentMod)
    return sm


if __name__ == '__main__':
    input_from, input_to = map(int, input().split())
    #print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to))
    print(last_digit_of_the_sum_of_fibonacci_numbers_again_naive(input_from, input_to))

