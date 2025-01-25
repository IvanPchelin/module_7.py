from pprint import pprint
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category
# Метод __str__, который возвращает строку в формате '<название>, <вес>, <категория>'. Все данные
# в строке разделены запятой с пробелами.
    def __str__(self):
        return(f'{self.name}, {self.weight}, {self.category}')


class Shop(Product):
# Инкапсулированный атрибут __file_name = 'products.txt'.
    def __init__(self, name, weight, category, __file_name='products.txt'):
        super().__init__(name, weight, category)
        self.__file_name = __file_name
# Метод get_products(self), который считывает всю информацию из файла __file_name, закрывает его и возвращает
# единую строку со всеми товарами из файла __file_name.
    def get_products(self):
        file = open(self.__file_name, 'r')
        st = file.read()
        file.close()
        print(f'{st}')
# Метод add(self, *products), который принимает неограниченное количество объектов класса Product. Добавляет в
# файл __file_name каждый продукт из products, если его ещё нет в файле (по названию). Если такой продукт уже есть,
# то не добавляет и выводит строку 'Продукт <название> уже есть в магазине' .
    def add(self, *products):
        for i in products:
            s = (str(i))
            file = open(self.__file_name, 'r')
            f = file.read()
            file.close()
            if s in f:
                print(f'Продукт {s} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.write(f'\n{s}')
                file.close()

s1 = Shop('',0 , '')
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
#
print(p2)  # __str__
s1.add(p1, p2, p3)
print(s1.get_products())
s1.get_products()
