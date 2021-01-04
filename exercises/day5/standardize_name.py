string = input('Enter a name: ')

# result = string.title()

# strip() bo dau cach o 2 dau
# capitalize() viet hoa chu cai dau cua tu do
def standardize_name(string):
    string = string.lower().strip()
    list_string = string.split(' ')
    result = ''
    for i in range(len(list_string)):
        if list_string[i] != '':
            list_string[i] = list_string[i].capitalize()
            result += list_string[i] + ' '
    return result
full_name = standardize_name(string)
print(full_name)