import string


class Preprocesa:
    def __init__(self):
        self.text=''

    def remove_punctuation(self,text):
        especiales = {"\"" , "." , "," , " " , ";" , ":" , "-" , "/"}
        for i in especiales:
            text.replace(i," ")
        forbidden = {"?", "¿", "¡", "!","<",">","(",")","\"",".",","," ",":",";","-","&","@","/","N/A","#","$"}
        pf = set(string.punctuation).union(forbidden) # Se crea un set con los caracteres prohibidos (unión de punctuation y forbidden)
        punctuationfree="".join([i  for i in text if i not in pf]) # Se crea una nueva cadena sin los caracteres prohibidos
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

preprocesador = Preprocesa()
texto = "¡AAAAAAAAAAAAAAAHHHHHHHH!"
texto_sin_puntuacion = preprocesador.remove_punctuation(texto)
texto_minusculas = preprocesador.lower_words(texto_sin_puntuacion)
texto_sin_acentos = preprocesador.quitarAcentos(texto_minusculas)

print(texto_sin_acentos)