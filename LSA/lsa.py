import numpy as np

# simulamos los valores de una matriz término-documento
a = np.random.randint(0, 5, (5, 10))
# conjunto de 10 documentos de texto y 5 dimensiones
print("Matriz Término-Documento (A):\n", a,"\n\n") 

# * Singular Value Decomposition
# 1. calculamos AA^T
a_t = a.T
aa_t = np.dot(a,a_t)
print(aa_t)