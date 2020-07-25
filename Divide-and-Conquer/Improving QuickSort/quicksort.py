# python3

from random import randint


def partition3(array, left, right):
    pivot_value = array[left]
    m_one = i = left
    m_two = right
    while i <= m_two:
        if array[i] < pivot_value:
            array[i], array[m_one] = array[m_one], array[i] #swap instruction
            m_one += 1
            i += 1
        elif array[i] == pivot_value:
            i += 1
        else:
            array[i], array[m_two] = array[m_two], array[i] #swap instruction
            m_two -= 1
        pIndexes = [m_one, m_two]
    return pIndexes


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left] # swap instruction
    pIndex = partition3(array, left, right)
    randomized_quick_sort(array, left, pIndex[0] - 1)
    randomized_quick_sort(array, pIndex[1] + 1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
