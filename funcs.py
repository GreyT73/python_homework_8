def show():
    with open('phonebook.csv', 'r', encoding='utf-8') as phonebook:
        count = 1
        phonebook = phonebook.read().split('\n')
        for i in phonebook:
            if len(i) != 0:
                print(f'{count}. {i}')
                count += 1