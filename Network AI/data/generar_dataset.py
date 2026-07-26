import csv
import random

# Número de redes a generar
TOTAL = 1000

with open("entrenamiento.csv", "w", newline="", encoding="utf-8") as archivo:

    escritor = csv.writer(archivo)

    escritor.writerow([
        "wpa",
        "abierta",
        "wep",
        "ccmp",
        "tkip",
        "banda",
        "canal",
        "senal",
        "radio",
        "resultado"
    ])

    for _ in range(TOTAL):

        # Seguridad
        abierta = random.choice([0, 1])

        if abierta:
            wpa = 0
            wep = 0
            ccmp = 0
            tkip = 0
            resultado = 0

        else:

            tipo = random.choice(["WPA2", "WPA3", "WEP"])

            wpa = 1 if tipo in ["WPA2", "WPA3"] else 0
            wep = 1 if tipo == "WEP" else 0

            cifrado = random.choice(["CCMP", "TKIP"])

            ccmp = 1 if cifrado == "CCMP" else 0
            tkip = 1 if cifrado == "TKIP" else 0

            # Regla para etiquetar
            if wpa and ccmp:
                resultado = 1
            else:
                resultado = 0

        # Banda
        banda = random.choice([2.4, 5, 6])

        # Canal
        canal = random.randint(1, 13)

        # Señal
        senal = random.randint(20, 100)

        # Radio
        radio = random.choice([0, 1, 2])
        # 0 = 802.11n
        # 1 = 802.11ac
        # 2 = 802.11ax

        escritor.writerow([
            wpa,
            abierta,
            wep,
            ccmp,
            tkip,
            banda,
            canal,
            senal,
            radio,
            resultado
        ])

print("Dataset generado correctamente.")