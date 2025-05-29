# Aplicación de PCA sobre el dataset de noticias, como evidencia, 
# adjunta los resultados de las métricas de evaluación (Matriz de confusión, precision, recall y F1).

# Librerías
import pandas as pd
import numpy as np
import string
# Librerías para el plot
import matplotlib.pyplot as plt
import seaborn as sns
# Lista de stopwords
from stopwords import stop_words

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

# Limpiamos el dataset (preprocesa)
numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] # Lista de números
class Preprocesa:
    def __init__(self):
        self.text=''
    def remove_punctuation(self, text):
        especiales = {"\"", ".", ",", " ", ";", ":", "-", "/"}
        for i in especiales:
            text = text.replace(i, " ")
        forbidden = set(string.punctuation).union({"¿", "¡", "<", ">", "(", ")", "\"", ",", ":", ";", "-", "&", "@", "/", "N/A", "#", "$", "‘", "’", "”"})
        text = text.replace('-', ' ')
        punctuationfree = "".join([i for i in text if i not in string.punctuation or i not in forbidden])
        return punctuationfree.strip()
    # función remove_numbers, similar a remove_punctuation
    def remove_numbers(self, text):
        numfree = "".join([i for i in text if i not in numeros]) # si el caracter no está en la lista de números, lo agrega a la nueva cadena
        return numfree.strip() # elimina los espacios en blanco al inicio y al final de la cadena
    def lower_words(self, text):
        words_lower = text.lower()
        return words_lower
    def remove_stopwords(self, text):
        text = text.split()
        text = [word for word in text if word not in stop_words]
        return " ".join(text)
    def quitar_acentos(self, s):
        replacements = (
            ("á", "a"),
            ("é", "e"),
            ("í", "i"),
            ("ó", "o"),
            ("ú", "u"),
            ("ñ", "n"),
            ("Á", "A"),
            ("É", "E"),
            ("Í", "I"),
            ("Ó", "O"),
            ("Ú", "U"),
            ("Ñ", "N"),
            (".", " ")
        )
        for a, b in replacements:
            s = s.replace(a, b)
        return s
# Crear instancia de la clase
preprocesador = Preprocesa()
def preprocesar_texto(texto):
    texto = preprocesador.lower_words(texto)
    texto = preprocesador.remove_punctuation(texto)
    texto = preprocesador.remove_numbers(texto)
    texto = preprocesador.quitar_acentos(texto)
    return texto

# Aplicar preprocesamiento a `news`
data['text_procesado'] = data['news'].fillna("").apply(preprocesar_texto)
# Mostrar el dataset con la columna nueva
print(data[['news', 'text_procesado']].head())

