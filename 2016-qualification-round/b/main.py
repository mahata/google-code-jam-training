#!/usr/bin/env python3


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


input()  # Discard first input
case_count = 1
while True:
    try:
        N, K = [int(x) for x in input().split(" ")]
        input_data = [
            [int(x) for x in input().split(" ")],
            [int(x) for x in input().split(" ")],
            [int(x) for x in input().split(" ")],
            [int(x) for x in input().split(" ")]]

        combinations = create_combinations(N)
        count = len([True for combination in combinations if is_xor_value_ok(K, combination, input_data)])
        print("Case #{}: {}".format(case_count, count))
        case_count += 1

    except EOFError:
        break
