val = 1 or '2'
val *= 3
print(val)

names = ['Alice', 'Bob', 'Lance', 'Mike']
names[2] = 'Jimmy'
print(names)

names = ['Alice', 'Bob', 'Lance', 'Mike']
names.insert(2, 'Jimmy')
print(names)

def double_values(list1):
    doubles = []
    for num in list1:
        doubles.append(str(num * 2))
    return doubles

first_list = [1, 2, 3, 4]
print(" ".join(double_values(first_list)))

ages = {'Keith': 30, 'Levi': 25, 'John': 20}
age = ages.get('Kevin')
print(age)

# def fib(n):
#     a, b = 0, 1
#     for _ in range(1, n):
#         a, b = b, a + b
#         yield a
# fib_gen = fib()
# print(fib_gen)

print (3 ** 3)

def double_values(list1):
    doubles = []
    for num in list1:
        doubles.append(num * 2)

first_list = [1, 2, 3, 4]
print(double_values(first_list))

names = ['Alice', 'Bob', 'Lance', 'Mike']
names.remove('Bob')
print(names)

names = ['Alice', 'Bob', 'Lance', 'Mike']
names[1:2] = []
print (names)

for num in range(10):
    print(num)
    if num % 2 == 0:
        continue
    else:
        break

for num in range(1, 10, 2):
    # print(num)
    if num % 3:
        print(num)