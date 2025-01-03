# import torch
# import torch.nn as nn
# 
# x = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.float32)
# y = torch.tensor([[0], [1], [1], [0]], dtype=torch.float32)
# 
# 
# class XORNet(nn.Module):
#     def __init__(self):
#         super(XORNet, self).__init__()
#         self.hidden = nn.Linear(2, 2)  # Скрытый слой: 2 входа -> 2 нейрона
#         self.output = nn.Linear(2, 1)  # Выходной слой: 2 нейрона -> 1 выход
#         self.activation_hidden = nn.Sigmoid()  # Активация скрытого слоя
#         self.activation_output = nn.Sigmoid()  # Активация выходного слоя
# 
#     def forward(self, x):
#         x = self.activation_hidden(
#             self.hidden(x))  # Пропускаем через скрытый слой
#         x = self.activation_output(
#             self.output(x))  # Пропускаем через выходной слой
#         return x
# 
# 
# # Создаём модель
# model = XORNet()
# 
# # Используем BCELoss для бинарной классификации
# criterion = nn.BCELoss()  # Binary Cross Entropy Loss
# # optimizer = optim.SGD(model.parameters(), lr=0.1)
# optimizer = torch.optim.Adam(model.parameters(), lr=0.1)
# 
# for epoch in range(3000):
#     optimizer.zero_grad()
#     outputs = model(x)
#     loss = criterion(outputs, y)
#     loss.backward()
#     optimizer.step()
# 
#     if epoch % 100 == 0:
#         print(f"Эпоха {epoch}, Потеря: {loss.item():.4f}")
# 
# # Тестируем сеть
# with torch.no_grad():  # Отключаем градиенты для тестирования
#     for i in range(len(x)):
#         output = model(x[i]).item()
#         print(f"Вход: {x[i].tolist()}, Выход: {round(output)}")

import torch

# Данные
X = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.float32)
y = torch.tensor([[0], [1], [1], [0]], dtype=torch.float32)

# Параметры
input_size = 2
hidden_size = 4
output_size = 1
learning_rate = 0.1

# Инициализация весов и смещений
w1 = torch.randn(input_size, hidden_size, requires_grad=True)
b1 = torch.randn(hidden_size, requires_grad=True)
w2 = torch.randn(hidden_size, output_size, requires_grad=True)
b2 = torch.randn(output_size, requires_grad=True)

# Сигмоидная функция активации
def sigmoid(x):
    return 1 / (1 + torch.exp(-x))

# Цикл обучения
for epoch in range(10000):
    # Forward pass
    hidden_layer = sigmoid(torch.mm(X, w1) + b1)
    outputs = sigmoid(torch.mm(hidden_layer, w2) + b2)

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

    # Обнуляем градиенты
    w1.grad.zero_()
    b1.grad.zero_()
    w2.grad.zero_()
    b2.grad.zero_()

    if (epoch+1) % 100 == 0:
        print(f'Epoch [{epoch+1}/1000], Loss: {loss.item():.4f}')

# Проверка модели
with torch.no_grad():
    predicted = sigmoid(torch.mm(X, w1) + b1)
    predicted = sigmoid(torch.mm(predicted, w2) + b2)
    predicted = (predicted > 0.5).float()
    print('Predicted:', predicted)
    print('Actual:', y)