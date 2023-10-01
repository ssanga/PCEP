y = 5

def set_x(z):
    # print("Inner y:", y)
    global y
    global a
    
    x = z
    y = x
    a = 7

# if 1 < 2:
#     x = 5
print("y before set_x", y)
set_x(10)
# print("Outer y:", y)
print("y after set_x", y)
print("a after set_x", a)
# while x < 6: 
#     print(x)
#     x += 1

# print(x)
# conditional and loops dont have its own scope