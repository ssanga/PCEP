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