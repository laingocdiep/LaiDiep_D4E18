# ex1
# year = int(input("Nhập năm muốn kiểm tra"))
# if year % 4 == 0:
#     conclude = "là năm nhuận"
#     days_year = 366
# else:
#     conclude = "không phải năm nhuận"
#     days_year = 365
# print("Năm", year, conclude, ", có", days_year, "ngày")

# ex2
# month = int(input("Nhập tháng muốn kiểm tra"))
# if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
#     days_month = 31
# elif month == 4 or month == 6 or month == 9 or month == 11:
#     days_month = 30
# elif month == 2:
#     if conclude == "là năm nhuận":
#         days_month = 29
#     else:
#         days_month = 28
# if month == 2:
#     print("Tháng 2 năm", year, "có", days_month, "ngày")
# else:
#     print("Tháng", month, "có", days_month, "ngày")

# ex3
# if month == 1 or month == 2 or month == 3:
#     season = "mùa xuân"
# elif month == 4 or month == 5 or month == 6:
#     season = "mùa hạ"
# elif month == 7 or month == 8 or month == 9:
#     season = "mùa thu"
# else:
#     season = "mùa đông"
# print("Tháng", month, "là", season)

# ex4
# a = int(input("Nhập số nguyên a"))
# b = int(input("Nhập số nguyên b"))
# c = int(input("Nhập số nguyên c"))
# nums = [a, b, c]
# print(*sorted(nums))

# ex5
a = int(input("Nhập số nguyên a"))
b = int(input("Nhập số nguyên b"))
c = int(input("Nhập số nguyên c"))
if a + b > c and b + c > a and a + c > b:
    nums = sorted([a, b, c])
    if nums[0] == nums[1]:
        if nums[1] == nums[2]:
            triangle = "đều"
        elif nums[0]**2 + nums[1]**2 == nums[2]**2:
            triangle = "vuông cân"
        else:
            triangle = "cân"
    else:
        if nums[0]**2 + nums[1]**2 == nums[2]**2:
            triangle = "vuông"
        else:
            triangle = "thường"
    print("Có thể lập thành tam giác", triangle)
else:
    print("Không thể lập thành tam giác")