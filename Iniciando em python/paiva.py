import numpy as np

A = "agtcatc"
B = "ucaguag"

Matriz = []
Matriz.append(list(A.upper()))
Matriz.append(list(B.upper()))

print(np.matrix(Matriz))

