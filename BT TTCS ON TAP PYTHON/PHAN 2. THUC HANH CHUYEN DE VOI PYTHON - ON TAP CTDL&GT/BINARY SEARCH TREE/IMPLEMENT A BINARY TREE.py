class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    #Hàm 1: Kiểm tra cây rỗng
    def isEmpty(self): return self.root is None

    #Hàm 2: Xóa cây
    def clear(self): self.root = None

    #Hàm 3: Tìm kiếm node = x trên cây
    def search(self, x): return self._search_recursive(self.root, x)

    #Hàm 3a
    def _search_recursive(self, node, x):
        if node is None or node.key == x: return node
        if x < node.key: return self._search_recursive(node.left, x)
        return self._search_recursive(node.right, x)

    #Hàm 4: Thêm gốc vào cây
    def insert(self, x):
        if self.search(x) is None: self.root = self._insert_recursive(self.root, x)

    #Hàm 4a
    def _insert_recursive(self, node, x):
        if node is None: return TreeNode(x)
        if x < node.key: node.left = self._insert_recursive(node.left, x)
        else: node.right = self._insert_recursive(node.right, x)
        return node

    #Hàm 5: Duyệt theo mức (BFS)
    def breadth(self):
        if self.root is None: return 
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.key, end = " ")
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)

    #Hàm 6: Duyệt trước (Gốc - Trái - Phải)
    def preorder(self): self._preorder_recursive(self.root)

    #Hàm 6a
    def _preorder_recursive(self, node):
        if node == None: return 
        print(node.key, end = " ")
        self._preorder_recursive(node.left)
        self._preorder_recursive(node.right)

    #Hàm 7: Duyệt giữa (Trái - Gốc - Phải)
    def inorder(self): self._inorder_recursive(self.root)

    #Hàm 7a
    def _inorder_recursive(self, node):
        if node == None: return 
        self._inorder_recursive(node.left)
        print(node.key, end =" ")
        self._inorder_recursive(node.right)

    #Hàm 8: Duyệt sau (Trái - Phải - Gốc)
    def postorder(self): self._postorder_recursive(self.root)

    #Hàm 8a
    def _postorder_recursive(self, node):
        if node == None: return 
        self._postorder_recursive(node.left)
        self._postorder_recursive(node.right)
        print(node.key, end =" ")

    #Hàm 9a
    def count_node(self, node):
        if node == None: return 0
        return 1 + self.count_node(node.left) + self.count_node(node.right)
    
    #Hàm 9: Đếm số node
    def count(self): return self.count_node(self.root)
    
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
            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete_recursive(node.right, temp.key)
        return node

    #Hàm 10b
    def _min_value_node(self, node):
        current = node
        while current.left: current = current.left
        return current

    #Hàm 11: GTNN của cây
    def min(self):
        if self.root is None: return None
        current = self.root
        while current.left: current = current.left
        return current.key

    #Hàm 12: GTLN của cây
    def max(self):
        if self.root is None: return None
        current = self.root
        while current.right: current = current.right
        return current.key

    #Hàm 13: Tính tổng
    def sum(self): return self._sum_recursive(self.root)

    #Hàm 13a
    def _sum_recursive(self, node):
        if node is None: return 0
        return node.key + self._sum_recursive(node.left) + self._sum_recursive(node.right)

    #Hàm 14: Trung bình cộng
    def avg(self):
        nodes = self.count()
        if nodes == 0: return 0
        return self.sum() / nodes

    #Hàm 15: Độ cao của cây
    def height(self):
        return self._height_recursive(self.root)

    #Hàm 15a
    def _height_recursive(self, node):
        if node is None: return 0
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        return max(left_height, right_height) + 1

    #Hàm 16: Đường đi có tổng lớn nhất
    def max_path_cost(self): return self._max_path_cost_recursive(self.root)

    def _max_path_cost_recursive(self, node):
        if node is None: return 0
        left_cost = self._max_path_cost_recursive(node.left)
        right_cost = self._max_path_cost_recursive(node.right)
        return max(left_cost, right_cost) + node.key

    def is_avl(self):
        def _is_avl_recursive(node):
            if node is None: return True, 0
            left_balanced, left_height = _is_avl_recursive(node.left)
            right_balanced, right_height = _is_avl_recursive(node.right)
            height = max(left_height, right_height) + 1
            if not left_balanced or not right_balanced: return False, height
            if abs(left_height - right_height) > 1: return False, height
            return True, height

        balanced, _ = _is_avl_recursive(self.root)
        return balanced

q = int(input())
a = list(map(int, input().split()))
bst = BinarySearchTree()
for x in a: bst.insert(x)
if q == 5: res = bst.breadth()
elif q == 6: res = bst.preorder()
elif q == 7: bst.inorder()
elif q==8: res = bst.postorder()
elif q ==9: print(bst.count())
elif q==11: print(bst.min())
elif q==12: print(bst.max())
elif q==13: print(bst.sum())
