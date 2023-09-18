# unary and bitwise operators
a = 0b010
print(a)
print(bin(a))
# ALT + 126
print(~a)
# mismo resultado que la linea anterior con la tilde de la ñ
print(-a - 1)

print(bin(~a))

a = 0b1001
b = 0b1100
print(bin(a | b )) #OR
print(bin(a & b )) #AND
print(bin(a ^ b )) #XOR

a = 0b110
print(bin(a >> 2))
print(bin(a >> 4))
print(bin(a << 2))

# Boolean Operators
print(not True)
print(not False)
print(True or True)
print(True or False)
print(False or False)
print(False or True)

print(True and True)
print(True and False)
print(False and False)
print(False and True)

# Comparision Operators
print(1 < 2)
print(2 > 1)
print(2 < 1)
print(1 <= 1)
print(2.0 >= 3)
print(2.0 >= 2)
print('a' > 'b')
print('b' > 'a') #True
print('bb' >= 'ba') #True
print('a' <= 'c') #True
print(ord('a'))
print(ord('b'))
print(ord('c'))

# esto no se puede
# print('a' <= 1)

print(1 == 1)
print('a' == 1)
print(1 != 2)

print(1 is 1)
print(1 is 1.0) #False
print('a' is 'a')
print('a' is not 'a')
print(id('a'))
print([] is []) #False

# Operator priority



