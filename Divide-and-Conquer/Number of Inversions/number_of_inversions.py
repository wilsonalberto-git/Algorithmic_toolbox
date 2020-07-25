# python3

import sys
from itertools import combinations

def compute_inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions

def merge(elements, b, left, mid, right):
    num_inv = 0
    i, j, k = left, mid, left
    while i <= mid - 1 and j <= right:
        if elements[i] <= elements[j]:
            b[k] = elements[i]
            i += 1
        else:
            b[k] = elements[j]
            j += 1
            num_inv += mid - i
        k += 1
    while i <= mid - 1:
        b[k] = elements[i]
        i += 1
        k += 1
    while j <= right:
        b[k] = elements[j]
        j += 1
        k += 1
    for i in range(left, right + 1):
        elements[i] = b[i]
    return num_inv

def merge_sort(elements, b, left, right):
    num_inv = 0
    if right > left:
        mid = (left + right) // 2
        num_inv += merge_sort(elements, b, left, mid)
        num_inv += merge_sort(elements, b, mid + 1, right)
        num_inv += merge(elements, b, left, mid + 1, right)
    return num_inv

if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    #assert len(elements) == input_n
    #print(compute_inversions(elements))
    #input = sys.stdin.read()
    #n, *a = list(map(int, input.split()))
    #b = n * [0]
    b = [i * 0 for i in elements]
    print(merge_sort(elements, b, 0, len(elements) - 1))
