sheeps = [5, 7, 300, 90, 24, 75]

for month in range(5):
    print(f'after {month + 1} month, here is my sheeps size...')
    for i in range(len(sheeps)):
        sheeps[i] += 50
    print(sheeps)

    print('my sheeps after being sheared...')
    max_sheep_index = 0
    for i in range(len(sheeps)):
        if sheeps[i] > sheeps[max_sheep_index]:
            max_sheep_index = i
    sheeps[max_sheep_index] = 8
    print(sheeps)
    print()

total = 0
for i in range(len(sheeps)):
    total += sheeps[i]
print(f'after 5 months, my total sheep size is {total}')
# print(f'after 5 months, my total sheep size is {sum(sheeps)}')
print(f'i would get {total * 2}$')