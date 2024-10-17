# x が条件を満たすかどうか
def P(x):
    # 条件を満たすかどうかを判定するロジックをここに書く
    pass

# P(x) = True となる最小の整数 x を返す
def binary_search(left, right):
    # P(left) = False, P(right) = True となるように
    while right - left > 1:
        mid = left + (right - left) // 2
        if P(mid):
            right = mid
        else:
            left = mid
    return right

# 使用例（P関数に適当な実装を追加する必要があります）
def main():
    left = 0  # 左の境界 (P(left) = False となる値)
    right = 100  # 右の境界 (P(right) = True となる値)
    result = binary_search(left, right)
    print(result)

if __name__ == "__main__":
    main()

