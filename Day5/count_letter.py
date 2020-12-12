def count_letter(sentence):
    count = {}
    for char in sentence:
        if char != ' ':
            if char not in count:
                count[char] = 1
            else:
                count[char] += 1
    return count

sentence = input('Enter a sentence: ')
result = count_letter(sentence.lower())

for key in result:
    print(f'{key}: {result[key]}')
