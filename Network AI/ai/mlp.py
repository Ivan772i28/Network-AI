import numpy as np


class MLP:

    def __init__(self, entradas=9, ocultas=16, salidas=1):
        np.random.seed(42)

        # Pesos capa de entrada -> capa oculta
        self.W1 = np.random.randn(entradas, ocultas)

        # Bias capa oculta
        self.b1 = np.zeros((1, ocultas))

        # Pesos capa oculta -> salida
        self.W2 = np.random.randn(ocultas, salidas)

        # Bias salida
        self.b2 = np.zeros((1, salidas))

    # Función sigmoide
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    # Derivada de la sigmoide
    def sigmoid_derivada(self, x):
        return x * (1 - x)

    # Propagación hacia adelante
    def forward(self, X):
        self.z1 = np.dot(X, self.W1) + self.b1
        self.a1 = self.sigmoid(self.z1)

        self.z2 = np.dot(self.a1, self.W2) + self.b2
        self.a2 = self.sigmoid(self.z2)

        return self.a2

    # Entrenamiento (Corregida la indentación para que pertenezca a la clase)
    def train(self, X, y, epochs=5000, lr=0.05):
        n = X.shape[0]

        for epoch in range(epochs):
            # Forward
            salida = self.forward(X)

            # Error
            error = salida - y

            # Gradiente de la capa de salida
            d_output = error * self.sigmoid_derivada(salida)

            # Gradiente de la capa oculta
            d_hidden = np.dot(d_output, self.W2.T) * self.sigmoid_derivada(
                self.a1
            )

            # Actualización de pesos (promediando por número de muestras)
            self.W2 -= lr * np.dot(self.a1.T, d_output) / n
            self.b2 -= lr * np.sum(d_output, axis=0, keepdims=True) / n

            self.W1 -= lr * np.dot(X.T, d_hidden) / n
            self.b1 -= lr * np.sum(d_hidden, axis=0, keepdims=True) / n

            if epoch % 500 == 0:
                mse = np.mean((y - salida) ** 2)
                print(f"Época {epoch} - Error: {mse:.6f}")

    # Devuelve la probabilidad
    def predict(self, X):
        return self.forward(X)

    # Clasificación
    def clasificar(self, X):
        probabilidades = self.predict(X)
        return (probabilidades >= 0.5).astype(int)

    # Guardar modelo
    def guardar_modelo(self, archivo):
        np.savez(
            archivo, W1=self.W1, b1=self.b1, W2=self.W2, b2=self.b2
        )

    # Cargar modelo
    def cargar_modelo(self, archivo):
        datos = np.load(archivo)
        self.W1 = datos["W1"]
        self.b1 = datos["b1"]
        self.W2 = datos["W2"]
        self.b2 = datos["b2"]