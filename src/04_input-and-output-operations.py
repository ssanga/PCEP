# typecasting
print(float(1))
print(int(1.3)) #truncate
print(str(1.0))
print(str(False))
print(float('1.2'))
print(bool(1))
print(bool(0))
print(bool(0.0))
print(bool('Pepe'))
print(bool(''))

# input
name = input("What is you name? ")
color = input("Favorite Color: ")
age = int(input("How old are you? "))

# print
print(name)
print("is " + str(age) + " years old")
print("and loves the color " + color + ".")

print(name, end=" ")
print("is " + str(age) + " years old", end=" ")
print("and loves the color " + color + ".", end=" ")

print(name, 'is', age, 'years old and loves the color', color + '.')
