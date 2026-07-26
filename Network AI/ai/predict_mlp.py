import numpy as np
from pathlib import Path
from ai.mlp import MLP

red = MLP()

modelo = Path(__file__).parent.parent / "models" / "mlp_modelo.npz"

red.cargar_modelo(modelo)

print("=== Analizador WiFi ===")

wpa = float(input("¿Tiene WPA2/WPA3? (1/0): "))
wps = float(input("¿WPS desactivado? (1/0): "))
senal = float(input("Señal (0-100): ")) / 100

entrada = np.array([[wpa, wps, senal]])

probabilidad = red.predict(entrada)[0][0]

print(f"\nProbabilidad: {probabilidad*100:.2f}%")

if probabilidad >= 0.5:
    print("🟢 RED SEGURA")
else:
    print("🔴 RED INSEGURA")