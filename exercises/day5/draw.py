from turtle import *

# pic 1
# color('blue')
# speed(-1)
# for i in range(24):
#     for i in range(4):
#         forward(100)
#         left(90)
#     left(360/24)

# pic 2
color('blue')
speed(-1)
current_size = 200
n = 10
for i in range(n):
    for i in range(4):
        forward(current_size)
        left(90)
    current_size += current_size / n
    left(12)

mainloop()