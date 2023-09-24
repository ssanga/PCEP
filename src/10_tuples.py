point = (2.0, 3.0)
print(point)
# tuple is an inmutable type

point_3d = point + (4.0,) # need to add a comma to indicate that is a tuple
print(point_3d)
x, y, z = point_3d
print(x)
print(y)
print(z)

# tuples vs lists
# use list when you are not sure if the items are going to increase
person = ('Kevin Bacon', 61, "555-555-5555")
person2 = ('Bob Ross', 76, "")
print(person[0])
print(person2[0])

# combining tuples and lists
my_list = [1, 2, 3]
my_tuple = (my_list, 1)
print (my_tuple)
other_list = [1, 2, my_tuple]
print(other_list)