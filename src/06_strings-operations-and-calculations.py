# inmutability: something that cannot be changed
my_str = "testing"
print(my_str.capitalize())
# data is not changed in my_str
print(my_str)
print(id(my_str))
print(id("testing"))
# they have the same ID!
other_str = "testing"
print(id(my_str) == id(other_str))
# is True

# len Function
my_str = "testing"
print(len(my_str))

# string indexing and slicing
test_str = "testing"
print(test_str[0])
print(test_str[len(test_str) - 1])
print(test_str[- 1])

# slicing
test_str = "testing"
print(test_str[0:2])
print(test_str[3:5])
print(test_str[2:len(test_str)])
print(test_str[2:]) #best way
print(test_str[1:5:2]) #step by 2
print(test_str[1:6:2]) #step by 2
print(test_str[:6:2]) #step by 2
print(test_str[1::2]) #step by 2
print(test_str[::-1]) #step by 2 reverse the string