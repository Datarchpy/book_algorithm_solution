# 比較して最小値を代入する関数
def chmin(a, b):
    return min(a, b)

INF = 1 << 60  # 十分大きな値 (ここでは 2^60 とする)

def main():
    # 入力
    N = int(input())
    c = [list(map(int, input().split())) for _ in range(N + 1)]

    # DP テーブル定義
    dp = [INF] * (N + 1)

    # DP 初期条件
    dp[0] = 0

    # DPループ
    for i in range(N + 1):
        for j in range(i):
            dp[i] = chmin(dp[i], dp[j] + c[j][i])

    # 答えの出力
    print(dp[N])

if __name__ == "__main__":
    main()
