from pathlib import Path

from ai.mlp import MLP
from scanner.scanner import escanear
from scanner.parser import obtener_redes
from scanner.features import convertir

# Escanear redes
texto = escanear()

# Obtener lista de redes
redes = obtener_redes(texto)

# Cargar modelo entrenado
red = MLP()

modelo = Path("models") / "mlp_modelo.npz"

red.cargar_modelo(modelo)

print("=" * 60)

for wifi in redes:

    # Convertir la información al formato de entrada de la IA
    entrada = convertir(wifi)

    # Obtener probabilidad
    probabilidad = red.predict(entrada)[0][0]

    print(f"\nSSID           : {wifi.get('ssid')}")
    print(f"Autenticación  : {wifi.get('auth')}")
    print(f"Cifrado        : {wifi.get('cipher')}")
    print(f"Señal          : {wifi.get('signal')}%")
    print(f"Canal          : {wifi.get('channel')}")
    print(f"Radio          : {wifi.get('radio')}")

    print(f"\nProbabilidad de seguridad: {probabilidad*100:.2f}%")

    if probabilidad >= 0.5:
        print("🟢 RED SEGURA")
    else:
        print("🔴 RED INSEGURA")

    print("-" * 60)