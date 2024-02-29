#Chuyển số thành chữ
def changeNumtoChar(x):
    return chr(x + 65) 

#Nhập ma trận
a = []
n = int(input())
for i in range (n): 
    b = list(map(int, input().split()))
    a.append(b)
v = int(input())

#Thuật toán tìm chu trình Ơ le
#Bước 1: Khởi tạo
st = [v] #stack rỗng mới có đỉnh v 
ce = [] #Chu trình ơ le

#Bước 2: Lặp
while st: #Khi stack chưa rỗng
    x = st[-1] #Đỉnh stack
    p = -1 #Đỉnh kề với x đầu tiên còn lại
    for i in range(n):
        if a[x][i]:
            p = i
            break 
    if p!=-1: #Còn đỉnh kề
        st.append(p) 
        a[x][p] = a[p][x] = 0 
    else: #Hết đỉnh kề
        st.pop()
        ce.append(x)


#Bước 3: Lật ngược vector CE ra đáp án
for i in range(len(ce) - 1): print(changeNumtoChar(ce[i]), end = " -> ")
print(changeNumtoChar(ce[-1]))
