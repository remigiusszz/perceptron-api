# model.py
import numpy as np

class Perceptron:
    def __init__(self, input_size, lr=0.01):
        self.weights = np.zeros(input_size + 1)
        self.lr = lr

    def predict(self, x):
        x = np.insert(x, 0, 1)
        summation = np.dot(self.weights, x)
        return 1 if summation > 0 else 0

    def train(self, X, y, epochs=10):
        for _ in range(epochs):
            for xi, target in zip(X, y):
                update = self.lr * (target - self.predict(xi))
                xi = np.insert(xi, 0, 1)
                self.weights += update * xi
