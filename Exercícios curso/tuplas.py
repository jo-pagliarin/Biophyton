tupla = ("A", "C", "D", "E", "F", "G","H", "I", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "Y")

# letra a 
print(len(tupla)) 
print(tupla)

# letra b 
print(f'', "S" in tupla)
print(tupla.index("S"))
print(tupla.count("S"))

# letra c 
tupla2 = ("P", "G", "N", "Y", "V","W")

# letra d 
tupla3 = tupla + tupla2
print(tupla3)

# letra e 
print(tupla3.count("G"))
print(tupla3.count("N"))
print(tupla3.count("C"))

# letra f
print(tupla3.index("N"))

# letra g
print(tupla3[len(tupla3) - 5:])
