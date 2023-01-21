# EXERCÍCÍO 1
# letra A
countAmino = {'1A8M': '471', '1TNR': '283', '2AZ5':'592', '1TNF': '471', '2TNF': '468', '2TUN': '942', '4TSV': '150', '5TSW': '900', '2E7A': '471', '6RMJ': '489'}
# letra B
print(countAmino['2TNF']) 
print(countAmino['2E7A']) 
# letra C
print(len(countAmino))
# letra D
print(list(countAmino.keys()))
# letra E
print(list(countAmino.values()))
# letra F
id = list(countAmino.keys())
residues = (list(countAmino.values()))
print(list(zip(id,residues))) # lista
print(dict(list(zip(id,residues)))) #dict
