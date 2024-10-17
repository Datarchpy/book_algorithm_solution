import bisect

INF = 20000000  # 十分大きな値に

def main():
    # 入力を受け取る
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # 暫定最小値を格納する変数
    min_value = INF

    # b をソート
    b.sort()

    # b に無限大を表す値 (INF) を追加しておく
    b.append(INF)

    # a を固定して解く
    for i in range(N):
        # b の中で K - a[i] 以上の範囲での最小値を示すイテレータ
        idx = bisect.bisect_left(b, K - a[i])

        # イテレータの示す値を取り出す
        val = b[idx]

        # min_value と比較する
        if a[i] + val < min_value:
            min_value = a[i] + val

    print(min_value)

if __name__ == "__main__":
    main()
