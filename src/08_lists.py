my_list = [1,2,3,4,5]
print(my_list)
other_list = ['a',1,1.0,False]
print(other_list)
print(my_list[0])
print(my_list[2])
print(len(my_list))
print(my_list[0:2])
print(my_list[1:])
print(my_list[:3])
print(my_list[0::1])
print(my_list[0::2])

# list are mutable, we can modify them
my_list[0] = 'a'
print(my_list)
print(my_list + [8,9,10])
print(my_list)
my_list += [8,9,10]
print(my_list)

my_list[1:3] = ['b', 'c']
print(my_list)
my_list[3:5] = ['d', 'e', 'f']
print(my_list)
my_list = ['a','b','c','d',5,6,7]
print(my_list)
my_list[4:] = []
print(my_list)
del my_list[0]
print(my_list)

# functions and methods
my_list = [1,2,3]
my_list.append(4)
print(my_list)
my_list.insert(0, 'a')
print(my_list)
print(my_list.index(3))
print(4 in my_list)
print(4 not in my_list)
my_list = [1, 3, 4, 8, 2]
print(sorted(my_list))
print(reversed(my_list))
print(list(reversed(my_list)))
print(list(reversed(sorted(my_list))))

# nested list: matrices and cubes
'''
1 2 3
4 5 6
'''

my_matrix = [[1, 2, 3],
            [4, 5, 6]]
print(my_matrix)
row_count = len(my_matrix)
print(row_count)
column_count = len(my_matrix[0])
print(column_count)
print(my_matrix[0][1])
print(my_matrix[1][1])
