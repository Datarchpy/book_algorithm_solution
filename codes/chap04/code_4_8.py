# fibo(N) の答えをメモ化するリスト
memo = [-1] * 50  # 長さ50のリストを-1で初期化

def fibo(N):
    # ベースケース
    if N == 0:
        return 0
    elif N == 1:
        return 1

    # メモをチェック (すでに計算済みならば答えをリターンする)
    if memo[N] != -1:
        return memo[N]

    # 答えをメモ化しながら，再帰呼び出し
    memo[N] = fibo(N - 1) + fibo(N - 2)
    return memo[N]

# メイン処理
if __name__ == "__main__":
    # fibo(49) を呼び出す
    fibo(49)

    # memo[0], ..., memo[49] に答えが格納されている
    for N in range(2, 50):
        print(f"{N} 項目: {memo[N]}")

