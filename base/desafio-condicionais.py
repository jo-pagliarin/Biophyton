sequencias = {
    'seq_A' : "LRSSSQNSSDKLVAHVVANHQVEEQLEWLSQRANALLANGMDLKDNQLVVLADGLYLVYSQVLFKGQGCLDYVLLTHTVSLRSSSDK", 
    'seq_B' : "KPAAHLIGDPSKQNSLLWRANTDRAFLQDGFSLSNNSLLVPTSGIYFVYSQVVFSGKAYSPKATSSPLYLAHEVQLFSS",
    'seq_C' : "CPQGKYIHPQNNSICCTKCHKGTYLYNDCPGPGQDTDCRECESGSFTASENHLRHCLSCSKCRKEMGQVEISSCTVDRDTVCGCR",
    'seq_D' : "LIGDSKQNSLLWRANTDRAFLQDGFSLSNNSLLVTSGIYFVYSQVVFSGKAYSK"
    
}

# EXERCÍCIO 1
def firstPrint(sequencias):
    for sequencia in sequencias:
        if(len(sequencias[sequencia]) >= 80):
            print(sequencias[sequencia])
        
# firstPrint(sequencias)

# EXERCÍCIO 2
def secondPrint(sequencias):
    soma = 0
    for sequencia in sequencias:
        soma = soma + len(sequencias[sequencia])
    media = soma/3
    for sequencia in sequencias:
        if(len(sequencias[sequencia]) > media): 
            print(sequencias[sequencia])

# secondPrint(sequencias)

# EXERCÍCIO 3
def thirdPrint(sequencias): 
    for sequencia in sequencias:
        if sequencias[sequencia].find("P") == -1:
            if sequencias[sequencia].find("H") != -1:
                print(sequencia)
    
# thirdPrint(sequencias)

# EXERCÍCIO 5
def ordenaTamanho(sequencias):
    tam = []
    for sequencia in sequencias:
        tam.append(len(sequencias[sequencia]))
    tam = sorted(tam)
    for i in range (len(tam)):
        for sequencia in sequencias:
            if tam[i] == len(sequencias[sequencia]):
                print(sequencia)
            
ordenaTamanho(sequencias)