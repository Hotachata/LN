# Aplicación de PCA sobre el dataset de noticias, como evidencia, 
# adjunta los resultados de las métricas de evaluación (Matriz de confusión, precision, recall y F1).

# Librerías
import pandas as pd
import numpy as np
# Librerías para el plot
import matplotlib.pyplot as plt
import seaborn as sns

# Guardamos los datos dentro del dataset de noticias en data
data = pd.read_csv("news.csv")
print(data.head()) # Imprimimos los primeros cinco datos dentro del dataset

# Generamos la gráfica con los tipos de noticias
columna_tipo_noticia = 'Type' # Ajusta 'Type' al nombre real de la columna con los tipos de noticia
conteo_tipos = data[columna_tipo_noticia].value_counts() # Contar registros por tipo de noticia
# Creamos la gráfica con matplotlib
plt.figure(figsize=(10, 6))
sns.barplot(x=conteo_tipos.index, y=conteo_tipos.values, palette='viridis')
# Labels para la gráfica
plt.title('Cantidad de registros por tipo de noticia')
plt.xlabel('Tipo de noticia')
plt.ylabel('Cantidad de registros')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()