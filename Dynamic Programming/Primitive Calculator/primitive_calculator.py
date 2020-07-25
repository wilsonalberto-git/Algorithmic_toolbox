# python3
import sys

def compute_operations(n):
    assert 1 <= n <= 10 ** 6
    hop_count = [0] * (n + 1)

    hop_count[1] = 1
    for i in range(2, n + 1):
        indices = [i - 1]
        if i % 2 == 0:
            indices.append(i // 2)
        if i % 3 == 0:
            indices.append(i // 3)

        min_hops = min([hop_count[x] for x in indices])

        hop_count[i] = min_hops + 1
    ptr = n
    optimal_seq = [ptr]
    while ptr != 1:

        candidates = [ptr - 1]
        if ptr % 2 == 0:
            candidates.append(ptr // 2)
        if ptr % 3 == 0:
            candidates.append(ptr // 3)
        ptr = min(
            [(c, hop_count[c]) for c in candidates],
            key=lambda x: x[1]
        )[0]
        optimal_seq.append(ptr)
    optimal_seq.reverse()

    return optimal_seq


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    reversed(output_sequence)
    print(len(output_sequence) - 1)
    #print(*reversed(output_sequence))
    print(*output_sequence)
