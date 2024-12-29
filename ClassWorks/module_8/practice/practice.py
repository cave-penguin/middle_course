def calc(line):
    operand1, operation, operand2 = line.split(' ')
    operand1 = int(operand1)
    operand2 = int(operand2)
    if operation == '+':
        return f"result: {operand1 + operand2}"
    if operation == '-':
        return f"result: {operand1 - operand2}"
    if operation == '*':
        return f"result: {operand1 * operand2}"
    if operation == '/':
        return f"result: {operand1 / operand2}"


cnt = 0

with open('data.txt', 'r') as file:
    for line in file:
        cnt += 1
        try:
            calc(line)
        except ValueError as exc:
            if 'unpack' in exc.args[0]:
                print(f'Ошибка в строке {cnt}, не хватает данных для ответа')
            else:
                print(f"Ошибка в строке {cnt}, нельзя перевести в число")
