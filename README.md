# 🛡️ Network AI

Sistema de análisis de seguridad de redes Wi-Fi utilizando un escáner de redes y una red neuronal MLP desarrollada desde cero con Python y NumPy.

El proyecto tiene como objetivo analizar las características de las redes Wi-Fi detectadas y utilizar Inteligencia Artificial para estimar si una red puede considerarse segura o insegura.

> 🚧 Proyecto en desarrollo.

---

## 🎯 Objetivo del proyecto

El objetivo de Network AI es desarrollar una herramienta capaz de analizar redes Wi-Fi cercanas y utilizar Inteligencia Artificial para estimar su nivel de seguridad.

El objetivo final es poder ejecutar:

```bash
python -m main
```

y obtener automáticamente información como:

```text
============================================================

SSID           : DigitalNet_4BAF
Autenticación  : WPA2-Personal
Cifrado        : CCMP
Señal          : 81%
Canal          : 1
Radio          : 802.11n

🔐 Seguridad estimada: 93.42%

🟢 Clasificación: SEGURA

Fortalezas:
✔ WPA2 detectado
✔ Cifrado CCMP
✔ Señal excelente (81%)
✔ Canal válido

Debilidades:
⚠ No utiliza WPA3
⚠ WPS no pudo verificarse

Recomendación:
Puede utilizarse con un nivel de riesgo bajo.

============================================================
```

Este formato representa el objetivo de presentación final del proyecto.

---

# 🧠 Arquitectura del sistema

El funcionamiento general de Network AI está diseñado de la siguiente manera:

```text
                 ┌─────────────────┐
                 │     RED WI-FI   │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │  WI-FI SCANNER  │
                 │  Detección redes│
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │     PARSER      │
                 │ Procesamiento   │
                 │     de datos    │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │    FEATURES     │
                 │ Características │
                 │    numéricas    │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │       MLP       │
                 │ Inteligencia IA │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │   PREDICCIÓN    │
                 │ Seguridad Wi-Fi │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │    ANÁLISIS     │
                 │   Resultado     │
                 └─────────────────┘
```

---

# 📁 Estructura del proyecto

La estructura actual del proyecto es:

```text
Network AI/
│
├── ai/
│   ├── __init__.py
│   ├── mlp.py
│   ├── neurona.py
│   ├── predict_mlp.py
│   └── train_mlp.py
│
├── data/
│   └── entrenamiento.csv
│
├── models/
│   ├── mlp_modelo.npz
│   └── modelo.json
│
├── scanner/
│   ├── __init__.py
│   ├── features.py
│   ├── parser.py
│   └── scanner.py
│
├── main.py
├── redes.csv
├── scanner.py
└── README.md
```

---

# 🔍 Escáner de redes Wi-Fi

El proyecto cuenta con un escáner para obtener información de las redes Wi-Fi visibles.

En Windows se utiliza el comando:

```bash
netsh wlan show networks mode=bssid
```

El escáner puede obtener información como:

- SSID
- Autenticación
- Cifrado
- Señal
- Canal
- Banda
- Tipo de radio
- BSSID

Ejemplo de información obtenida:

```text
SSID           : DigitalNet_4BAF
Autenticación  : WPA2-Personal
Cifrado        : CCMP
Señal          : 81%
Canal          : 1
Radio          : 802.11n
```

Otro ejemplo:

```text
SSID           : RED_NET-5029_EXT
Autenticación  : WPA2-Personal
Cifrado        : CCMP
Señal          : 50%
Canal          : 9
Radio          : 802.11n
```

La información obtenida puede procesarse mediante expresiones regulares y posteriormente almacenarse en archivos CSV.

---

# 📊 Dataset de entrenamiento

El modelo de Inteligencia Artificial utiliza un dataset ubicado en:

```text
data/entrenamiento.csv
```

Actualmente el dataset contiene las siguientes características:

```text
wpa
abierta
wep
ccmp
tkip
banda
canal
senal
radio
resultado
```

Ejemplo:

```csv
wpa,abierta,wep,ccmp,tkip,banda,canal,senal,radio,resultado
1,0,0,1,0,2.4,3,98,2,1
1,0,0,0,1,5,5,75,2,0
1,0,0,1,0,6,5,77,1,1
0,1,0,0,0,2.4,3,27,1,0
0,1,0,0,0,2.4,1,54,2,0
0,0,1,0,1,2.4,1,89,1,0
```

La columna `resultado` representa la etiqueta utilizada durante el entrenamiento:

