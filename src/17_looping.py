# while 1 < 2:
#     print("something")

count = 1
while count <= 4:
    print("looping")
    count += 1

colors = ['blue', 'green', 'red', 'purple']
for color in colors:
    print(color)

point = (1, 2, 3)
for value in point:
    print(value)

ages = {'Kevin': 59, 'Bob': 40}
for key in ages:
    print(key)

for key, value in ages.items():
    print(key, value)

for letter in 'my_string':
    print(letter)

counter = 1
while counter <= 25:
    if counter % 4 == 0:
        print(counter)
    counter += 1

count = 0
while count <= 10:
    if count % 2 == 0:
        count += 1
        continue
    print(f"We are counting odd numbers: {count}")
    count += 1
print("_____")
count = 1
while count < 10:
    if count % 2 == 0:
        break
    print(f"We are counting odd numbers: {count}")
    count += 1

colors = ['blue', 'green', 'red', 'purple']
for color in colors:
    if color == 'blue':
        continue
    elif color == 'red':
        break
    print(color)

count = 1
while count <= 4:
    print(count)
    count += 1
else:
    print("While loop completed")

for i in [1,2,3,4,5]:
    print(i)
else:
    print("For loop completed")

colors = ['blue', 'green', 'red', 'purple']
for color in colors:
    if color == 'green':
        print("Orange is in the list")
        break
else:
    print("Orange is not in the list")

# range
my_range = range(10)
print(list(range(1,14,2)))

for _ in range(4):
    print("looping")

# list comprehensions
colors = ['red', 'blue', 'orange', 'green', 'yellow']
uppercase_colors = []

for color in colors:
    uppercase_colors.append(color.upper())

print(uppercase_colors)

uppercase_colors = []
uppercase_colors = [color.upper() for color in colors]
print(uppercase_colors)

warm_colors = []
warm_colors_colors = [color.upper() for color in colors if color in ['red', 'orange', 'yellow']]
print(warm_colors_colors)
