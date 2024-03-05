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
    
    def rotate_left(self, node):
        if node is None or node.right is None:
            return node
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        return new_root
    
    def rotate_right(self, node):
        if node is None or node.left is None:
            return node
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        return new_root    
    
n = int(input())
a = list(map(int, input().split()))
q = int(input())
bst = BinarySearchTree()
for x in a: bst.insert(x)
print("Breadth-first traversal of the original BST:")
bst.breadth()
print()
if q == 1:
    print("Breadth-first traversal after rotation to right around the root:")
    bst.root = bst.rotate_right(bst.root)
    bst.breadth()
else:
    print("Breadth-first traversal after rotation to left around the root:")
    bst.root = bst.rotate_left(bst.root)
    bst.breadth()