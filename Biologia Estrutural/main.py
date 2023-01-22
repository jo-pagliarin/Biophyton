import sys

def registraSaida():
    nomeArqEntrada = sys.argv[1]
    arqEntrada = open(nomeArqEntrada, "rt")
    arqSaida = open("saida.txt", "w")
    for l in arqEntrada:
        if l.find("ATOM", 0, 4) != -1:
            arqSaida.write(
                l[0:6] + 
                l[7:11] + "  " + 
                l[13:16] + " " + 
                l[17] + 
                l[18:20] + " " + 
                l[21:23] + " " + 
                l[23:26] + " " + 
                l[31:38] + " " + 
                l[39:46] + " " + 
                l[47:54] + "  " + 
                l[77:78])
            arqSaida.write("\n")
    arqEntrada.close()
    arqSaida.close

    
    
def criaDicionario():
    dicA =  {}
    dicB = {}
    nomeArqEntrada = sys.argv[1]
    arqEntrada = open(nomeArqEntrada, "rt")
    for l in arqEntrada:
        if l.find("ATOM", 0, 4) != -1:
            if l.find("A", 21, 23)!= -1:
                dicA = {'Serial': l[7:11],'Name': l[13:16], 'resName': l[17:20], 'chainID': l[21:23], 'resSeq': l[23:26], 'x':l[31:38], 'y': l[39:46], 'z': l[47:54], 'Element': l[77:78]}
            else:
                dicB = {'Serial': l[7:11],'Name': l[13:16], 'resName': l[17:20], 'chainID': l[21:23], 'resSeq': l[23:26], 'x':l[31:38], 'y': l[39:46], 'z': l[47:54], 'Element': l[77:78]}
    print(dicA['resName'])

    # for serial, name, resname, chainid, resseq, x, y, z, element in dicA.items():
    #     print(serial, name, resname, chainid, resseq, x, y, z, element)

registraSaida()
criaDicionario()