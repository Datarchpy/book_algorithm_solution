# こちらのC++コードをPythonに書き換えると、次のようになります。
# Pythonではメモリ管理は自動で行われるため、new や delete などは必要ありません。

class Node:
    def __init__(self, name=""):
        self.next = None  # 次がどのノードを指すか
        self.name = name  # ノードに付随している値

# 番兵を表すノードをグローバル領域に置いておく
nil = None

# 初期化
def init():
    global nil
    nil = Node()
    nil.next = nil  # 初期状態では nil が nil を指すようにする

# 連結リストを出力する
def printList():
    cur = nil.next  # 先頭から出発
    while cur != nil:
        print(f"{cur.name} -> ", end="")
        cur = cur.next
    print()

# ノード p の直後にノード v を挿入する
# ノード p のデフォルト引数を nil としておく
# そのため insert(v) を呼び出す操作は，リストの先頭への挿入を表す
def insert(v, p=nil):
    v.next = p.next
    p.next = v

def main():
    # 初期化
    init()

    # 作りたいノードの名前の一覧
    names = ["yamamoto", "watanabe", "ito", "takahashi", "suzuki", "sato"]

    # 各ノードを生成して，連結リストの先頭に挿入していく
    for i in range(len(names)):
        # ノードを作成する
        node = Node(names[i])

        # 作成したノードを連結リストの先頭に挿入する
        insert(node)

        # 各ステップの連結リストの様子を出力する
        print(f"step {i}: ", end="")
        printList()

if __name__ == "__main__":
    main()

