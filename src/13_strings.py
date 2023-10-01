print(ord('a'))
print('\u2122')
print(chr(8482))

# useful String methods
my_str = "This is an example"
print(my_str.lower())
print(my_str.upper())
print(my_str.capitalize())
print(my_str.title())
print(my_str.isascii())
print(my_str.islower())
print(my_str.isupper())
print(my_str.istitle())
print(" ".isspace())
print("1.0".isdecimal())
print("1".isdecimal())
print("1".isdigit())
print("1".isnumeric())
print("1.0".isnumeric()) # no lo detecta
print("asdasda".isalpha())
print("1bear".isidentifier()) #False
print("Class".isidentifier()) #False
print("This is printable\n".isprintable())

phrase = "This is a simple phrase"
words = phrase.split()
print(words)
url = "https://example.com/users/jimmy"
user = url.split('/')[-1]
print(user)

print(", ".join(words))
lines = ["First line", "Second line", "Third Line"]
output = '\n'.join(lines)
print(output)

# format
str_example = "Hello, my name is {} and I really enjoy {}, Have a nice day!"
print(str_example.format('Santi', 'Python'))

