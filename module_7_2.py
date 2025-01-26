from pprint import pprint
# Создайте функцию custom_write(file_name, strings), которая принимает аргументы file_name - название файла для записи,
# strings - список строк для записи.
def custom_write(file_name, strings):
    strings_positions = {}
# Записывать в файл file_name все строки из списка strings, каждая на новой строке.
    with open(file_name, 'w', encoding='utf-8') as file:
# Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>), а значением -
# записываемая строка. Для получения номера байта начала строки используйте метод tell() перед записью.
        for i, string in enumerate(strings, 1):
            position = file.tell()
            file.write(string + '\n')
            strings_positions[(i, position)] = string
        return strings_positions

info = ['Text for tell.','Используйте кодировку utf-8.','Because there are 2 languages!','Спасибо!']
result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)






