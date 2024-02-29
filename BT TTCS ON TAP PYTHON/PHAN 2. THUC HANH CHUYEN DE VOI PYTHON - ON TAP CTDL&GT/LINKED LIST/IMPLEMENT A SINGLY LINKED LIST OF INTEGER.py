class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def makeNode(x):
    return Node(x)

#Hàm 1
def addToHead(a, x):
    tmp = makeNode(x)
    if a is None: a = tmp
    else:
        tmp.next = a
        a = tmp
    return a

#Hàm 2
def addToTail(a, x):
    tmp = makeNode(x)
    if a is None: a = tmp
    else:
        p = a
        while p.next: p = p.next
        p.next = tmp
    return a

#Hàm 3
def addAfter(a, p, x):
    new_node = Node(x)
    # Tìm phần tử có giá trị bằng p
    current = head
    while current:
        if current.data == p:
            # Chèn phần tử mới vào sau phần tử có giá trị p
            new_node.next = current.next
            current.next = new_node
            break
        current = current.next
    return head

#Hàm 4 và Hàm 14
def traverse(a):
    while a:
        print(a.data, end = " ")
        a = a.next
    print()

#Phần tử x thay cho phần tử ở vị trí pos
def insertAtPosition(a, x, pos):
    if pos == 1: return addToHead(a, x)
    else:
        n = count(a)
        if n == pos - 1: return addToTail(a, x)
        else:
            p = a
            for i in range(1, pos - 1): p = p.next
            tmp = makeNode(x)
            tmp.next = p.next
            p.next = tmp
    return a

#Hàm 5
def deleteFromHead(a):
    if a: a = a.next
    return a

#Hàm 6
def deleteFromTail(a):
    if a:
        if not a.next: a = None
        else:
            prev = None
            current = a
            while current.next:
                prev = current
                current = current.next
            prev.next = None
    return a

#Hàm 7
def deleteAfter(a, p): 
    current = head
    while current.next:
        if current.data == p:
            # Xóa node sau phần tử có giá trị p nếu có
            if current.next: current.next = current.next.next
            break
        current = current.next
    
    return head

#Hàm 8, Hàm 13
def delete(a, x): 
    pos = findPos(a, x)
    if pos == 1:
        return deleteFromHead(a)
    else:
        return deleteAtPosition(a, pos)

# Hàm 9 - Vị trí đầu tiên phần tử bằng x 
def findPos(a, x):
    cnt = 0
    while a:
        cnt += 1
        if a.data == x:
            return cnt
        a = a.next
    return -1  # Không tìm thấy

#Hàm 10: Đếm số phần tử trong DSLK
def count(a):
    cnt = 0
    while a:
        cnt += 1
        a = a.next
    return cnt

#Hàm 11: Xóa phần tử ở chính xác 1 vị trí cho trước
def deleteAtPosition(a, pos):
    if pos == 1:
        return deleteFromHead(a)
    else:
        current = a
        for i in range(pos - 1):
            prev = current
            current = current.next
        prev.next = current.next
    return a

#Hàm 12, 15: Sắp xếp theo thứ tự tăng dần
def sapXep(a):
    current = a
    while current:
        next_node = current.next
        while next_node:
            if current.data > next_node.data:
                current.data, next_node.data = next_node.data, current.data
            next_node = next_node.next
        current = current.next
    return a

#Hàm 16
def addBefore(a, p, x):
    pos = findPos(a, p)
    insertAtPosition(a, x, pos)
    return a

#Hàm 17: Nối 2 DSLK đơn
def appendLinkedList(head1, head2):
    # Tìm nút cuối cùng của danh sách thứ nhất
    current = head1
    while current.next is not None: current = current.next
    # Nối danh sách thứ hai vào cuối danh sách thứ nhất
    current.next = head2
    return head1  # Trả về danh sách thứ nhất đã được nối   

#Hàm 18: Tìm GTLN trong DSLK đơn
def maxVal(a):
    res = -1
    while a:
        res = max(res, a.data)
        a = a.next
    return res

#Hàm 19: Tìm GTNN trong DSLK đơn
def minVal(a):
    res = 10**9
    while a:
        res = min(res, a.data)
        a = a.next
    return res

#Hàm 20: Tính tổng tất cả các phần tử trong DSLK
def calSum(a):
    sum = 0
    while a:
        sum+=a.data
        a = a.next
    return sum 

