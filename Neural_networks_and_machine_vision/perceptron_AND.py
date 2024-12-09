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
        print(self.weights, "     ", self.bias)


if __name__ == '__main__':
    perceptron = Perceptron(2)

    training_inputs = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]],
                                   dtype=torch.float64)
    training_outputs = torch.tensor([0, 0, 0, 1], dtype=torch.float64)

    for _ in range(10):
        for inputs, target in zip(training_inputs, training_outputs):
            perceptron.train(inputs, target)

    for inputs, target in zip(training_inputs, training_outputs):
        output = perceptron.feed_forward(inputs)
        print(f"Входы: {inputs.tolist()} Выход: {int(output)}")
