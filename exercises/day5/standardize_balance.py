def standardize(nums):
    num = ''
    result = ''
    # bỏ những số 0 đứng trước
    while nums[0] == '0':
        nums.pop(0)
    
    # num là số đã bỏ các số 0 ở đầu 
    for i in nums:
        num += i
    num = int(num)

    while num >= 1000:
        result = ',' + str(num % 1000) + result
        num = num // 1000
    result = str(num) + result
    return result

number = input('Enter your balance: ')
nums = list(number)
updated = standardize(nums)
print(f'Your updated balance: ${updated}')