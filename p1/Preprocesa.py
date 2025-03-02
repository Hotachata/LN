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
        forbidden = {"?" , "¿" , "¡" , "!" , "<" , ">" , "(" , ")" , "\"" , "." , "," , ":" , ";" , "-" , "&" , "@" , "/" , "N/A" , "#" , "$"}
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
            )
        for a, b in replacements:
            s = s.replace(a, b).replace(a.upper(), b.upper())
        return s
    
    # método para preprocesar el texto
    def preprocesamiento(self, text):
        text = self.quitarAcentos(text)
        text = self.lower_words(text)
        text = self.remove_punctuation(text)
        return text

df = pd.read_csv("news.csv") # dataframe
preprocesador = Preprocesa()
# preprocesamiento para news (nueva columna)
df["preprocesado"] = df["news"].apply(preprocesador.preprocesamiento)
# nuevo archivo CSV
df.to_csv("news1.csv", index=False)