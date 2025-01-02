import torch
import torch.nn as nn
import torch.optim as optim

# Простая модель с одним линейным слоем
model = nn.Linear(1, 1)

# Оптимизатор SGD
optimizer = optim.SGD(model.parameters(), lr=0.1)

# Пример входных данных
x = torch.tensor([[1.0]])
y_true = torch.tensor([[2.0]])

# Функция потерь (MSE)
criterion = nn.MSELoss()

# Прямой проход (вычисление предсказания)
y_pred = model(x)

# Вычисление потерь
loss = criterion(y_pred, y_true)
print("Loss before optimization:", loss.item())

# Обратный проход (вычисление градиентов)
loss.backward()

# Шаг оптимизации (обновление параметров)
optimizer.step()

# Сброс градиентов
optimizer.zero_grad()

# Новое предсказание
y_pred_updated = model(x)
loss_updated = criterion(y_pred_updated, y_true)
print("Loss after optimization:", loss_updated.item())
