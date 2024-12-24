class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"ФИО: {self.name}, Должность: {self.position}, Оклад: {self.salary}"


class Manager(Employee):
    def __init__(self, name, position, salary, team_size):
        super().__init__(name, position, salary)
        self.team_size = team_size

    def __str__(self):
        return f"{super().__str__()}, Размер команды: {self.team_size}"


class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def list_employees(self):
        for emp in self.employees:
            print(emp)

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for emp in self.employees:
                if isinstance(emp, Manager):
                    file.write(f"{emp.name}, {emp.position}, {emp.salary}, "
                               f"{emp.team_size}\n")
                else:
                    file.write(f"{emp.name}, {emp.position}, {emp.salary}\n")


company = Company()

while True:
    print('Добро пожаловать в программу Сотрудник 2.0')
    print('В этой программе доступны команды: \n'
          'add - добавление сотрудника\n'
          'list - вывод списка всех сотрудников\n'
          'save - сохранение списка сотрудников в отдельный файл\n'
          'exit - выход из программы')

    action = input('Выберите действие (add/list/save/exit): ')
    if action == 'add':
        emp_type = input('Введите тип сотрудника (разработчик / тимлид): ')
        name = input('Введите ФИО сотрудника: ')
        position = input('Введите должность сотрудника: ')
        salary = input('Укажите оклад сотрудника: ')

        if emp_type == 'тимлид':
            team_size = int(input('Введите кол-во команды: '))
            company.add_employee(Manager(name, position, salary, team_size))
        else:
            company.add_employee(Employee(name, position, salary))

    elif action == 'list':
        company.list_employees()

    elif action == 'save':
        filename = input('Введите имя файла для сохранения: ')
        company.save_to_file(filename)

    elif action == 'exit':
        print('Сеанс завершен!')
        break

    else:
        print('Некорректное действие! Пожалуйста, попробуйте снова.')

"""
  # Добавить сообщение после добавления сотрудника
  # Добавить сообщение после сохранения

  # Вывести сообщение, если список сотрудников на начало программы пустой
  ** Вывести список сотрудников из другого файла, если сотрудники там есть

  # Добавить возможность увольнения (удаления) сотрудника из общего файла

  # Добавить возможность дополнять список сотрудников добавляя новых (чтобы список каждый раз не обнулялся)
"""
