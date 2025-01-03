import torch
import torch.nn as nn
import torch.optim as optim

X = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.float32)
y = torch.tensor([[0], [1], [1], [0]], dtype=torch.float32)
# print(X)
# print(y)


class XORNet(nn.Module):
    def __init__(self):
        super(XORNet, self).__init__()
        self.fc1 = nn.Linear(
            2, 4
        )  # Входной слой с 2 нейронами, выходной слой с 4 нейронами
        self.fc2 = nn.Linear(
            4, 1
        )  # Скрытый слой с 4 нейронами, выходной слой с 1 нейроном
        self.sigmoid = nn.Sigmoid()
        print(self.fc1)
        print(self.fc2)

    def forward(self, x):
        x = self.fc1(x)
        x = self.sigmoid(x)
        x = self.fc2(x)
        x = self.sigmoid(x)
        return x

model = XORNet()
criterion = nn.MSELoss()  # Среднеквадратичная ошибка
optimizer = optim.SGD(model.parameters(), lr=0.1)

num_epochs = 1000
for epoch in range(num_epochs):
    # Forward pass
    outputs = model(X)
    loss = criterion(outputs, y)

    # Backward and optimize
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if (epoch+1) % 100 == 0:
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

with torch.no_grad():
    predicted = model(X)
    predicted = (predicted > 0.5).float()  # Преобразуем в бинарный выход
    print('Predicted:', predicted)
    print('Actual:', y)