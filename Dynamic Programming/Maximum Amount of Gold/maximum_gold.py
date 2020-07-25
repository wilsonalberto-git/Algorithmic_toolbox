# python3

from sys import stdin


def maximum_gold(W_capacity, w_weights):
    assert 1 <= W_capacity <= 10 ** 4
    assert 1 <= len(w_weights) <= 10 ** 3
    assert all(1 <= w <= 10 ** 5 for w in w_weights)
    elements = [0]
    for element in w_weights:
        if element <= W_capacity:
            elements.append(element)
    capacity = W_capacity + 1
    weights = [[0 for _ in range(len(elements))] for _ in range(capacity)]
    for j in range(1, len(elements)):
        for i in range(1, capacity):
            previous = weights[i][j - 1]
            current = elements[j] + weights[i - elements[j]][j - 1]
            if current > i:
                weights[i][j] = previous
            else:
                weights[i][j] = max(previous, current)
    return weights[-1][-1]


if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n
    print(maximum_gold(input_capacity, input_weights))