#Hàm 21: Tính trung bình cộng toàn bộ DSLK
def calAvg(a):
    return calSum(a)/count(a)

#Hàm 22: Check DSLK đã SX chưa
def isNonDecreasing(head):
    current = head
    while current and current.next:
        if current.data > current.next.data: return "false"
        current = current.next
    return "true"

#Hàm 23: Chèn số x vào DSLK sao cho vẫn bảo đảm tính SX
def insert(head, x):
    new_node = Node(x)
    
    # Nếu danh sách rỗng hoặc giá trị của nút đầu tiên lớn hơn x
    # thì chèn nút mới vào đầu danh sách và trả về nút mới làm nút đầu
    if not head or head.data > x:
        new_node.next = head
        return new_node
    
    current = head
    
    # Duyệt qua danh sách đến khi tìm được vị trí thích hợp để chèn nút mới
    while current.next and current.next.data < x:
        current = current.next
    
    # Chèn nút mới vào giữa danh sách
    new_node.next = current.next
    current.next = new_node
    
    return head

#Hàm 24: Duyệt DSLK ngược
def reverseTraversal(head):
    if head is None: return
    reverseTraversal(head.next)
    print(head.data, end=" ")

#Hàm 25: Kiểm tra xem 2 DSLK giống nhau không
def areListsEqual(list1, list2):
    ptr1 = list1
    ptr2 = list2

    while ptr1 is not None and ptr2 is not None:
        if ptr1.data != ptr2.data:
            return "no"
        ptr1 = ptr1.next
        ptr2 = ptr2.next

    # Đảm bảo cả hai danh sách kết thúc cùng một lúc
    # Nếu một trong hai danh sách còn phần tử và một danh sách kết thúc
    if ptr1 is not None or ptr2 is not None:
        return "no"

    return "yes"

