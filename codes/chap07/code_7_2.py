# 区間を (int, int) で表す
def cmp(a):
    return a[1]

def main():
    # 入力
    N = int(input())
    inter = [tuple(map(int, input().split())) for _ in range(N)]

    # 終端時刻が早い順にソートする
    inter.sort(key=cmp)

    # 貪欲に選ぶ
    res = 0
    current_end_time = 0
    for i in range(N):
        # 最後に選んだ区間と被るのは除く
        if inter[i][0] < current_end_time:
            continue

        res += 1
        current_end_time = inter[i][1]

    print(res)

if __name__ == "__main__":
    main()
