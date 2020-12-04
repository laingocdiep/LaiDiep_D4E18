import math
name = "Doris"
age = 17
# print(name, "is only", age)
age = age + 5
# print("After 5 years,", name, "is", age)
height = 1.6
# print(height)
# print(height / 2)

# print("10 % 2 =", 10 % 2)
# print("10 ^ 2 =", 10**2)
# or print(pow(10,2))

# multi-lined string
numbers = '''1
    2
3
    4
5
    6
7
    8
9
    10'''
# print(numbers)
# message = f'This is our first lesson:\n {numbers}'
# print(message)
# print(f'My name is {name}')

# so ki tu cua chuoi
# print(len(numbers))
# print(len("hi\n"))   = 3

a = "10"
b = "3.0"
add = int(a) + float(b)
# print(add)


int_var = 10
float_var = 12.1
str_var =  "a string"
# print(type(int_var))
# print(type(float_var))
# print(type(str_var))

# name = input("Can I have your name?")
# print(f'Hello {name}! Welcome to my heart <3')
# msg = "I like the number " + str(13)
# print(msg)
# num = (input("So what is your favorite number?"))
# print(f'{num} is an interesting number')
# print(type(num))

# age = input("How old are you?")
# print(f'I guess you were born in {2020 - int(age)}')


# area and peremiter of circle
r = float(input("Enter the radius"))
area = r * r * math.pi
pere = 2 * r * math.pi
print(f'Area = {str(round(area, 2))} and peremeter = {str(round(pere,2))}')