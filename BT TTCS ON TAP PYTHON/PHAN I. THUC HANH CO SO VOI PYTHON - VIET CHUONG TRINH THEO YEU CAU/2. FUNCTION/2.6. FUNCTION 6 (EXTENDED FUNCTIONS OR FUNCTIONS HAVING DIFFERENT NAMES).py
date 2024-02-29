def chia(x, y):
    if y==0: 
        print("Cannot divide by 0.")
        print("None")
        return 
    print(x/y)


x, y = int(input()), int(input())
chia(x, y)