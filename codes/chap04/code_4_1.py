def func(N):
    if N == 0:
        return 0
    return N + func(N - 1)

