import numpy as np

# Pega as quantidades de dezenas e jogos
qtdD = input("Digite a quantidade de dezenas: ")
qtdJ = input("Digite a quantidade de jogos: ")

# Se for vazio a quantidade de dezenas, serão 6 dezenas e,
# se for vazio a quantidade de jogos, serão 10 jogos
if qtdD == '':
    qtdD = 6
if qtdJ == '':
    qtdJ = 10

# Todas as dezenas que um jogo pode ter.
todasDezenas = list(np.arange(0,60))


def geraJogo(dezenas):
    '''
    Gera jogo não repetitivo entre suas dezenas
    :param dezenas: Recebe quantas dezenas deve ter no jogo
    :return: lista contendo as dezenas do jogo
    '''
    jogo = []
    while len(jogo) != dezenas:
        numero = np.random.randint(0, 59)

        # Condição para que não haja repetição nas dezenas do jogo
        if numero not in jogo:
            jogo.append(numero)

            # Condição que vai auxiliar depois para verificar quais dezenas não foram escolhidas nos jogos
            if numero in todasDezenas:
                todasDezenas.remove(numero)

    return jogo

# Cria a lista com os jogos
listaJogos=[]
for i in range(0, int(qtdJ)):
    jogo = geraJogo((int(qtdD)))
    listaJogos.append(jogo)

# Vai conter todos os números que foram repetidos entre os jogos
numerosRepetidos = []

# Vai conter quais dezenas foram repetidos para cada par de jogos
numerosRepetidos2 = {}

# Verifica se tem jogo repetitivo
for jogo1 in range(0,len(listaJogos)-1):
    for jogo2 in range(jogo1+1,len(listaJogos)):
        # Vai adicionando numeros repetidos entre os jogos
        if len(set(listaJogos[jogo1]).intersection(listaJogos[jogo2])):
            numerosRepetidos.extend(list(set(listaJogos[jogo1]).intersection(listaJogos[jogo2])))
            numerosRepetidos2[str(jogo1+1)+" e "+ str(jogo2+1)] = list(set(listaJogos[jogo1]).intersection(listaJogos[jogo2]))

        # Compara entre dois jogos ordenados se são iguais, fica no laço até eles serem diferentes
        while len(set(listaJogos[jogo1]).intersection(listaJogos[jogo2])) == qtdD:
            jogo = geraJogo((int(qtdD)))
            listaJogos[jogo2]=jogo

# Saidas
print("Lista de jogos com as dezenas ordenadas")
for jogo in range(0,len(listaJogos)):
    print("Jogo", jogo+1, ":", sorted(listaJogos[jogo]))

print("\nResumo de repetições de dezenas entre os jogos.")
print(sorted(set(numerosRepetidos)),"\n")
for key, value in numerosRepetidos2.items():
    print("Jogos ",key,"tem o(s) seguinte(s) número(s) repetido(s): ",sorted(value))

print("\nResumo dos números que não foram selecionados entre os jogos elaborados.")
print(todasDezenas)