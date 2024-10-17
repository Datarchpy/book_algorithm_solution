def func(N):
    # 再帰関数を呼び出したことを報告する
    print(f"func({N}) を呼び出しました")

    if N == 0:
        return 0

    # 再帰的に答えを求めて出力する
    result = N + func(N - 1)
    print(f"{N} までの和 = {result}")

    return result

# メイン関数
if __name__ == "__main__":
    func(5)

