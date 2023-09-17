#!/usr/bin/env python3.7 

# This is a full line comment. This is free, does not create string
# Python does not have block comments, you have to put # individually

print("Hello, World!") # this is a trailing comment

"""
This is not a block comment
This is a multiline string.
This is not free, this create strings in the interpreter
"""

# variables
my_str = "This is a simple string"
print(my_str)
my_str = "This is a different string"
print(my_str)
my_str += " testing"
print(my_str)
my_str = my_str + " testing"
print(my_str)
my_str = 1
print(my_str)

# string and string operators
my_str = 'simple quoted string'
my_str = "double quoted string"
my_str = '''
this is a triple quoted 
multi-line string
'''
print(my_str)
my_str = "pass" + "word"
print(my_str)
my_str = "Ha" * 4
print(my_str)
my_str = "my_string"
print(my_str.find("t"))

my_str = "TeStInG"
print(my_str.lower())

my_str = "Tab\tDelimited"
print(my_str)

my_str = "New\nLine"
print(my_str)

# escape \n
my_str = "New\\nLine"
print(my_str)

my_str = "'Single' in Double"
print(my_str)

my_str = '"Double" in Single'
print(my_str)

my_str = "\"Double\" in Double"
print(my_str)

# booleans
value = True
value = False
print(value)

# Numbers
print (2 + 2)
print (2.0 + 2.0)
print(4.5e9)
print(4.5e9 == 4.5 * (10 ** 9))
print(4.5e-2)