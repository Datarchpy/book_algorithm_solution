# メイン処理
if __name__ == "__main__":
    F = [0] * 50  # 長さ50のリストを初期化
    F[0], F[1] = 0, 1
    for N in range(2, 50):
        F[N] = F[N - 1] + F[N - 2]
        print(f"{N} 項目: {F[N]}")

