class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    #Hàm 0: Thêm gốc vào cây
    def insert(self, x):
        self.root = self._insert_recursive(self.root, x)

    #Hàm 0a
    def _insert_recursive(self, node, x):
        if node is None: return TreeNode(x)
        if x < node.key: node.left = self._insert_recursive(node.left, x)
        else: node.right = self._insert_recursive(node.right, x)
        return node

    #Hàm 1: Duyệt theo mức (BFS)
    def breadth(self):
        if self.root is None: return 
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.key, end = " ")
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
    
    #Hàm 10: Xóa node x trên cây
    def dele(self, x): 
        self.root = self._delete_recursive(self.root, x)

    #Hàm 10a
    def _delete_recursive(self, node, x):
        if node is None: return node
        if x < node.key: node.left = self._delete_recursive(node.left, x)
        elif x > node.key: node.right = self._delete_recursive(node.right, x)
        else:
            if node.left is None: return node.right
            elif node.right is None: return node.left
            #Lấy node phải nhất của cây con bên trái có root là node cần xóa
            temp = self._max_value_node(node.left)
            node.key = temp.key
            #Tiến hành xóa node tmp của cây con bên phải có root là node cần xóa
            node.left = self._delete_recursive(node.left, temp.key)
        return node

    #Hàm 10b
    def _max_value_node(self, node):
        current = node
        while current.right: current = current.right
        return current

n = int(input())
a = list(map(int, input().split()))
bst = BinarySearchTree()
for x in a: bst.insert(x)
x1 = int(input())
print("Breadth-first traversal of the original BST:")
bst.breadth()
print()
print("Breadth-first traversal after deleting node {}:".format(x1))
bst.dele(x1)
bst.breadth()
