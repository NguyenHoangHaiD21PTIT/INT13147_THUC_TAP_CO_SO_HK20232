class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    #Hàm 0: Thêm node vào cây
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
    
    def createBalanceBST(self, a, start, end):
        if start > end: return None
        mid = (start + end) // 2
        node = TreeNode(a[mid])
        node.left = self.createBalanceBST(a, start, mid - 1)
        node.right = self.createBalanceBST(a, mid + 1, end)
        return node
        
n = int(input())
a = list(map(int, input().split()))
bst = BinarySearchTree()
for x in a: bst.insert(x)
print("Breadth-first traversal of the original BST:")
bst.breadth()
print()
a.sort()
bst.root = bst.createBalanceBST(a, 0, n - 1)
print("Breadth-first traversal after simple balancing:")
bst.breadth()