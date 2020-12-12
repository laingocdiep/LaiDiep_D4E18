# container
person = ['Doris', 2002, 'free learner']

# dictionary
person = {
    'name': 'Doris',
    'yob': 2002,
    'job': 'free learner',
    12: 'you'
}

# C R U D
# C
person['say'] = 'evermore'

# R
# print(person[12])
for key in person:
    print(f'{key}: {person[key]}')
print('----------------------------')

# U
person[12] = 'Back to December'
for key in person:
    print(f'{key}: {person[key]}')
print('----------------------------')

# D
del person['yob']
for key in person:
    print(f'{key}: {person[key]}')

# for key in ['yo', True, 9, 12]:
#     print(key)

# check if key exists
# if 'job' in person:
#     print(person['job'])

