import numpy as np

# Функция и её производная
def f(x):
    return x**2

def grad_f(x):
    return 2 * x

# Параметры
x = 10  # Начальная точка
learning_rate = 0.1
iterations = 100

# Градиентный спуск
for i in range(iterations):
    gradient = grad_f(x)
    x = x - learning_rate * gradient
    print(f"Итерация {i+1}: x = {x:.5f}, f(x) = {f(x):.5f}")
