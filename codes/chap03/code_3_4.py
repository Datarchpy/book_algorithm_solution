# 十分大きな値として INF を定義
INF = 20000000

# 入力を受け取る
N, K = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 線形探索
min_value = INF
for i in range(N):
    for j in range(N):
        # 和が K 未満の場合はスキップ
        if a[i] + b[j] < K:
            continue

        # 最小値を更新
        if a[i] + b[j] < min_value:
            min_value = a[i] + b[j]

# 結果出力
print(min_value)

