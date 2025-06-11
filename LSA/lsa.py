import numpy as np
from scipy.linalg import svd

# * Simulamos los valores de una matriz término-documento
a = np.random.randint(0, 5, (5, 10)) # conjunto de 10 documentos de texto y 5 dimensiones
print("Matriz Término-Documento:\n", a,"\n") 

# * Singular Value Decomposition
U, singular, V_transpose = svd(a)
print("U —matriz de términos—:\n", U,"\n")
print("S —vector de valores singulares—:\n", singular,"\n")
print("V^{T} —matriz de documentos—:\n", V_transpose)