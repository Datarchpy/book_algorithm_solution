# 比較して最小値を代入する関数
def chmin(a, b):
    return min(a, b)

# 1 << 29 はビットシフト演算で、1 を 29 ビット左にシフトすることで 2^29 を計算しています
INF = 1 << 29  # 十分大きな値 (ここでは 2^29 とする)

def main():
    # 入力
    S = input()
    T = input()

    # DP テーブル定義
    dp = [[INF] * (len(T) + 1) for _ in range(len(S) + 1)]

    # DP 初期条件
    dp[0][0] = 0

    # DPループ
    for i in range(len(S) + 1):
        for j in range(len(T) + 1):
            # 変更操作
            if i > 0 and j > 0:
                if S[i - 1] == T[j - 1]:
                    dp[i][j] = chmin(dp[i][j], dp[i - 1][j - 1])
                else:
                    dp[i][j] = chmin(dp[i][j], dp[i - 1][j - 1] + 1)

            # 削除操作
            if i > 0:
                dp[i][j] = chmin(dp[i][j], dp[i - 1][j] + 1)

            # 挿入操作
            if j > 0:
                dp[i][j] = chmin(dp[i][j], dp[i][j - 1] + 1)

    # 答えの出力
    print(dp[len(S)][len(T)])

if __name__ == "__main__":
    main()