```text
0 = Insegura
1 = Segura
```

---

# 🧮 Características utilizadas

El modelo utiliza las siguientes características:

| Característica | Descripción |
|---|---|
| `wpa` | Indica si la red utiliza WPA/WPA2 |
| `abierta` | Indica si la red está abierta |
| `wep` | Indica si se detecta WEP |
| `ccmp` | Indica el uso de cifrado CCMP |
| `tkip` | Indica el uso de cifrado TKIP |
| `banda` | Banda de frecuencia utilizada |
| `canal` | Canal Wi-Fi utilizado |
| `senal` | Intensidad de la señal |
| `radio` | Tipo de radio inalámbrica |
| `resultado` | Clasificación utilizada para el entrenamiento |

---

# 🤖 Red neuronal MLP

La Inteligencia Artificial principal está implementada en:

```text
ai/mlp.py
```

La red neuronal fue desarrollada utilizando:

```python
import numpy as np
```

La implementación se realizó desde cero utilizando NumPy.

No se utiliza TensorFlow ni PyTorch para la implementación de la red neuronal.

La MLP implementa:

- Forward Propagation.
- Backpropagation.
- Función Sigmoide.
- Derivada de la Sigmoide.
- Actualización de pesos.
- Bias.
- Entrenamiento supervisado.
- Predicción.
- Clasificación.
- Guardado del modelo.
- Carga del modelo.

---

# 🧠 Arquitectura de la MLP

La arquitectura utilizada es:

```text
Entradas
   │
   │
   ▼
Capa oculta
   │
   │
   ▼
Capa de salida
   │
   ▼
Predicción
```

La clase principal es:

```python
class MLP:
```

La red puede inicializarse utilizando:

```python
red = MLP(
    entradas=3,
    ocultas=4,
    salidas=1
)
```

La arquitectura puede configurarse mediante:

- Número de entradas.
- Número de neuronas ocultas.
- Número de salidas.

---

# 🔄 Forward Propagation

La red utiliza propagación hacia adelante para obtener una predicción.

El proceso general es:

```text
Entrada
   ↓
W1 + b1
   ↓
Sigmoide
   ↓
Capa oculta
   ↓
W2 + b2
   ↓
Sigmoide
   ↓
Salida
```

---

# 🔙 Backpropagation

El entrenamiento utiliza Backpropagation para ajustar los pesos de la red neuronal.

El proceso permite calcular el error entre:

```text
Valor esperado
```

y:

```text
Valor obtenido
```

Posteriormente se actualizan:

```text
W1
b1
W2
b2
```

para reducir progresivamente el error.

---

# 📉 Entrenamiento

El entrenamiento se realiza utilizando el método:

```python
red.train(X, y)
```

La configuración utilizada actualmente incluye:

```text
Épocas: 5000
Learning Rate: 0.1
```

Durante el entrenamiento se muestra el error MSE.

Ejemplo de entrenamiento:

```text
Época 0 - Error: 0.440673
Época 500 - Error: 0.004357
Época 1000 - Error: 0.001613
Época 1500 - Error: 0.000947
Época 2000 - Error: 0.000659
Época 2500 - Error: 0.000501
Época 3000 - Error: 0.000402
Época 3500 - Error: 0.000335
Época 4000 - Error: 0.000286
Época 4500 - Error: 0.000249
```

Esto demuestra que la red puede reducir considerablemente el error durante el proceso de entrenamiento.

---

# 💾 Guardado del modelo

Una vez entrenado el modelo, sus pesos y bias pueden almacenarse utilizando NumPy.

El modelo se guarda en:

```text
models/mlp_modelo.npz
```

El archivo contiene:

```text
W1
b1
W2
b2
```

El modelo puede guardarse utilizando:

```python
red.guardar_modelo(
    "models/mlp_modelo.npz"
)
```

Esto permite conservar el modelo entrenado y utilizarlo posteriormente sin necesidad de realizar nuevamente el entrenamiento.

---

# 📂 Carga del modelo

El modelo entrenado puede cargarse posteriormente utilizando:

```python
red = MLP()

red.cargar_modelo(
    "models/mlp_modelo.npz"
)
```

Esto permite separar el proceso de entrenamiento del proceso de predicción.

El flujo es:

```text
Entrenamiento
      │
      ▼
Guardar modelo
      │
      ▼
mlp_modelo.npz
      │
      ▼
Cargar modelo
      │
      ▼
Realizar predicciones
```

---

# 🔮 Predicción

La red neuronal cuenta con un método para obtener la salida:

