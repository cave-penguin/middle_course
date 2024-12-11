import torch
import torch.nn as nn

x = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.float32)
y = torch.tensor([[0], [1], [1], [0]], dtype=torch.float32)


class XORNet(nn.Module):
    def __init__(self):
        super(XORNet, self).__init__()
        self.hidden = nn.Linear(2, 2)  # Скрытый слой: 2 входа -> 2 нейрона
        self.output = nn.Linear(2, 1)  # Выходной слой: 2 нейрона -> 1 выход
        self.activation_hidden = nn.Sigmoid()  # Активация скрытого слоя
        self.activation_output = nn.Sigmoid()  # Активация выходного слоя

    def forward(self, x):
        x = self.activation_hidden(
            self.hidden(x))  # Пропускаем через скрытый слой
        x = self.activation_output(
            self.output(x))  # Пропускаем через выходной слой
        return x


# Создаём модель
model = XORNet()

# Используем BCELoss для бинарной классификации
criterion = nn.BCELoss()  # Binary Cross Entropy Loss
# optimizer = optim.SGD(model.parameters(), lr=0.1)
optimizer = torch.optim.Adam(model.parameters(), lr=0.1)

for epoch in range(3000):
    optimizer.zero_grad()
    outputs = model(x)
    loss = criterion(outputs, y)
    loss.backward()
    optimizer.step()

    if epoch % 100 == 0:
        print(f"Эпоха {epoch}, Потеря: {loss.item():.4f}")

# Тестируем сеть
with torch.no_grad():  # Отключаем градиенты для тестирования
    for i in range(len(x)):
        output = model(x[i]).item()
        print(f"Вход: {x[i].tolist()}, Выход: {round(output)}")
