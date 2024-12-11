import torch


def activation_func(x):
    return torch.tensor(1) if x >= 0 else torch.tensor(0)


class Perceptron:
    def __init__(self, num_inputs):
        # num_inputs - количество входов
        self.weights = torch.rand(num_inputs, dtype=torch.float64)
        self.bias = torch.rand(1, dtype=torch.float64)

    def feed_forward(self, inputs):
        return activation_func(torch.sum(inputs * self.weights) + self.bias)

    def train(self, inputs, target, learning_rate=0.1):
        output = self.feed_forward(inputs)
        error = target - output

        self.weights += error * inputs * learning_rate
        self.bias += error * learning_rate


if __name__ == '__main__':
    perceptron = Perceptron(2)

    training_inputs = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]],
                                   dtype=torch.float64)
    training_outputs = torch.tensor([0, 0, 0, 1], dtype=torch.float64)

    # for _ in range(5):
    #     for inputs, target in zip(training_inputs, training_outputs):
    #         perceptron.train(inputs, target)
    #
    # for inputs, target in zip(training_inputs, training_outputs):
    #     output = perceptron.feed_forward(inputs)
    #     print(f"Входы: {inputs.tolist()} Выход: {int(output)}")

    # correct = 0
    # for inputs, target in zip(training_inputs, training_outputs):
    #     output = perceptron.feed_forward(inputs)
    #     if output == target:
    #         correct += 1
    # print(f"Точность: {correct / len(training_outputs) * 100:.2f}%")

    max_epochs = 1000  # Максимальное число эпох
    for epoch in range(max_epochs):
        total_error = 0
        for inputs, target in zip(training_inputs, training_outputs):
            output = perceptron.feed_forward(inputs)
            error = target - output
            total_error += abs(error)
            perceptron.train(inputs, target)
        if total_error == 0:
            print(f"Обучение завершено за {epoch + 1} эпох.")
            break
    else:
        print(
            "Достигнуто максимальное число эпох, но персептрон всё ещё обучается.")
