def fibo(N):
    print(f"fibo({N}) を呼び出しました")

    # ベースケース
    if N == 0:
        return 0
    elif N == 1:
        return 1

    # 再帰的に答えを求めて出力する
    result = fibo(N - 1) + fibo(N - 2)
    print(f"{N} 項目 = {result}")

    return result

# メイン関数
if __name__ == "__main__":
    fibo(6)

