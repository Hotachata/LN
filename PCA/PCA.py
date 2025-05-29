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
# Nube de palabras
import spacy # python -m spacy download es_core_news_sm
from wordcloud import WordCloud as wc

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
plt.show() # Mostramos la gráfica

# Limpiamos el dataset (preprocesa)
numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] # Lista de números
# Cargamos el modelo en español de spacy
nlp = spacy.load("es_core_news_sm") # Cargamos el modelo en español de spacy
# Lista personalizada de stopwords desde el archivo txt
with open("stopwords.txt", "r", encoding="utf-8") as f:
    stop_words = set(f.read().strip().split("\n"))
# Añadimos las stopwords personalizadas a las stopwords de spaCy
stop_words = stop_words.union(set(nlp.Defaults.stop_words))
class Preprocesa: # Creamos la clase Preprocesa para preprocesar el dataset
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
# Función para procesar con spaCy
def preprocesar_con_spacy(texto):
    doc = nlp(texto)  # Ya el texto está sin acentos y en minúsculas
    tokens_limpios = [
        token.lemma_ for token in doc
        if token.is_alpha and token.lemma_ not in stop_words  # Filtramos stopwords
    ]
    return " ".join(tokens_limpios)

# Creamos una nueva celda que guarde el texto preprocesado
data['texto_procesado'] = data['news'].fillna("").apply(preprocesar_texto)  # Primero limpiar el texto
data['texto_procesado'] = data['texto_procesado'].apply(preprocesar_con_spacy)  # Luego procesar con spaCy
print(data[['news', 'texto_procesado']].head()) # Imprimimos los cinco primeros textos y sus versiones originales

# Unir todos los textos preprocesados en una sola cadena
texto_completo = " ".join(data['texto_procesado'].dropna())
# Crear la nube de palabras
wordcloud = wc(width=800, height=400, background_color='white', colormap='viridis').generate(texto_completo)

# Mostrar la nube de palabras
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")  # Desactivar los ejes
plt.show()