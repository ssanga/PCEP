def print_something(something):
    print(something)

print_something("prueba")

def print_name(name):
    print(f"Name is {name}")

print_name("Santi")

def add_two(num):
    return num + 2

result = add_two(2)
print(result)

def add(num1, num2):
    return num1 + num2

result = add(3,4)
print(result)

def contact_card(name, age, car_model):
    return f"{name} is {age} and drives a {car_model}"

print(contact_card("Santi",44, "Toyota Verso"))
print(contact_card(name= "Santi", age=44, car_model="Toyota Verso"))

def can_drive(age, driving_age=16):
    return age >= driving_age

print(can_drive(29))

# recursion en fichero aparte