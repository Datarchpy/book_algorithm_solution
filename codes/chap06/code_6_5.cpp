def main():
    # 入力
    N = int(input())
    H = []
    S = []
    for _ in range(N):
        h, s = map(int, input().split())
        H.append(h)
        S.append(s)

    # 二分探索の上限値を求める
    M = 0
    for i in range(N):
        M = max(M, H[i] + S[i] * N)

    # 二分探索
    left, right = 0, M
    while right - left > 1:
        mid = (left + right) // 2

        # 判定する
        ok = True
        t = [0] * N  # 各風船を割るまでの制限時間
        for i in range(N):
            # そもそも mid が初期高度より低かったら False
            if mid < H[i]:
                ok = False
            else:
                t[i] = (mid - H[i]) // S[i]

        # 時間制限がさし迫っている順にソート
        t.sort()
        for i in range(N):
            # 時間切れ発生の場合は False
            if t[i] < i:
                ok = False

        if ok:
            right = mid
        else:
            left = mid

    print(right)

if __name__ == "__main__":
    main()
