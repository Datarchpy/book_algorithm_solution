import sys

# 比較して最小値を代入する関数
def chmin(a, b):
    return min(a, b)

# 十分大きい値として INF を定義
INF = sys.maxsize

# 入力データと，メモ用の DP テーブル
N = 0
h = []
dp = []

def rec(i):
    # DP の値が更新されていたらそのままリターン
    if dp[i] < INF:
        return dp[i]

    # ベースケース: 足場 0 のコストは 0
    if i == 0:
        return 0

    # 答えを表す変数を INF で初期化する
    res = INF

    # 足場 i - 1 から来た場合
    res = chmin(res, rec(i - 1) + abs(h[i] - h[i - 1]))

    # 足場 i - 2 から来た場合
    if i > 1:
        res = chmin(res, rec(i - 2) + abs(h[i] - h[i - 2]))

    # 結果をメモしながら、返す
    dp[i] = res
    return dp[i]

def main():
    global N, h, dp
    # 入力受け取り
    N = int(input())
    h = list(map(int, input().split()))

    # 初期化 (最小化問題なので INF に初期化)
    dp = [INF] * N

    # 答え
    print(rec(N - 1))

if __name__ == "__main__":
    main()
