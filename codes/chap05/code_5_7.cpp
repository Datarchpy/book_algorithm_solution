# 比較して最大値を代入する関数
def chmax(a, b):
    return max(a, b)

def main():
    # 入力
    N, W = map(int, input().split())
    weight = []
    value = []
    for _ in range(N):
        w, v = map(int, input().split())
        weight.append(w)
        value.append(v)

    # DP テーブル定義
    dp = [[0] * (W + 1) for _ in range(N + 1)]

    # DPループ
    for i in range(N):
        for w in range(W + 1):
            # i 番目の品物を選ぶ場合
            if w - weight[i] >= 0:
                dp[i + 1][w] = chmax(dp[i + 1][w], dp[i][w - weight[i]] + value[i])

            # i 番目の品物を選ばない場合
            dp[i + 1][w] = chmax(dp[i + 1][w], dp[i][w])

    # 最適値の出力
    print(dp[N][W])

if __name__ == "__main__":
    main()
