import math

# 2点 (x1, y1) と (x2, y2) との距離を求める関数
def calc_dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# 入力データを受け取る
N = int(input())
x = []
y = []
for _ in range(N):
    xi, yi = map(float, input().split())
    x.append(xi)
    y.append(yi)

# 求める値を、十分大きい値で初期化しておく
minimum_dist = 100000000.0

# 探索開始
for i in range(N):
    for j in range(i + 1, N):
        # (x[i], y[i]) と (x[j], y[j]) との距離
        dist_i_j = calc_dist(x[i], y[i], x[j], y[j])
        
        # 暫定最小値 minimum_dist を dist_i_j と比べる
        if dist_i_j < minimum_dist:
            minimum_dist = dist_i_j

# 答えを出力する
print(minimum_dist)
