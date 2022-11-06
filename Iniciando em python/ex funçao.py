def velocidade_media(distancia,tempo):
    velocidade = distancia/tempo
    return velocidade

# distância em metros e tempo em segundos

velocidade = velocidade_media(int(input("Qual a distância percorrida?")), int(input("Qual o tempo percorrido?")))

print("A velocidade média é igual a {}" .format(velocidade))



