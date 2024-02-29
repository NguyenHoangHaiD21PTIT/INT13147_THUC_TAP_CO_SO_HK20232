import copy

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def s_pop(self):
        if self.is_empty():
            print("3. Pop empty stack")
            print("Error: Stack is empty")
            return -1  # or raise an exception
        return self.stack.pop()

    def top(self):
        if self.is_empty():
            print("Error: Stack is empty")
            return -1  # or raise an exception
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def print_st(self):
        for i in self.stack:
            print(i, end=" ")
        print()

    def size(self):
        return len(self.stack)

thaoTac = int(input())
if thaoTac == 3: 
    print("3. Pop empty stack")
    print("Error: Stack is empty")
else:
    n = int(input())  # Số phần tử
    a = Stack()
    a.stack = list(map(int, input().split()))

    if thaoTac == 1:
        x = int(input())
        print("1. Push {} to the top of {}-element stack: ".format(x, n), end="")
        a.print_st()
        a.push(x)
        print("Current stack: ", end="")
        a.print_st()
    elif thaoTac == 2:
        print("2. Pop the top element of {}-element stack: ".format(n), end="")
        a.print_st()
        print(a.top())
        a.s_pop()
        print("Current stack: ", end="")
        a.print_st()
    elif thaoTac == 4:
        print("4. Top of {}-element stack: ".format(n), end="")
        a.print_st()
        print(a.top())
        print("Current stack: ", end="")
        a.print_st()
    elif thaoTac == 5:
        q = int(input())  # Số loại truy vấn
        b = copy.deepcopy(a)  # Lưu trữ lại stack ban đầu
        for i in range(q):
            ques = input()
            if ques == "pop":
                a.s_pop()
            else:
                a.push(int(ques[4::]))

        print("5. After {} operations on the {}-element stack: ".format(q, n), end="")
        b.print_st()
        print("Current stack size: {}".format(a.size()))
        print("Current stack: ", end="")
        a.print_st()

    
    