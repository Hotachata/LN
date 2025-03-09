import string
import pandas as pd
from collections import defaultdict
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import matplotlib.pyplot as plt

# Preprocesamiento del texto
class Preprocesa:
    def __init__(self):
        self.stopwords = set(stopwords.words('spanish'))
        self.lemmatizer = WordNetLemmatizer()

    def remove_punctuation(self, text):
        forbidden = set(string.punctuation).union({"¿", "¡", "<", ">", "(", ")", "\"", ",", ":", ";", "-", "&", "@", "/", "N/A", "#", "$", "‘", "’", "_"})
        return "".join([char for char in text if char not in forbidden])

    def lower_words(self, text):
        return text.lower()

    def remove_stopwords(self, text):
        return " ".join([word for word in text.split() if word not in self.stopwords])

    def remove_accents(self, text):
        replacements = (
            ("á", "a"),
            ("é", "e"),
            ("í", "i"),
            ("ó", "o"),
            ("ú", "u"),
            ("ñ", "n"),
        )
        for a, b in replacements:
            text = text.replace(a, b).replace(a.upper(), b.upper())
        return text

    def lemmatize_text(self, text):
        return " ".join([self.lemmatizer.lemmatize(word) for word in text.split()])

    def preprocesamiento(self, text):
        text = self.remove_accents(text)
        text = self.lower_words(text)
        text = self.remove_punctuation(text)
        text = self.remove_stopwords(text)
        text = self.lemmatize_text(text)
        return text

def create_bow(dataframe):
    vocabulary = set()
    for document in dataframe:
        words = document.split()
        vocabulary.update(words)
    
    vocabulary = list(vocabulary)
    
    bow = []
    for document in dataframe:
        word_count = defaultdict(int)
        words = document.split()
        for word in words:
            word_count[word] += 1
        bow_vector = [word_count[word] for word in vocabulary]
        bow.append(bow_vector)
    
    return bow, vocabulary

try:
    # Cargar el archivo CSV
    df = pd.read_csv("news.csv")
    preprocesador = Preprocesa()
    
    # Normalización y eliminación de stopwords
    df["preprocesado"] = df["news"].apply(preprocesador.preprocesamiento)
    df.to_csv("news1.csv", index=False)
    print("\nArchivo preprocesado!\n")
    
    df = pd.read_csv("news1.csv")
    df["preprocesado"] = df["preprocesado"].astype(str)
    dataframe = df["preprocesado"].tolist()
    print("Creando BoW! Espera un momento!\n")
    
    # Crear la Bag of Words
    bow, vocabulary = create_bow(dataframe)
    
    # Convertir la BoW en un DataFrame
    bow_df = pd.DataFrame(bow, columns=vocabulary)
    
    # Guardar la BoW en un nuevo archivo CSV
    bow_df.to_csv("bow.csv", index=False)
    print("\nBag of Words guardada en 'bow.csv'!\n")
    
    # Imprimir la BoW (fragmento)
    print("Bag of Words:")
    print(bow_df.head())
    
    # Graficar la frecuencia de los tipos de noticias
    conteotipos = df["Type"].value_counts()
    plt.figure(figsize=(5, 3))
    conteotipos.plot(kind="bar", color="skyblue")
    plt.xlabel("Tipo de noticia")
    plt.ylabel("Frecuencia")
    plt.title("Frecuencia por tipo de noticia")
    plt.show()
    
except Exception as e:
    print(f"\nHa ocurrido un error: {e}\n")