```python
red.predict(X)
```

También cuenta con un método de clasificación:

```python
red.clasificar(X)
```

La clasificación utiliza un umbral de:

```text
0.5
```

Por lo tanto:

```text
Probabilidad >= 0.5
        ↓
     Segura
```

Mientras que:

```text
Probabilidad < 0.5
        ↓
    Insegura
```

---

# 🧪 Pruebas del modelo

El proyecto cuenta con pruebas para comprobar el funcionamiento de la red neuronal.

Ejemplo:

```python
pruebas = np.array([
    [1, 1, 0.95],
    [1, 0, 0.80],
    [0, 0, 0.95],
    [0, 1, 0.40]
])
```

Las predicciones pueden obtenerse utilizando:

```python
predicciones = red.predict(pruebas)
```

---

# 📡 Integración con el escáner

El objetivo del proyecto es integrar completamente el escáner Wi-Fi con la red neuronal.

El flujo de funcionamiento es:

```text
Red Wi-Fi detectada
        ↓
Scanner
        ↓
Parser
        ↓
Extracción de características
        ↓
Normalización
        ↓
Modelo MLP
        ↓
Predicción
        ↓
Probabilidad de seguridad
        ↓
Clasificación
```

De esta manera, el usuario no necesita introducir manualmente las características de cada red.

---

# 🔐 Análisis de seguridad

El sistema busca utilizar las características de cada red para generar una estimación de seguridad.

Entre las características analizadas se encuentran:

- Tipo de autenticación.
- Tipo de cifrado.
- Uso de WPA.
- Uso de WEP.
- Red abierta.
- Uso de CCMP.
- Uso de TKIP.
- Banda.
- Canal.
- Intensidad de señal.
- Tipo de radio.

El resultado final busca mostrar una probabilidad de seguridad.

Ejemplo:

```text
🔐 Seguridad estimada: 93.42%

🟢 Clasificación: SEGURA
```

---

# ⚠️ WPS

La detección de WPS todavía no está completamente integrada al sistema.

El comando utilizado actualmente:

```bash
netsh wlan show networks mode=bssid
```

no proporciona directamente una verificación confiable del estado de WPS.

Por este motivo, actualmente el sistema puede mostrar:

```text
⚠ WPS no pudo verificarse
```

La detección de WPS se considera una función pendiente de implementar mediante métodos específicos para cada sistema operativo.

---

# 🐧 Compatibilidad con Ubuntu y Linux

Uno de los objetivos del proyecto es permitir que Network AI pueda ejecutarse también en Ubuntu y otras distribuciones Linux.

Actualmente, el escaneo principal está basado en herramientas de Windows.

La arquitectura futura contempla utilizar diferentes métodos de escaneo según el sistema operativo.

Por ejemplo:

```text
Windows
   │
   └── netsh

Ubuntu / Linux
   │
   ├── nmcli
   └── iw
```

La Inteligencia Artificial seguirá siendo la misma.

La intención es cambiar únicamente el módulo encargado de obtener la información de las redes.

La arquitectura será:

```text
              Network AI
                  │
          ┌───────┴───────┐
          │               │
       Windows           Linux
          │               │
        netsh         nmcli / iw
          │               │
          └───────┬───────┘
                  │
                  ▼
              Parser
                  │
                  ▼
              Features
                  │
                  ▼
                MLP
                  │
                  ▼
             Predicción
```

---

# ▶️ Ejecución

## Entrenar la red neuronal

Desde la carpeta raíz del proyecto:

```bash
python -m ai.train_mlp
```

Este comando realiza el entrenamiento de la MLP y guarda el modelo.

El modelo generado se almacena en:

```text
models/mlp_modelo.npz
```

---

## Ejecutar el programa principal

Para ejecutar el sistema:

```bash
python -m main
```

El objetivo es que el programa principal realice automáticamente:

```text
1. Escanear redes Wi-Fi
        ↓
2. Obtener información
        ↓
3. Procesar datos
        ↓
4. Extraer características
        ↓
5. Normalizar datos
        ↓
6. Cargar modelo MLP
        ↓
7. Realizar predicción
        ↓
8. Calcular probabilidad
        ↓
9. Clasificar la red
        ↓
10. Mostrar fortalezas
        ↓
11. Mostrar debilidades
        ↓
12. Mostrar recomendaciones
```

---

# 🛠️ Tecnologías utilizadas

El proyecto utiliza las siguientes tecnologías:

