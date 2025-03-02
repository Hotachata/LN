import string
import pandas as pd
from collections import defaultdict

class Preprocesa:
    def __init__(self):
        self.text=''

    def remove_punctuation(self,text):
        especiales = {"\"" , "." , "," , " " , ";" , ":" , "-" , "/"}
        for i in especiales:
            text.replace(i," ")
        # (le quité el espacio a forbbiden)
        forbidden = {"?" , "¿" , "¡" , "!" , "<" , ">" , "(" , ")" , "\"" , "," , ":" , ";" , "-" , "&" , "@" , "/" , "N/A" , "#" , "$"}
        pf = set(string.punctuation).union(forbidden) # caracteres prohibidos (unión de punctuation y forbidden)
        punctuationfree="".join([i  for i in text if i not in pf]) # nueva cadena sin los caracteres prohibidos
        return punctuationfree.strip()

    def lower_words(self,text):
        words_lower = text.lower()
        return words_lower

    def quitarAcentos(self, s):
        replacements = (
            ("á", "a"),
            ("é", "e"),
            ("í", "i"),
            ("ó", "o"),
            ("ú", "u"),
            ("ñ", "n"),
            (".", " ")
            )
        for a, b in replacements:
            s = s.replace(a, b).replace(a.upper(), b.upper())
        return s
    
    # método para preprocesar el texto
    def preprocesamiento(self, text):
        text = self.quitarAcentos(text) #quita acentos, ñ y añade espacios después del .
        text = self.lower_words(text)
        text = self.remove_punctuation(text)
        return text

def create_bow(dataframe): # la función create_bow fue generada por deepseek
    # Paso 1: Tokenización y construcción del vocabulario
    vocabulary = set()
    for document in dataframe:
        words = document.split()
        vocabulary.update(words)
    
    # Convertir el vocabulario a una lista para mantener un orden
    vocabulary = list(vocabulary)
    
    # Paso 2: Crear la BoW para cada documento
    bow = []
    for document in dataframe:
        word_count = defaultdict(int)
        words = document.split()
        for word in words:
            word_count[word] += 1
        # Crear un vector de conteo para el documento actual
        bow_vector = [word_count[word] for word in vocabulary]
        bow.append(bow_vector)
    
    return bow, vocabulary

try:
    df = pd.read_csv("news.csv") # dataframe, encoding='utf-8'
    preprocesador = Preprocesa()
    # preprocesamiento en la columna news (creamos nueva columna "preprocesado")
    df["preprocesado"] = df["news"].apply(preprocesador.preprocesamiento)
    # nuevo archivo CSV
    df.to_csv("news1.csv", index=False)
    print("\nArchivo preprocesado!\n")
    
    # leemos el nuevo archivo con el texto filtrado
    df = pd.read_csv("news1.csv") # reescribimos dataframe
    df["preprocesado"] = df["preprocesado"].astype(str) # hacemos que todos los valores sean str
    # print("1")
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
    print(bow_df.head())  # Imprime las primeras filas de la BoW
    
except Exception as e:
    print(f"\nHa ocurrido un error: {e}\n")
