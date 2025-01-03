import torch
import torch.nn as nn
import torch.optim as optim

# Пример модели
model = nn.Linear(2, 1)  # Линейная модель с 2 входами и 1 выходом

# Оптимизатор
optimizer = optim.SGD(model.parameters(), lr=0.1)

# Пример данных
inputs = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
targets = torch.tensor([[1.0], [2.0]])

# Функция потерь
criterion = nn.MSELoss()

# Прямой проход
outputs = model(inputs)
loss = criterion(outputs, targets)

# Вычисление градиентов
loss.backward()

# Обновление параметров
optimizer.step()
