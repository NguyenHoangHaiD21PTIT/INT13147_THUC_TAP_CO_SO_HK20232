s = input()
if s[0]=="-":
    if s[1::].isdigit(): print("Error: negative number")
    else: print("Error: not a number")
else:
    if not s.isdigit(): print("Error: not a number")
    else: 
        x = int(s)
        print(str(bin(x))[2::]) 
        tong = 0
        for x in s: tong+=int(x)
        print(tong)
        print(int(s[::-1]))
    
    