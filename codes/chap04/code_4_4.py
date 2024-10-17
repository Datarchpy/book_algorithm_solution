def GCD(m, n):
    # ベースケース
    if n == 0:
        return m

    # 再帰呼び出し
    return GCD(n, m % n)

# メイン関数
if __name__ == "__main__":
    print(GCD(51, 15))  # 3 が出力される
    print(GCD(15, 51))  # 3 が出力される

