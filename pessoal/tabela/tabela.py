from random import randint
tabela = list()
rodadaJogo = dict()
rodada = list()
confronto = dict()
associacoes = list()
numerosSorteados = list()

def todosClubes(* clubes):
    for clube in clubes:
        associacoes.append(clube)

def construirRodada(clubes):
    totalClubes = len(clubes)
    jogosRodada = 0
    if totalClubes & 2 == 0:
        jogosRodada = totalClubes / 2
    else:
        jogosRodada = ( totalClubes / 2)- 1
    for r in range(1, int(totalClubes)):
        numerosSorteados.clear()
        for c in range(0, totalClubes):
            while True:
                numeroSorteado = randint(0, totalClubes - 1)
            
                if numeroSorteado not in numerosSorteados:
                    numerosSorteados.append(numeroSorteado)
                    break
        for numero in range(0, len(numerosSorteados) - 1, 2):
            confronto['casa'] = clubes[numerosSorteados[numero]]
            confronto['fora'] = clubes[numerosSorteados[numero - 1]]
            rodada.append(confronto.copy())
            confronto.clear()
            if len(rodada) == int(jogosRodada):
                rodadaJogo['rodada'] = r
                rodadaJogo['jogos'] = rodada[:]
                tabela.append(rodadaJogo.copy())
                rodadaJogo.clear()
                rodada.clear()
todosClubes('Gremio', 'Inter', 'Juventude', 'Caxias', 'Pelotas')
construirRodada(associacoes)
for rod in tabela:
    print(rod)  