import os.path


class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        all_products = ''
        if not os.path.exists(self.__file_name):
            with open(self.__file_name, 'w', encoding='utf-8') as file:
                file.write('')
        with open(self.__file_name, 'r') as file:
            for product in file.readlines():
                all_products += f"{product}"
        return all_products

    def add(self, *products):
        all_products = self.get_products()
        for product in products:
            if product.name in all_products:
                print(f"Продукт {product.name} уже есть в магазине")
            else:
                with open(self.__file_name, 'a') as file:
                    file.write(f"{product.name}, {product.weight}, "
                               f"{product.category}\n")


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__
s1.add(p1, p2, p3)
print(s1.get_products())
