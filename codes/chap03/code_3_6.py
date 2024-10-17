# 入力を受け取る
N, W = map(int, input().split())
a = list(map(int, input().split()))

# bit は 2^N 通りの部分集合全体を動く
exist = False
for bit in range(1 << N):
    sum_ = 0  # 部分集合に含まれる要素の和
    for i in range(N):
        # i 番目の要素 a[i] が部分集合に含まれているかどうか
        if bit & (1 << i):
            sum_ += a[i]
    
    # sum が W に一致するかどうか
    if sum_ == W:
        exist = True

# 結果出力
if exist:
    print("Yes")
else:
    print("No")

