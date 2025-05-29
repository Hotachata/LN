# Aplicación de PCA sobre el dataset de noticias, como evidencia, 
# adjunta los resultados de las métricas de evaluación (Matriz de confusión, precision, recall y F1).

# Librerías
import pandas as pd
import numpy as np

# Guardamos los datos dentro del dataset de noticias en data
data = pd.read_csv("news.csv")
print(data.head()) # Imprimimos los primeros cinco datos dentro del dataset