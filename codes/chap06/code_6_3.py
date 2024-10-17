def main():
    print("Start Game!")

    # A さんの数の候補を表す区間を、[left, right) と表す
    left, right = 20, 36

    # A さんの数を 1 つに絞れないうちは繰り返す
    while right - left > 1:
        mid = left + (right - left) // 2  # 区間の真ん中

        # mid 以上かを聞いて、回答を yes/no で受け取る
        print(f"Is the age less than {mid} ? (yes / no)")
        ans = input()

        # 回答に応じて、ありうる数の範囲を絞る
        if ans == "yes":
            right = mid
        else:
            left = mid

    # ズバリ当てる！
    print(f"The age is {left}!")

if __name__ == "__main__":
    main()

