def main():
    # 入力
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    # 答え
    sum_ = 0
    for i in range(N - 1, -1, -1):
        A[i] += sum_  # 前回までの操作回数を足す
        amari = A[i] % B[i]
        D = 0
        if amari != 0:
            D = B[i] - amari
        sum_ += D

    print(sum_)

if __name__ == "__main__":
    main()
