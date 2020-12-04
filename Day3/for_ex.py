# print from 1 to 20
# for i in range(1,21):
#     print(i)

# print even from 0 to 20
# for i in range(21):
#     if i % 2 == 0:
#         print(i)

# print from 20 to 1
# for i in range(20, 0, -1):
#     print(i)

# print bang cuu chuong tu 1 den 9
for i in range(1,10):
    for j in range(1,10):
        if i * j > 9:
            white_space = ' '
        else:
            white_space = '  '
        print(i * j, end=white_space)
    print()  # = print(end='\n')
