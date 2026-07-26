import subprocess


def escanear():

    comando = [
        "netsh",
        "wlan",
        "show",
        "networks",
        "mode=bssid"
    ]

    resultado = subprocess.run(
        comando,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="ignore"
    )

    return resultado.stdout
from scanner.scanner import escanear

print(escanear())