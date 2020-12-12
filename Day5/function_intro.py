# def = define function
def welcome(name, talker='Taylor'):
    print(f"Hi {name}~ It's {talker}. I just want to welcome you to my house <3")
    something = talker
    return something    # đưa biến something ra khỏi function

st = welcome('Doris', 'Taylor')
print(st)
# call function
welcome('Doris')
welcome('Doris', 'Alec')

