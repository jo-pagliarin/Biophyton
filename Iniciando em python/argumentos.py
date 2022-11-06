def teste(arg,	*args):
    print('primeiro	argumento	normal:	{}'.format(arg))
    for arg in args:
        print('outro	argumento:	{}'.format(arg))


teste('python',	'é',	'muito',	'legal')

lista = ["é", "muito", "legal"]
# tupla = ("é", "muito", "legal)
teste('python',	*lista)
