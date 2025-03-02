import string
import pandas as pd
from collections import defaultdict

stopwords = ["y", "en", "de", "para", "con", "el", "la", "los", "las", "un", "una", "unos", "unas", 
    "por", "que", "a", "o", "e","su","sus",
	"a", "actualmente", "adelante", "además", "afirmó", "agregó", "ahora", "ahí", "al", "algo",
    "alguna", "algunas", "alguno", "algunos", "algún", "alrededor", "ambos", "ampleamos", "ante",
    "anterior", "antes", "apenas", "aproximadamente", "aquel", "aquellas", "aquellos", "aqui",
    "aquí", "arriba", "aseguró", "así", "atras", "aunque", "ayer", "añadió", "aún", "bajo",
    "bastante", "bien", "buen", "buena", "buenas", "bueno", "buenos", "cada", "casi", "cerca",
    "cierta", "ciertas", "cierto", "ciertos", "cinco", "comentó", "como", "con", "conocer",
    "conseguimos", "conseguir", "considera", "consideró", "consigo", "consigue", "consiguen",
    "consigues", "contra", "cosas", "creo", "cual", "cuales", "cualquier", "cuando", "cuanto",
    "cuatro", "cuenta", "cómo", "da", "dado", "dan", "dar", "de", "debe", "deben", "debido",
    "decir", "dejó", "del", "demás", "dentro", "desde", "después", "dice", "dicen", "dicho",
    "dieron", "diferente", "diferentes", "dijeron", "dijo", "dio", "donde", "dos", "durante",
    "e", "ejemplo", "el", "ella", "ellas", "ello", "ellos", "embargo", "empleais", "emplean",
    "emplear", "empleas", "empleo", "en", "encima", "encuentra", "entonces", "entre", "era",
    "erais", "eramos", "eran", "eras", "eres", "es", "esa", "esas", "ese", "eso", "esos", "esta",
    "estaba", "estabais", "estaban", "estabas", "estad", "estada", "estadas", "estado", "estados",
    "estais", "estamos", "estan", "estando", "estar", "estaremos", "estará", "estarán", "estarás",
    "estaré", "estaréis", "estaría", "estaríais", "estaríamos", "estarían", "estarías", "estas",
    "este", "estemos", "esto", "estos", "estoy", "estuve", "estuviera", "estuvierais", "estuvieran",
    "estuvieras", "estuvieron", "estuviese", "estuvieseis", "estuviesen", "estuvieses", "estuvimos",
    "estuviste", "estuvisteis", "estuviéramos", "estuviésemos", "estuvo", "está", "estábamos",
    "estáis", "están", "estás", "esté", "estéis", "estén", "estés", "ex", "existe", "existen",
    "explicó", "expresó", "fin", "fue", "fuera", "fuerais", "fueran", "fueras", "fueron", "fuese",
    "fueseis", "fuesen", "fueses", "fui", "fuimos", "fuiste", "fuisteis", "fuéramos", "fuésemos",
    "gran", "grandes", "gueno", "ha", "haber", "habida", "habidas", "habido", "habidos", "habiendo",
    "habremos", "habrá", "habrán", "habrás", "habré", "habréis", "habría", "habríais", "habríamos",
    "habrían", "habrías", "habéis", "había", "habíais", "habíamos", "habían", "habías", "hace",
    "haceis", "hacemos", "hacen", "hacer", "hacerlo", "haces", "hacia", "haciendo", "hago", "han",
    "has", "hasta", "hay", "haya", "hayamos", "hayan", "hayas", "hayáis", "he", "hecho", "hemos",
    "hicieron", "hizo", "hoy", "hube", "hubiera", "hubierais", "hubieran", "hubieras", "hubieron",
    "hubiese", "hubieseis", "hubiesen", "hubieses", "hubimos", "hubiste", "hubisteis", "hubiéramos",
    "hubiésemos", "hubo", "igual", "incluso", "indicó", "informó", "intenta", "intentais", "intentamos",
    "intentan", "intentar", "intentas", "intento", "ir", "junto", "la", "lado", "largo", "las", "le",
    "les", "llegó", "lleva", "llevar", "lo", "los", "luego", "lugar", "manera", "manifestó", "mayor",
    "me", "mediante", "mejor", "mencionó", "menos", "mi", "mientras", "mio", "mis", "misma", "mismas",
    "mismo", "mismos", "modo", "momento", "mucha", "muchas", "mucho", "muchos", "muy", "más", "mí",
    "mía", "mías", "mío", "míos", "nada", "nadie", "ni", "ninguna", "ningunas", "ninguno", "ningunos",
    "ningún", "no", "nos", "nosotras", "nosotros", "nuestra", "nuestras", "nuestro", "nuestros", "nueva",
    "nuevas", "nuevo", "nuevos", "nunca", "o", "ocho", "os", "otra", "otras", "otro", "otros", "para",
    "parece", "parte", "partir", "pasada", "pasado", "pero", "pesar", "poca", "pocas", "poco", "pocos",
    "podeis", "podemos", "poder", "podria", "podriais", "podriamos", "podrian", "podrias", "podrá",
    "podrán", "podría", "podrían", "poner", "por", "por qué", "porque", "posible", "primer", "primera",
    "primero", "primeros", "principalmente", "propia", "propias", "propio", "propios", "próximo", "próximos",
    "pudo", "pueda", "puede", "pueden", "puedo", "pues", "que", "quedó", "queremos", "quien", "quienes",
    "quiere", "quién", "qué", "realizado", "realizar", "realizó", "respecto", "sabe", "sabeis", "sabemos",
    "saben", "saber", "sabes", "se", "sea", "seamos", "sean", "seas", "segunda", "segundo", "según", "seis",
    "ser", "seremos", "será", "serán", "serás", "seré", "seréis", "sería", "seríais", "seríamos", "serían",
    "serías", "seáis", "señaló", "si", "sido", "siempre", "siendo", "siete", "sigue", "siguiente", "sin",
    "sino", "sobre", "sois", "sola", "solamente", "solas", "solo", "solos", "somos", "son", "soy", "su",
    "sus", "suya", "suyas", "suyo", "suyos", "sí", "sólo", "tal", "también", "tampoco", "tan", "tanto",
    "te", "tendremos", "tendrá", "tendrán", "tendrás", "tendré", "tendréis", "tendría", "tendríais",
    "tendríamos", "tendrían", "tendrías", "tened", "teneis", "tenemos", "tener", "tenga", "tengamos",
    "tengan", "tengas", "tengo", "tengáis", "tenida", "tenidas", "tenido", "tenidos", "teniendo",
    "tenéis", "tenía", "teníais", "teníamos", "tenían", "tenías", "tercera", "ti", "tiempo", "tiene",
    "tienen", "tienes", "toda", "todas", "todavía", "todo", "todos", "total", "trabaja", "trabajais",
    "trabajamos", "trabajan", "trabajar", "trabajas", "trabajo", "tras", "trata", "través", "tres",
    "tu", "tus", "tuve", "tuviera", "tuvierais", "tuvieran", "tuvieras", "tuvieron", "tuviese", "tuvieseis",
    "tuviesen", "tuvieses", "tuvimos", "tuviste", "tuvisteis", "tuviéramos", "tuviésemos", "tuvo", "tuya",
    "tuyas", "tuyo", "tuyos", "tú", "ultimo", "un", "una", "unas", "uno", "unos", "usa", "usais", "usamos",
    "usan", "usar", "usas", "uso", "usted", "va", "vais", "valor", "vamos", "van", "varias", "varios",
    "vaya", "veces", "ver", "verdad", "verdadera", "verdadero", "vez", "vosotras", "vosotros", "voy",
    "vuestra", "vuestras", "vuestro", "vuestros", "y", "ya", "yo", "él", "éramos", "ésta", "éstas",
    "éste", "éstos", "última", "últimas", "último", "últimos"]

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
    
    def stop_words(self, text):
        text = text.split()  # separamos el texto por palabras
        text = [word for word in text if word not in stopwords] # nueva lsta sin las stopwords
        return " ".join(text)

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
        text = self.lower_words(text) # convertimos el texto a minúsculas
        text = self.stop_words(text) # eliminamos las stop words
        text = self.remove_punctuation(text) # eliminamos los símbolos especiales
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
