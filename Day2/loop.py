a = range(10)
# # unpack: use *
# print(*a)
# print(a)
# print(*range(20, 0, -1))
# print(*range(0, 11, 2))

# for i in range(6):
#     print(i)
# for i in range(6, -1, -1):
#     print(i)
for _ in range(3):
    # print("Hi guys")
    print("Hi guys", end=' <3 ')
    # print("Hi guys", end='\t')

# tính tổng từ 1 đến n
# n = int(input("Enter an integer"))
# sum1 = 0
# for i in range(n + 1):
#     sum1 = sum1 + i
# print("Sum =", sum1)
# tính tổng nghịch đảo từ 1 đến n
# sum2 = 0
# if n > 0:
#     for i in range(1, n + 1):
#         sum2 = sum2 + 1/i
#     print("Sum =", sum2)
# else:
#     print("Please input an integer that is greater than 0")

i = 0
while i <= 10:
    i += 1
    if i % 2 != 0:
        continue
    print(i)

# quickly loop
print("Hi guys " * 3)