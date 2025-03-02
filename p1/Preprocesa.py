import string
import pandas as pd

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
    palabras = df["preprocesado"]
    print(palabras[1])
    
except Exception as e:
    print(f"\nHa ocurrido un error: {e}\n")
