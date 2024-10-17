N = 8
a = [3, 5, 8, 10, 14, 17, 21, 39]

# 目的の値 key の添字を返す (存在しない場合は -1)
def binary_search(key):
    left, right = 0, len(a) - 1  # 配列 a の左端と右端
    while right >= left:
        mid = left + (right - left) // 2  # 区間の真ん中
        if a[mid] == key:
            return mid
        elif a[mid] > key:
            right = mid - 1
        else:
            left = mid + 1
    return -1

def main():
    print(binary_search(10))  # 3
    print(binary_search(3))   # 0
    print(binary_search(39))  # 7

    print(binary_search(-100))  # -1
    print(binary_search(9))     # -1
    print(binary_search(100))   # -1

if __name__ == "__main__":
    main()

