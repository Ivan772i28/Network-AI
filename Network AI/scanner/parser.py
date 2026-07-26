def obtener_redes(texto):

    redes = []
    red_actual = None

    for linea in texto.splitlines():

        linea = linea.strip()

        # Saltar líneas vacías
        if not linea:
            continue

        # Nuevo SSID
        if linea.startswith("SSID "):

            if red_actual:
                redes.append(red_actual)

            nombre = linea.split(":", 1)[1].strip()

            red_actual = {
                "ssid": nombre
            }

            continue

        if red_actual is None:
            continue

        # Autenticación
        if linea.startswith("Autenticación"):

            red_actual["auth"] = linea.split(":", 1)[1].strip()

        # Cifrado
        elif linea.startswith("Cifrado"):

            red_actual["cipher"] = linea.split(":", 1)[1].strip()

        # Señal
        elif linea.startswith("Señal"):

            valor = linea.split(":", 1)[1]
            valor = valor.replace("%", "").strip()

            try:
                red_actual["signal"] = int(valor)
            except ValueError:
                red_actual["signal"] = 0

        # Tipo de radio
        elif linea.startswith("Tipo de radio"):

            red_actual["radio"] = linea.split(":", 1)[1].strip()

        # Banda
        elif linea.startswith("Banda"):

            red_actual["band"] = linea.split(":", 1)[1].strip()

        # Canal
        elif linea.startswith("Canal"):

            try:
                red_actual["channel"] = int(linea.split(":", 1)[1].strip())
            except ValueError:
                red_actual["channel"] = 0

    # Agregar la última red
    if red_actual:
        redes.append(red_actual)

    return redes