import numpy as np

class Perceptron:
    def __init__(self, learning_rate=0.1, n_iterations=100, threshold=0.5):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.weights = np.zeros(2)
        self.threshold = threshold
        self.bias = 0

    def activation_function(self, x):
        return 1 if x >= self.threshold else 0

    def predict(self, inputs):
        linear_output = np.dot(inputs, self.weights) + self.bias
        return self.activation_function(linear_output)

    def train(self, X, y):
        for _ in range(self.n_iterations):
            for x, y_true in zip(X, y):
                y_pred = self.predict(x)
                error = y_true - y_pred
                self.weights += error * self.learning_rate * x
                self.bias += error * self.learning_rate


#A função xor_perceptron_simple verifica se duas entradas são diferentes e, se forem, retorna 1; se forem iguais, retorna 0. Isso simula o comportamento da porta XOR, que só é verdadeira quando as entradas não são iguais.

def xor_perceptron_simple(input1, input2):
    return int(input1 != input2)

if __name__ == "__main__":

    # Dados para a porta XOR
    X_xor = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

    # Dados para a porta AND
    X_and = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y_and = np.array([0, 0, 0, 1])  # Saídas esperadas para AND

    # Criar e treinar o perceptron and
    perceptron_and = Perceptron()
    perceptron_and.train(X_and, y_and)

    # Dados para a porta OR 
    y_or = np.array([0, 1, 1, 1])


    # Criar e treinar o perceptron OR
    perceptron_or = Perceptron()
    perceptron_or.train(X_and, y_or)  # Repete X_and pois as entradas são as mesmas

    #Dados para a porta NAND
    y_nand = np.array([1, 1, 1, 0])

    # Criar e treinar o perceptron NAND
    perceptron_nand = Perceptron()
    perceptron_nand.train(X_and, y_nand)  

    # Testar o perceptron treinado
    for inputs in X_and:
        print(f"Inputs: {inputs} -> AND Prediction: {perceptron_and.predict(inputs)}")
        print(f"Inputs: {inputs} -> OR Prediction: {perceptron_or.predict(inputs)}")
        print(f"Inputs: {inputs} -> NAND Prediction: {perceptron_nand.predict(inputs)}")

    for input_pair in X_xor:
        print(f"Inputs: {input_pair} -> XOR Prediction: {xor_perceptron_simple(input_pair[0], input_pair[1])}")

