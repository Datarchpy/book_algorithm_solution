class Node:
    def __init__(self, name=""):
        self.prev = None  # 前のノードへのポインタ
        self.next = None  # 次のノードへのポインタ
        self.name = name  # ノードに付随している値

# 番兵を表すノードをグローバル領域に置いておく
nil = None

# 初期化
def init():
    global nil
    nil = Node()
    nil.prev = nil
    nil.next = nil

# 連結リストを出力する
def printList():
    cur = nil.next  # 先頭から出発
    while cur != nil:
        print(f"{cur.name} -> ", end="")
        cur = cur.next
    print()

# ノード p の直後にノード v を挿入する
def insert(v, p=nil):
    v.next = p.next
    p.next.prev = v
    p.next = v
    v.prev = p

# ノード v を削除する
def erase(v):
    if v == nil:
        return  # v が番兵の場合は何もしない
    v.prev.next = v.next
    v.next.prev = v.prev
    # Pythonでは明示的にメモリを解放する必要はない

def main():
    # 初期化
    init()

    # 作りたいノードの名前の一覧
    names = ["yamamoto", "watanabe", "ito", "takahashi", "suzuki", "sato"]

    # 連結リスト作成: 各ノードを生成して連結リストの先頭に挿入していく
    watanabe = None
    for name in names:
        # ノードを作成する
        node = Node(name)

        # 作成したノードを連結リストの先頭に挿入する
        insert(node)

        # 「渡辺」ノードを保持しておく
        if name == "watanabe":
            watanabe = node

    # 「渡辺」ノードを削除する
    print("before: ", end="")
    printList()  # 削除前を出力
    erase(watanabe)
    print("after: ", end="")
    printList()  # 削除後を出力

if __name__ == "__main__":
    main()
