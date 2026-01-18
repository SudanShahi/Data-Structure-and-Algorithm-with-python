text = input()
chars = list(text)
for i in range(len(chars)):
    for j in range(i+1, len(chars)):
        if chars[i] > chars[j]:
           temp = chars[i]
           chars[i] =chars[j]
           chars[j] = temp
result =""
for c in chars:
    result = result + c
    
print(result)


#Arthmetic
a = int(input())
b = int(input())
#for sum
print(str(a) + " + " + str(b) + " is " + str(a + b))
# for difference
print(str(a) + " - " + str(b) + " is " + str(a - b))
#for multiplication
print(str(a) + " * " + str(b) + " is " + str(a * b))
#for divison
print(str(a) + " / " + str(b) + " is " + str(a / b))
#for percentage
print(str(a) + " % " + str(b) + " is " + str(a % b))
#for reminder
print(str(a) + " ^ " + str(b) + " is "+ str(a ** b))

#Squares
n = int(input())

square_dict = {}
for i in range(1, n + 1):
    square_dict[i] = i * i

print(square_dict)    

#Sum of the first n Positive integers
n = int(input())
result = n * (n + 1) // 2
print("The sum of the first " + str(n) + " positive integers is " + str(result))


#Count vowels
s = input()
s = s.lower()
vowels = "aeiou"
count = 0

for ch in s:
    if ch in vowels:
        count = count + 1

print("Number of vowels: " + str(count))


#Sum of collectio of numbers
total = 0.0
while True:
    user_input = input()
    try:
        number = float(user_input)
        if number == 0:
            break
        total += number
        print(f"The total is now {total}")
    except ValueError:
        print("That wasn’t a number.")
print(f"The grand total is {total}")

#Custom encoder
def custom_encoder(text):
    reference_string = 'abcdefghijklmnopqrstuvwxyz'
    positions = []
    for char in text:
        char = char.lower()
        if char in reference_string:
            positions.append(reference_string.index(char))
        else:
            positions.append(-1)
    return positions


#Class person
class Person:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print(f"Hello, my name is {self.name}")



#Restaurant
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.name} serves wonderful {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.name} is open. Come on in!")


#user
class User:
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location
    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")
    def greet_user(self):
        print(f"Welcome back {self.username}!")




#Write function to combine two lists
def combine_lists(list1, list2):
    combined = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined