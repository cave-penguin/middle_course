# import torch
# import torch.nn as nn
# import torch.optim as optim

# # Данные
# X = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.float32)
# y = torch.tensor([[0], [1], [1], [0]], dtype=torch.float32)
#
# # Параметры
# input_size = 2
# hidden_size1 = 4
# hidden_size2 = 4
# output_size = 1
# learning_rate = 0.1
#
# # Модель с двумя скрытыми слоями
# model = nn.Sequential(
#     nn.Linear(input_size, hidden_size1),
#     nn.Sigmoid(),
#     nn.Linear(hidden_size1, hidden_size2),
#     nn.Sigmoid(),
#     nn.Linear(hidden_size2, output_size),
#     nn.Sigmoid()
# )
#
# # Критерий ошибки и оптимизатор
# criterion = nn.MSELoss()
# optimizer = optim.SGD(model.parameters(), lr=learning_rate)
#
# # Цикл обучения
# num_epochs = 1000
# for epoch in range(num_epochs):
#     # Прямое распространение
#     outputs = model(X)
#     loss = criterion(outputs, y)
#
#     # Обратное распространение и оптимизация
#     optimizer.zero_grad()
#     loss.backward()
#     optimizer.step()
#
#     if (epoch+1) % 100 == 0:
#         print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')
#
# # Проверка модели
# with torch.no_grad():
#     predicted = model(X)
#     predicted = (predicted > 0.5).float()
#     print('Predicted:', predicted)
#     print('Actual:', y)


import torch

# Данные
X = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.float32)
y = torch.tensor([[0], [1], [1], [0]], dtype=torch.float32)

# Параметры
input_size = 2
hidden_size1 = 4
hidden_size2 = 4
output_size = 1
learning_rate = 0.1

# Инициализация весов и смещений
w1 = torch.randn(input_size, hidden_size1, requires_grad=True)
b1 = torch.randn(hidden_size1, requires_grad=True)
w2 = torch.randn(hidden_size1, hidden_size2, requires_grad=True)
b2 = torch.randn(hidden_size2, requires_grad=True)
w3 = torch.randn(hidden_size2, output_size, requires_grad=True)
b3 = torch.randn(output_size, requires_grad=True)

# Сигмоидная функция активации
def sigmoid(x):
    return 1 / (1 + torch.exp(-x))

# Цикл обучения
for epoch in range(1000):
    # Прямое распространение
    hidden_layer1 = sigmoid(torch.mm(X, w1) + b1)
    hidden_layer2 = sigmoid(torch.mm(hidden_layer1, w2) + b2)
    outputs = sigmoid(torch.mm(hidden_layer2, w3) + b3)

    # Вычисление ошибки (MSE)
    loss = torch.mean((outputs - y) ** 2)

    # Обратное распространение ошибки
    loss.backward()

    # Обновление весов
    with torch.no_grad():
        w1 -= learning_rate * w1.grad
        b1 -= learning_rate * b1.grad
        w2 -= learning_rate * w2.grad
        b2 -= learning_rate * b2.grad
        w3 -= learning_rate * w3.grad
        b3 -= learning_rate * b3.grad

    # Обнуляем градиенты
    w1.grad.zero_()
    b1.grad.zero_()
    w2.grad.zero_()
    b2.grad.zero_()
    w3.grad.zero_()
    b3.grad.zero_()

    if (epoch+1) % 100 == 0:
        print(f'Epoch [{epoch+1}/1000], Loss: {loss.item():.4f}')

# Проверка модели
with torch.no_grad():
    hidden_layer1 = sigmoid(torch.mm(X, w1) + b1)
    hidden_layer2 = sigmoid(torch.mm(hidden_layer1, w2) + b2)
    predicted = sigmoid(torch.mm(hidden_layer2, w3) + b3)
    predicted = (predicted > 0.5).float()
    print('Predicted:', predicted)
    print('Actual:', y)