# 入力を受け取る
N, v = map(int, input().split())
a = list(map(int, input().split()))

# 線形探索
found_id = -1  # 初期値は -1 などありえない値に
for i in range(N):
    if a[i] == v:
        found_id = i  # 見つかったら添字を記録
        break  # ループを抜ける

# 結果出力 (-1 のときは見つからなかったことを表す)
print(found_id)
