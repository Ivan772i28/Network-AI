import numpy as np


def convertir(red):

    auth = red.get("auth", "").upper()
    cipher = red.get("cipher", "").upper()
    band = red.get("band", "")
    radio = red.get("radio", "").lower()

    # ------------------------
    # Autenticación
    # ------------------------

    wpa = 1 if ("WPA2" in auth or "WPA3" in auth) else 0

    abierta = 1 if "OPEN" in auth else 0

    wep = 1 if "WEP" in auth else 0

    # ------------------------
    # Cifrado
    # ------------------------

    ccmp = 1 if "CCMP" in cipher else 0

    tkip = 1 if "TKIP" in cipher else 0

    # ------------------------
    # Banda
    # ------------------------

    if "2,4" in band or "2.4" in band:
        banda = 2.4
    elif "5" in band:
        banda = 5
    elif "6" in band:
        banda = 6
    else:
        banda = 2.4

    banda = banda / 6

    # ------------------------
    # Canal
    # ------------------------

    canal = red.get("channel", 1) / 13

    # ------------------------
    # Señal
    # ------------------------

    senal = red.get("signal", 0) / 100

    # ------------------------
    # Radio
    # ------------------------

    if "11AX" in radio:
        radio = 2
    elif "11AC" in radio:
        radio = 1
    else:
        radio = 0

    radio = radio / 2

    return np.array([[
        wpa,
        abierta,
        wep,
        ccmp,
        tkip,
        banda,
        canal,
        senal,
        radio
    ]])