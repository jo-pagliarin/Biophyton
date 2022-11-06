# EXERCÍCÍO 1
# letra A
str = "AAY66821.1, AAY66759.1, AAY66711.1, AAY66706.1, AAY66703.1, AAY66697.1,  AAY66696.1, AAY66682.1, AAY66647.1, AAY66625.1, AAY66623.1, AAY66620.1, AAY66619.1, AAY66616.1, AAY66609.1, AAY66607.1, AAY66586.1, AAY66564.1, AAY66562.1, AAY66561.1, AAY66558.1, AAY66544.1, AAY66542.1, AAY66539.1, AAY66538.1, AAY66537.1, AAY66536.1, AAY66512.1, AAY66496.1, AAM93627.1,  AAM93626.1, AAY66506.1, AAM93587.1, AAY66811.1, AAY66620.1, AAY66555.1, AAY66707.1, AAM93653.1, AAY66608.1, AAY66700.1, AAY66646.1, AAY66809.1,  AAK97814.1, AAK97810.1, AAY66594.1, AAY66685.1, AAY66571.1, AAY66865.1"

#removendo espaços (depois da vírgula) da string 
str = str.replace(" ", "")

#covertendo string pra vetor, sendo que cada elemento é quebrado pela vírgula
str = str.split(",")
print(str)

#tamanho do vetor 
print(len(str))

# letra B
# buscando Id's ==> tentar fazer função
# forma convencional
print("AAY66682.1" in str)
print("AAY66504.1" in str)

# letra C
elemento = str[10]
print(elemento)

# letra D
str[11] = "AAY66967.1" 
print(str)

# letra E
print(str[8])
str.remove(str[8])
print(str)

# EXERCÍCIO 2
# letra A
energia = [-695.9, -884.3, -658.2, -917.9, -799.8, -842.1, -618.6, -726.6, -652.6, -594.8, -536.1, -788.2, -772.1, -676.9, -600.2, -575, -575.3,-603.4, -659.6, -715.3,  -643.8, -703, -763.1, -712.1, -719, -574.2, -594.1, -700.3, -742.1, -621.9, -649.7, -663.3, -825.3, -849.3, -616.5, -675.1, -572.8,-624.2, -608, -615.3, -572.8, -665.3, -644.6,-788.9, -631.8, -707.4, -715.2, -728.2, -729, -642.1,  -567.8 , -596.5, -551.5, -735,  -805.5, -696.7, -617.9, -606.5, -658.8, -667.8,  -689.5, -728.4, -564, -725.8, -623.2, -637, -570.9, -646.6, -703.2, -722.3, -624.1, -655.4]

# letra C => retornando o melhor score ==> a menor energia
def melhorScore(energia):
    menor = 10000
    for i in range(len(energia)-1):
        if energia[i] < menor:
            menor = energia[i]
    return menor

print(melhorScore(energia))
del(energia[energia.index(-575)])
print(energia)


#ordenando crescentemente 
def ordenaCrescente(energia):
    for i in range(len(energia)-1):
        energia.sort()
    return energia

#ordenando decrescentemente
def ordenaDecrescente(energia):
    for i in range(len(energia)-1):
        energia.sort(reverse = True)
    return energia

print(ordenaCrescente(energia))
print(ordenaDecrescente(energia))