# python3


def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


def majority_elementOne(elements):
    if len(elements) == 0:
        return None
    if len(elements) == 1:
        return elements[0]
    half = len(elements) // 2
    left = majority_elementOne(elements[0:half])
    right = majority_elementOne(elements[half:])
    if left == right:
        return left
    if elements.count(left) > half:
        return left
    if elements.count(right) > half:
        return right
    return None


def majority_element(elements):
    assert len(elements) <= 10 ** 5
    count = 0
    for x in elements:
        if count == 0:
            candidate = x
        if x == candidate:
            count += 1
        else:
            count -= 1
    if elements and elements.count(candidate) > len(elements) // 2:
        return 1
    return 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
