# still serious exercises
# ex1
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
# Add a key to inventory called 'pocket'; Set the value of 'pocket' to be a list consisting of the strings 'seashell',
# 'strange berry', and 'lint'.
inventory['pocket'] = ['seashell', 'strange berry', 'lint']

# Then remove 'dagger' from the list of items stored under the 'backpack' key.
inventory['backpack'].pop(1)

# Add 50 to the number stored under the 'gold' key.
inventory['gold'] += 50

print('-----------------------------------------')

# ex2
# without count()
nums = [1,2,3,1,9,5,7,8,2,4,1,0,3,7,4,5,2,2,9]
def count_number(nums):
    count = {}
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    return count
result = count_number(nums)
# key = int(input('Enter a number: '))
# if key in result:
#     print(f'{key} appears {result[key]} times in my list')
# else:
#     print(f"{key} doesn't appear in my list")

# with count()
# times = nums.count(key)
# print(f'{key} appears {times} times in my list')

# ex3
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
total_money = 0
# for fruit in prices:
#     total_money += prices[fruit] * stock[fruit]
#     print(f'''{fruit}:
#     price: {prices[fruit]}
#     stock: {stock[fruit]}
#     ''')
# print(f"You would make {total_money} if you sold all of your food")

# serious exercises
# ex2
def standardise(nums):
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
updated = standardise(nums)
print(f'Your updated balance: ${updated}')
