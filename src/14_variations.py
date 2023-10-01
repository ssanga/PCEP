#!/usr/bin/env python 3.7

# Python implementation here

message = input("Enter a message:")
print("Lowercase: ", message.lower())
print("Uppercase: ", message.upper())
print("Capitalized: ", message.capitalize())

words = message.split() # default splits by space
print("Words:", words)

sorted_words = sorted(words)
print("Alphabetic First Word", sorted_words[0])
print("Alphabetic Last Word", sorted_words[-1])