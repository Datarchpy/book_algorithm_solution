import sys

# 比較して最小値を代入する関数
def chmin(a, b):
    return min(a, b)

# 十分大きい値として INF を定義
INF = sys.maxsize

def main():
    # 入力
    N = int(input())
    h = list(map(int, input().split()))

    # 初期化 (最小化問題なので INF に初期化)
    dp = [INF] * N

    # 初期条件
    dp[0] = 0

    # ループ
    for i in range(1, N):
        dp[i] = chmin(dp[i], dp[i - 1] + abs(h[i] - h[i - 1]))
        if i > 1:
            dp[i] = chmin(dp[i], dp[i - 2] + abs(h[i] - h[i - 2]))

    # 答え
    print(dp[N - 1])

if __name__ == "__main__":
    main()

