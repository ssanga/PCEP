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

    
# Ver con ChatGPT
values = ['Kevin Bacon', 60, '555-555-5555', False]
val = not values[1] #False
val = not values[-1] #True
print(val)

# num = input("Enter a float value: ")
# new_num = num // 100
# print(new_num)

t = ("sandy", "mandy", "candy", "andy")

print(sorted(t))

Z = 19 % 4 + 15 / 2 * 3
print(19 % 4)
print(Z)

others = 0
for i in range(2):
    for j in range(2):
        if i != j:
            others += 1
else:
    others +=1
print(others)

list_one = [1,2]
list_two = list_one
list_two.append(3)
print(list_one[-1])

train_speed = {"AAA" : 201, "TGV": 320, "Shinkasen": 320}
for train in train_speed:
    print(train[0], end="")

power = 1
while power < 5:
    power += 1
    print("@", end="")
    if power == 3:
        break
else:
    print("@")

torque = 5
while torque > 0:
    torque -= 3
    print("*", end="")
else:
    print("*")

def process(data):
    data = [1,2,3]
    return data[-2]

measurements = [0 for i in range(3)]
print(measurements)
process(measurements)
print(measurements[-2])