from creation import create_name, create_surname, create_phone, create_company
from funcs import show

while True:
    action = input("Что вы хотите сделать:\n"
                   "1. Посмотреть справочник\n"
                   "2. Внести изменения\n"
                   "3. добавить запись\n"
                   "4. Удалить запись\n"
                   "5. Выйти\n"
                   ">")
    match action:
        case "1":
            show()
        case "2":
            show()
            number_to_change = int(input("Запись под каким номером нужно изменить?"))
            new_phonebook = []
            with open('phonebook.csv', 'r', encoding='utf-8') as phonebook:
                phonebook = phonebook.read().split('\n')
                for i in range(len(phonebook)):
                    if i + 1 != number_to_change and len(phonebook[i]) != 0:
                        new_phonebook.extend([phonebook[i],'\n'])
                    elif len(phonebook[i]) == 0:
                        continue
                    else:
                        new = phonebook[i].split()
                        thing_to_change = input("Что вы хотите поменять: \n"
                                                    "1. Имя\n"
                                                    "2. Фамилию\n"
                                                    "3. Телефон\n"
                                                    "4. Компанию\n"
                                                    ">").lower()
                        if thing_to_change == '1' or thing_to_change == "имя":
                            new[0] = create_name()
                        elif thing_to_change == '2' or thing_to_change == "фамилия":
                            new[1] = create_surname()
                        elif thing_to_change == '3' or thing_to_change == "телефон":
                            new[2] = create_phone()
                        elif thing_to_change == '4' or thing_to_change == "компанию":
                            new[3] = create_company()
                        else:
                            print("Изменений внесено не будет")

                        new = ' '.join(new)
                        new_phonebook.extend([new, '\n'])
            with open('phonebook.csv', 'w', encoding='utf-8') as phonebook:
                for i in new_phonebook:
                    phonebook.write(i)

        case "3":
            with open('phonebook.csv', 'a', encoding='utf-8') as phonebook:
                phonebook.write(f'{create_name()} {create_surname()} {create_phone()} {create_company()}\n')
        case "4":
            find = input("Напишите имя того, кого нужно удалить удалить?: ")
            new_phonebook = []
            with open('phonebook.csv', 'r', encoding='utf-8') as phonebook:
                for i in phonebook:
                    if find not in i:
                        new_phonebook.append(i)
            with open('phonebook.csv', 'w', encoding='utf-8') as phonebook:
                for i in new_phonebook:
                    phonebook.write(i)
        case "5":
            break
        case _:
            print("Вы ввели неверное значение\n")
