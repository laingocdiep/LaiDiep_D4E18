dic = {
    'sv': 'seven',
    'hx': 'hoax',
    'sio': 'shake it off',
    'fl': 'folklore',
    'bs': 'blank space'
}
run = True
while run:
    for key in dic:
        print(key, end='\t')
    print()
    user_key = input('your code? ')
    if user_key in dic:
        print(f'trans: {dic[user_key]}')
        print('--------------------------')
    else:
        ask = input('Not found! Do you want to contribute this word? (y/n): ').lower()
        if ask == 'y':
            dic[user_key] = input('Enter its trans: ')
            print('updated')
            print('--------------------------')
            run = True
        elif ask == 'n':
            print('see you later')
            break
    


