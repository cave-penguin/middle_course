class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out =False

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            return f"Книга {self.title} успешно взята"
        else:
            return f"Книга {self.title} уже кем-то взята"

    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            return f"Книга {self.title} вернулась в библиотеку!"
        else:
            return f"Книга {self.title} не была взята"

    def get_info(self):
        status = "Книга доступна" if not self.is_checked_out else "Книга взята"
        return f"Название: {self.title}, Автор: {self.author}, Статус: {status}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        return f"Книга {book.title} добавлена в библиотеку"

    def show_books(self):
        if not self.books:
            return "В библиотеке пусто"
        return '\n'.join(book.get_info() for book in self.books)

library = Library()
book1 = Book('Гарри Поттер', "Джоан Роулинг")
book2 = Book('Мастер и Маргарита', "Михаил Булгаков")
book3 = Book('Преступление и наказание', "Фёдор Достоевский")

print(library.add_book(book1))
print(library.add_book(book2))
print(library.add_book(book3))

print('--' * 15)

print(library.show_books())

print('--' * 15)

print(book1.check_out())
print(book1.get_info())

print('--' * 15)

print(book1.return_book())
print(book1.get_info())