- Python
- NumPy
- CSV
- Regular Expressions
- Subprocess
- pathlib
- Machine Learning
- Inteligencia Artificial
- Redes neuronales artificiales
- MLP
- Backpropagation

---

# 📦 Dependencias

La principal dependencia utilizada actualmente para la red neuronal es:

```text
numpy
```

La instalación puede realizarse mediante:

```bash
pip install numpy
```

También se recomienda crear un entorno virtual:

```bash
python -m venv venv
```

Activarlo en Windows:

```bash
venv\Scripts\activate
```

Y posteriormente instalar las dependencias:

```bash
pip install -r requirements.txt
```

---

# 🚧 Estado actual del proyecto

```text
🟢 Scanner Wi-Fi
🟢 Obtención de información de redes
🟢 Parser de datos
🟢 Dataset de entrenamiento
🟢 Red neuronal MLP
🟢 Forward Propagation
🟢 Backpropagation
🟢 Entrenamiento
🟢 Predicción
🟢 Clasificación
🟢 Guardado del modelo
🟢 Carga del modelo
🟢 Integración inicial con el scanner

🟡 Sistema de puntuación de seguridad
🟡 Generación de fortalezas y debilidades
🟡 Generación de recomendaciones
🟡 Detección de WPS
🟡 Detección de WPA3
🟡 Compatibilidad completa con Ubuntu
🟡 Integración final de todos los módulos

🔴 Interfaz gráfica
🔴 Dashboard
🔴 Generación de reportes
```

---

# 🚀 Próximos pasos

## 1. Integración completa

Unificar todos los módulos:

```text
Scanner
   +
Parser
   +
Features
   +
MLP
   +
Análisis
```

para que el sistema completo funcione mediante:

```bash
python -m main
```

---

## 2. Sistema de puntuación

Implementar una puntuación de seguridad de 0 a 100.

Ejemplo:

```text
0 - 20      🔴 Muy insegura
20 - 40     🔴 Insegura
40 - 60     🟠 Riesgo medio
60 - 80     🟡 Aceptable
80 - 100    🟢 Segura
```

---

## 3. Explicación de la predicción

El sistema deberá mostrar por qué una red recibió determinada clasificación.

Ejemplo:

```text
Fortalezas:

✔ WPA2 detectado
✔ Cifrado CCMP
✔ Buena intensidad de señal

Debilidades:

⚠ No se detectó WPA3
⚠ WPS no pudo verificarse
```

---

## 4. Detección de WPS

Investigar e implementar un método de detección de WPS compatible con el sistema operativo utilizado.

---

## 5. Detección de WPA3

Agregar la detección de WPA3 como una característica adicional del análisis.

---

## 6. Compatibilidad con Ubuntu

Agregar un scanner específico para Linux utilizando herramientas como:

```text
nmcli
iw
```

manteniendo la misma arquitectura de análisis e Inteligencia Artificial.

---

## 7. Interfaz final

Crear una interfaz más profesional para mostrar:

- Redes detectadas.
- Probabilidad de seguridad.
- Clasificación.
- Fortalezas.
- Debilidades.
- Recomendaciones.
- Información técnica.

---

# 🔐 Uso responsable

Network AI está diseñado para fines educativos, de investigación y auditoría autorizada.

El sistema analiza información disponible de redes inalámbricas cercanas y no debe utilizarse para acceder, atacar o comprometer redes sin autorización.

El usuario es responsable de utilizar el software de manera legal y ética.

---

# 📌 Estado del proyecto

**Network AI**

```text
Versión: 0.1.0
Estado: En desarrollo
```

El proyecto continúa en desarrollo con el objetivo de crear una herramienta de análisis de seguridad Wi-Fi asistida por Inteligencia Artificial.

---

# 🎯 Visión del proyecto

La visión final de Network AI es crear un sistema capaz de:

```text
             🔍 ESCANEAR
                  │
                  ▼
             📡 DETECTAR
                  │
                  ▼
             🧮 ANALIZAR
                  │
                  ▼
             🧠 PREDECIR
                  │
                  ▼
             🔐 EVALUAR
                  │
                  ▼
             📊 EXPLICAR
                  │
                  ▼
             💡 RECOMENDAR
```

El objetivo es que Network AI no sea únicamente un escáner de redes Wi-Fi, sino una herramienta inteligente capaz de analizar y explicar de manera clara el nivel de seguridad de las redes detectadas.

---

## ⭐ Network AI

**Inteligencia Artificial aplicada al análisis de seguridad de redes Wi-Fi.**

> Proyecto educativo y de investigación en desarrollo.