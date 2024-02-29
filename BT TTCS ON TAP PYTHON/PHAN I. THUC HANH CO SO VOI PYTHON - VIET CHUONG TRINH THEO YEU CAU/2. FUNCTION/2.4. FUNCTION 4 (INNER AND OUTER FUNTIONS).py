def outer_function(num1, num2):
    def inner_function():
        return num1 + num2
    return inner_function()

x = outer_function(int(input()), int(input()))
print(x)