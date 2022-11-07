# EXERCÍCIO 1 obs: nao precisava de aspas
rmsd1 = {'1.9', '1.8', '5.7', '1.6',  '5.8', '1.7', '9.6', '5.9', '9.5', '6.5', '6.2', '1.1', '4.4', '3.5', '2.9', '4.7', '4.6', '5.2', '5.3'}
rmsd2 = {'4.7', '3.6', '6.2', '7.1', '7', '5.6', '5.7', '3.4', '3.3', '2.1', '3.8', '3.9', '5', '5.1', '1.9', '9.5', '1.0', '1.3', '5.4'}
rmsd3 = {'2.2', '3.3', '5.1', '3', '3.7', '9.1', '8.8', '8.5', '2', '4.1', '6.1', '4.9', '1.1', '0.5', '0.8', '3.2', '6.9', '9.3', '9.5'}

# letra A => a diferença entre conjuntos, em Python, é a mesma contida na teoria dos conjuntos, em Matemática
dif12 = rmsd1 - rmsd2
dif13 = rmsd1 - rmsd3
dif23 = rmsd2 - rmsd3

# letra B 
print(rmsd1.intersection(rmsd2))

# letra C => Insira todos os elementos do conjunto 2 e 3 no conjunto 1 
print(rmsd1.union(rmsd2, rmsd3))  # a união já remove as repetições 

# EXERCÍCIO 2
A = {3, 6, 9, 12, 15, 18, 21, 24, 28, 27} 
B = {2, 6, 8, 10, 14, 16, 18, 20, 22, 24} 
C = {2, 6, 10, 18, 20} 
D = {1, 30, 5, 11, 17, 16, 22, 26}

# letra A 
# Em matemática, dois conjuntos são ditos disjuntos se não tiverem nenhum elemento em comum.

# letra B e C
print(A.isdisjoint(D))
print(B.isdisjoint(D))
print(C.issubset(A))
print(C.issubset(B))

# letra D => Acrescente os elementos 18, 23, 25, 63 no conjunto D
D.update([18, 23, 25, 63])
print(D)

# EXEMPLO .clear()
# Z = {1, 3, 3, 34, 4}
# print(Z)
# Z.clear()
# print(Z)

#saída: 
# {1, 34, 3, 4}
# set()