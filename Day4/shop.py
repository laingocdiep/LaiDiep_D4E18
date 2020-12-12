shop = ['T-shirt']
while True:
    action = input('Welcome to our shop. What do you want? (C R U D) ')
    action = action.upper()
    if action == 'C':
        new_item = input('Enter new stuff ')
        shop.append(new_item)
        print(shop)
    elif action == 'R':
        for i in range(len(shop)):
            print(f'{i + 1}. {shop[i]}')
    elif action == 'U':
        update = int(input('Enter update position '))
        shop[update] = input('Enter new item ')
        print(shop)
    elif action == 'D':
        delete = int(input('Enter delete position '))
        shop.pop(delete)
        print(shop)
    elif action == 'EXIT':
        print('See ya <3')
        break