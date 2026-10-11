import pandas as pd

# Crear un diccionario
diccionario = {
    "Nombre": ["Juan", "Pedro"],
    "Edad": [30, 25],
    "Ciudad": ["Santiago", "Concepción"],
}

# Imprimir el diccionario
df = pd.DataFrame(diccionario)

df.head(2)