if __name__ == "__main__":
    head = None
    input()
    q = int(input())
    n = int(input()) #Số phần tử mảng
    arr = list(map(int, input().split()))
    for p1 in arr: head = addToTail(head, p1)
    if q == 1: #Thêm vào đầu
        x = int(input())
        head = addToHead(head, x)
        print("1. Add {} before the head of {}-element list:".format(x, n), end = " ")
        for p in arr: print(p, end = " ")
        print()
        traverse(head)
    elif q==2: #Thêm vào đuôi
        x = int(input())
        head = addToTail(head, x)
        print("2. Add {} after the tail of {}-element list:".format(x, n), end = " ")
        for p in arr: print(p, end = " ")
        print()
        traverse(head)
    elif q==3: #Thêm vào sau vị trí đầu tiên phần tử có giá trị cho trước
        p, x = map(int, input().split())
        print("3. Insert an element {} after the element {} in the {}-element list". format(x, p, n), end = " ")
        traverse(head)
        head = addAfter(head, p, x)
        traverse(head)
    elif q==4: #Duyệt DSLK
        print("4. Traverse the {}-element list:". format(n), end = " ")
        traverse(head)
        traverse(head)
    elif q==5: #Xóa đầu
        print("5. Delete the head of the {}-element list:". format(n), end = " ")
        traverse(head)
        head = deleteFromHead(head)
        traverse(head)
    elif q==6: #Xóa đuôi
        print("6. Delete the tail of the {}-element list:". format(n), end = " ")
        traverse(head)
        head = deleteFromTail(head)
        traverse(head)
    elif q==7: #Xóa sau vị trí phần tử đầu tiên cho trước
        x = int(input())
        print("7. Delete the element after the element {} of the {}-element list:". format(x, n), end = " ")
        traverse(head)
        head = deleteAfter(head, x)
        traverse(head)
    elif q==8: #Xóa phần tử đầu tiên bằng giá trị cho trước
        x = int(input())
        print("8. Delete the element {} in the {}-element list:". format(x, n), end = " ")
        traverse(head)
        head = delete(head, x)
        traverse(head)
    elif q==9: #Xác định xem 1 phần tử cho trước trong list không
        x = int(input())
        print("9. Search the element {} in the {}-element list:". format(x, n), end = " ")
        traverse(head)
        x1 = findPos(head, x)
        if x1!=-1: print(x)
    elif q==10: #Đếm số phần tử trong 1 DSLK
        print("10. Count the number of the elements of the {}-element list:".format(n), end = " ")
        traverse(head)
        print(count(head))
    elif q==11: #Xóa chính xác tại 1 vị trí nào đó
        x = int(input())
        print("11. Delete the {}rd element in the {}-node list:". format(x, n), end = " ")
        traverse(head)
        head = deleteAtPosition(head, x)
        traverse(head)
    elif q==12:
        print("12. Sort in accending order the {}-node list:".format(n), end = " ")
        traverse(head)
        head = sapXep(head)
        traverse(head)
    elif q==13:
        x = int(input())
        print("13. Delete the element {} in the {}-node list:".format(x, n), end = " ")
        traverse(head)
        head = delete(head, x)
        traverse(head)
    elif q==14:
        print("14. create and return array containing info of all nodes in the {}-node list.".format(n))
        traverse(head)
    elif q==15:
        n1 = int(input()) #Số phần tử mảng
        arr1 = list(map(int, input().split()))
        for p1 in arr1: head = addToTail(head, p1)
        print("15. Merge two ordered circular singly linked lists of integers into one ordered list: {}-node list =".format(n), end = " ")
        for i in range(len(arr) - 1): print(arr[i], end = " ")
        print(arr[-1], end = "; ")
        print("{}-node list: ".format(n1), end = "")
        for x in arr1: print(x, end = " ")
        head = sapXep(head)
        print()
        traverse(head)
    elif q==16:
        x, p = map(int, input().split())
        print("16. add a node with value {} before the node {} in the {}-node list:". format(x, p, n), end = " ")
        for l in range(len(arr)-1): print(arr[l], end = " ")
        print(arr[-1], end ="."); print()
        head = addBefore(head, p, x)
        traverse(head)
    elif q==17:
        head1 = None
        n1 = int(input()) #Số phần tử mảng
        arr1 = list(map(int, input().split()))
        for p1 in arr1: head1 = addToTail(head1, p1)
        print("17. Attach a circular singly linked list of {} elements ".format(n1), end = "")
        for x in arr1: print(x, end = " ")
        print("to the end of another circular singly linked list of {} nodes: ".format(n), end = "")
        for x in arr: print(x, end = " ")
        print()
        head3 = appendLinkedList(head, head1)
        traverse(head3)
    elif q==18:
        print("18. find and return the maximum value in the {}-node list:".format(n), end = " ")
        traverse(head)
        print(maxVal(head))
    elif q==19:
        print("19. find and return the minimum value in the {}-node list:".format(n), end = " ")
        traverse(head)
        print(minVal(head))
    elif q==20:
        print("20. return the sum of all values in the {}-node list:".format(n), end = " ")
        traverse(head)
        print(calSum(head))
    elif q==21:
        print("21. return the average of all values in the {}-node list:".format(n), end = " ")
        traverse(head)
        print("{:.2f}".format(calAvg(head)))
    elif q==22:
        print("22. check and return true if the {}-node list ".format(n), end = "")
        for i in arr: print(i, end = " ")
        print("is sorted, return false if the list is not sorted.")
        print(isNonDecreasing(head))
    elif q ==23:
        x = int(input())
        print("23. sort the {}-node list:".format(n), end = " ")
        for i in arr: print(i, end = " ")
        print("then insert a node with value {} into the sorted list so that the new list is a sorted list".format(x))
        head = sapXep(head)
        traverse(head)
        head = insert(head, x)
        traverse(head)
    elif q == 24:
        print("24. Reverse the circular singly linked list of {} nodes: ".format(n), end = "")
        for i in arr: print(i, end = " ")
        print()
        reverseTraversal(head)
    elif q == 25:
        head1 = None
        n1 = int(input()) #Số phần tử mảng
        arr1 = list(map(int, input().split()))
        for p1 in arr1: head1 = addToTail(head1, p1)
        print("25. Check whether two circular singly linked list have the same contents: 1st list of {} elements:".format(n), end = " ")
        for i in range(len(arr) - 1): print(arr[i], end = " ")
        print(arr[-1], end ="; ")
        print("2nd list of {} elements: ".format(n1))
        for x in arr1: print(x, end = " ")
        print()
        head = sapXep(head)
        head1 = sapXep(head1)
        print(areListsEqual(head, head1))