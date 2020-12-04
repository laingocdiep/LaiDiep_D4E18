import math
# ex1
# x = float(input("Enter a number"))
# y1 = 4 * (x**2 + 10*x**3/2 + 3*x + 1)
# y2 = (math.sin(math.pi * x**2) + math.sqrt(x**2 + 1)) / (math.e**(2*x) + math.cos(x * math.pi/4))
# print("y1 =", y1)
# print("y2 =", y2)

# ex2
# money = int(input("Nhập số tiền bạn muốn đổi (là bội số của 10,000đ)"))
# dong100k = money // 100000
# dong50k = money % 100000 // 50000
# du1 = money - dong50k * 50000 - dong100k * 100000
# dong20k = du1 // 20000
# dong10k = du1 % 20000 // 10000
# print(money, "đổi được", dong100k, "đồng 100k,", dong50k, "đồng 50k,", dong20k, "đồng 20k và", dong10k, "đồng 10k")

# ex3
# num = int(input("Nhập 1 số có 3 chữ số"))
# sum = (num // 100) + (num % 100 // 10) + (num % 10)
# print("Tổng các chữ số của", num, "là", sum)