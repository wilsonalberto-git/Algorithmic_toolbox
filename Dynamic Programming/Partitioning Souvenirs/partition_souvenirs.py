# python3

from itertools import product
from sys import stdin


def partition3(values):
    global result
    assert 1 <= len(values) <= 20
    assert all(1 <= v <= 70 for v in values)

    third, module = divmod(sum(values), 3)
    if len(values) < 3 or module or max(values) > third:
        result = 0
        return result

    list = [[0] * (len(values) + 1) for _ in range(third + 1)]
    list2 = [[0] * (len(values) + 1) for _ in range(third + 1)]

    for i in range(1, third + 1):
        for j in range(1, len(values) + 1):
            if list[i][j - 1] == 2:
                list[i][j] = 2
                continue
            if values[j - 1] == i:
                list[i][j] = 1 if list[i][j - 1] == 0 else 2
                list2[i][j] = j
                continue
            index_i = i - values[j - 1]
            flag = True
            list2_id = list2[index_i][j - 1]
            if list2_id:
                for index_j in range(1, j):
                    if list2[index_i][index_j] == list2_id:
                        if list2[i][index_j]:
                            flag = False
                            break
            if index_i > 0 and list[index_i][j - 1] > 0 and not list2[i][j - 1] and flag:
                list[i][j] = 1 if list[i][j - 1] == 0 else 2

                list2[i][j] = j
                list2[i][j - 1] = j

                verifier = values[j - 1] + values[j - 2]
                if list2_id:
                    for index_j in range(1, len(values)):
                        if list2[index_i][index_j] == list2_id:
                            list2[i][index_j] = j
                            verifier += values[index_j - 1]
                if verifier < i:
                    for index_j in range(j - 2, 0, -1):
                        if list2[i][index_j] or verifier + values[index_j - 1] > i:
                            continue
                        verifier += values[index_j - 1]
                        list2[i][index_j] = j
                        if verifier == i:
                            break
            else:
                list[i][j] = list[i][j - 1]
        if list[-1][-1] == 2:
            result = 1
        else:
            result = 0
    return result

if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))
