def generate_dict(file_path): 
    elvees_dict = {} # Создаем словарик
    with open(file_path, 'r', encoding='utf-8') as file: # открываем файл
        for line in file: # считываем построчно
            words = line.strip().split()  # Разделение строки по пробелам
            for word in words: 
                key = words[0] # Ключ - первое слово
                value = ' '.join(words[1:]) # Значение - оставшаяся часть строки
                if key and value:
                    elvees_dict[key] = value # добавление в словарь
    return elvees_dict

def main():
    input_file = 'test.txt'  # Тестовый файлик
    name_count_dict = generate_dict(input_file) # Создаем словарик, заполняем его в функции

    for key, value in name_count_dict.items(): # Вывод словарика
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
