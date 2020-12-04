a = 10
b = 20
# print("a > b:", a > b)
# print("a < b:", a < b)
# print("a = b:", a == b)
# if a > b:
#     print("a is greater than b")
# else:
#     print("No no no")

# sex = input("What is your sex?")
# if sex == 'female':
#     print("Hi sis <3")
# elif sex == 'male':
#     print("Hey bro!")
# else:
#     print("We're proud of you")


# BMI
# weight = float(input("What is your weight in kg?"))
# height = float(input("What is your height in cm?"))
# bmi = round((weight / ((height / 100) ** 2)), 2) 
# print(f'Your BMI is {str(bmi)}')
# if bmi < 18.5:
#     print("You're thin")
# elif bmi < 25:
#     print("Excellent")
# else:
#     print("You should exercise to lose weight")

# equation ax^2 + bx + c = 0
a = float(input("Enter a"))
b = float(input("Enter b"))
c = float(input("Enter c"))
delta = b**2 - 4*a*c
x1 = (-b - delta**0.5) / (2*a)
x2 = (-b + delta**0.5) / (2*a)
if delta < 0:
    print("No solution")
elif delta == 0:
    print(f'Phương trình có nghiệm kép: {str(x1)}')
else:
    print(f'Phương trình có 2 nghiệm: {str(x1)} và {str(x2)}')

