#!/usr/bin/env python3

N = 2  # candidates for each position
K = 3  # target value

input_data = [[0, 0], [2, 0], [0, 0], [0, 1]]


def create_combinations(N):
    llst = [[]]
    for i in range(4):
        tmp_llst = llst[:]
        llst = []
        for j in range(N):
            for lst in tmp_llst:
                llst.append(lst + [j])

    return llst


def is_xor_value_ok(K, combination, input_data):
    import functools

    values = [value[combination[idx]] for idx, value in enumerate(input_data)]
    if functools.reduce(lambda a, b: a ^ b, values) == K:
        return True
    else:
        return False


combinations = create_combinations(N)
print([True for combination in combinations if is_xor_value_ok(K, combination, input_data)])
