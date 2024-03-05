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

    #Hàm 2
    def preorder(self, node):
        if node == None: return 
        print(node.key, end = " ")
        self.preorder(node.left)
        self.preorder(node.right)
        
    #Hàm 3: Duyệt giữa
    def inorder(self, node):
        if node == None: return 
        self.inorder(node.left)
        print(node.key, end =" ")
        self.inorder(node.right)

    #Hàm 4: Duyệt sau (Trái - Phải - Gốc)
    def postorder(self, node):
        if node == None: return 
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.key, end =" ")

q, n = int(input()), int(input())
a = list(map(int, input().split()))
bst = BinarySearchTree()
for x in a: bst.insert(x)
if q == 1: 
    print("1. Test breadth-first traversal:")
    bst.breadth()
elif q == 2: 
    print("2. Test pre-order traversal:")
    bst.preorder(bst.root)
elif q == 3: 
    print("3. Test in-order traversal: ")
    bst.inorder(bst.root)
elif q==4: 
    print("4. Test post-order traversal: ")
    res = bst.postorder(bst.root)

