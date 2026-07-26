import numpy as np
from pathlib import Path

from ai.mlp import MLP

# ==========================================
# Cargar dataset
# ==========================================

ruta = Path(__file__).parent.parent / "data" / "entrenamiento.csv"

datos = np.loadtxt(ruta, delimiter=",", skiprows=1)

# ==========================================
# Entradas (9 características)
# ==========================================

X = datos[:, 0:9]

# ==========================================
# Normalización
# ==========================================

# Banda (2.4, 5, 6 GHz)
X[:, 5] = X[:, 5] / 6

# Canal (1-13)
X[:, 6] = X[:, 6] / 13

# Señal (20-100)
X[:, 7] = X[:, 7] / 100

# Radio
# 0 = 802.11n
# 1 = 802.11ac
# 2 = 802.11ax
X[:, 8] = X[:, 8] / 2

# ==========================================
# Salida esperada
# ==========================================

y = datos[:, 9].reshape(-1, 1)

# ==========================================
# Crear la red neuronal
# ==========================================

red = MLP(
    entradas=9,
    ocultas=16,
    salidas=1
)

# ==========================================
# Entrenar
# ==========================================

print("\nEntrenando la red...\n")

red.train(
    X,
    y,
    epochs=5000,
    lr=0.1
)

print("\nEntrenamiento terminado.\n")

# ==========================================
# Guardar modelo
# ==========================================

carpeta = Path(__file__).parent.parent / "models"
carpeta.mkdir(exist_ok=True)

modelo = carpeta / "mlp_modelo.npz"

red.guardar_modelo(modelo)

print(f"Modelo guardado en:\n{modelo}")

# ==========================================
# Pruebas
# ==========================================

print("\n=========== PRUEBAS ===========\n")

pruebas = np.array([

    # WPA2 + CCMP (segura)
    [1,0,0,1,0,5/6,1/13,0.95,0],

    # WPA3 + CCMP + WiFi 6 (muy segura)
    [1,0,0,1,0,6/6,6/13,0.90,1],

    # Red abierta
    [0,1,0,0,0,2.4/6,11/13,0.80,0],

    # WEP + TKIP
    [0,0,1,0,1,2.4/6,3/13,0.60,0]

])

probabilidades = red.predict(pruebas)

for i, (entrada, prob) in enumerate(zip(pruebas, probabilidades), start=1):

    estado = "SEGURA" if prob[0] >= 0.5 else "INSEGURA"

    print(f"Prueba {i}")
    print("Entrada:", entrada)
    print(f"Probabilidad: {prob[0]*100:.2f}%")
    print("Clasificación:", estado)
    print("-" * 40)