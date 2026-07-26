import random
import math
import json


class Neurona:

    def __init__(self):

        self.w1 = random.uniform(-1, 1)
        self.w2 = random.uniform(-1, 1)
        self.w3 = random.uniform(-1, 1)

        self.bias = random.uniform(-1, 1)

    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))

    def pensar(self, x1, x2, x3):

        suma = (
            x1 * self.w1 +
            x2 * self.w2 +
            x3 * self.w3 +
            self.bias
        )

        return self.sigmoid(suma)

    def entrenar(self, x1, x2, x3, esperado, tasa=0.01):

        salida = self.pensar(x1, x2, x3)

        error = esperado - salida

        self.w1 += tasa * error * x1
        self.w2 += tasa * error * x2
        self.w3 += tasa * error * x3

        self.bias += tasa * error

        return error
    def guardar(self, archivo):

        datos = {
            "w1": self.w1,
            "w2": self.w2,
            "w3": self.w3,
            "bias": self.bias
        }

        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4)

    def cargar(self, archivo):

        with open(archivo, "r", encoding="utf-8") as f:
            datos = json.load(f)

        self.w1 = datos["w1"]
        self.w2 = datos["w2"]
        self.w3 = datos["w3"]
        self.bias = datos["bias"]