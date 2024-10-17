# 十分大きな値として INF を定義
INF = 20000000

# 入力を受け取る
N = int(input())
a = list(map(int, input().split()))

# 線形探索
min_value = INF
for i in range(N):
    if a[i] < min_value:
        min_value = a[i]

# 結果出力
print(min_value)
