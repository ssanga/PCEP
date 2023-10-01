if 'a' < 'b':
    print("Condition was True")

if 'b' < 'a':
    print("Condition was True")

if False:
    print("Was True")
else:
    print("Was False")

if 'b' < 'a':
    print("First Condition was True")
elif 'c' < 'd':
    print("Second Condition was True")
else: 
    print("no condition was True")

name =  input("What is your name?")

if (len(name) >=6):
    print("Your name is long")
elif(len(name) >= 4):
    print("Your name is 4 or more characters")
elif(len(name) == 5): #dead branch
    print("Your name is 5 characters")
else:
    print("Your name is short")


name = "Keith"

if name == "Kevin":
    print("Hello Kevin")
else:
    pass

