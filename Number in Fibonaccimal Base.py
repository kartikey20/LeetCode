from itertools import combinations


def generate_fibonacci_sequence(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence


def fibonaccimal(n):
    sequence = generate_fibonacci_sequence(n)
    possible_sums = []
    target = n

    def all_subsequences(arr):
        res = set()
        for i in range(1, len(arr) + 1):
            for comb in combinations(arr, i):
                res.add(comb)
        return res

    for x in all_subsequences(sequence[2:]):
        if sum(x) == target:
            possible_sums.append(x)

    res = []
    for x in possible_sums:
        string = ''
        till_index = sequence.index(max(x))
        for i in sequence[2:till_index+1][::-1]:
            if i in x:
                string += '1'
            else:
                string += '0'
        res.append(int(string))
    return res


print(fibonaccimal(13))
