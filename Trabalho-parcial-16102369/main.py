import biblioteca as bib
#import timeit

# Inicialmente o programa chama uma função que junta todos os arquivos de tempo
# em um arquivo só
dados = bib.juntaDados()

# Após juntar todos os dados ele calcula a média do tempo e retorna um vetor
md = bib.calculaMedia(dados)

# Depois ele calcula o desvio padrão
ds = bib.calculaDesvio(dados, md)

# Aqui ele passa a altura que o usuário deve preencher previamente, decidi
# deixar para alterar direto na main para nao perde tempo tendo que perguntar
# para o usuário
al = [1.18, 1.38, 1.58, 1.99, 2.19]

# Aqui ele calcula os tempos(pontos) reais para as alturas utilizadas para o
# teste
temp = bib.tempoReal(al)

# Neste passo ele retorna  o arquivo dados-finais.txt no qual contém três colunas
# com altura tempo médio e desvio padrão respectivamente
bib.escreveDados(al, md, ds)

# Por fim ele recebe todos esses dados e faz um gráfico de tempo x altura
bib.criaGrafico(al, md, ds, temp)

# Essa função fica a critério do usuário utilizar ou não, ela calcula o tempo de
# execução do programa. Sendo que para funcionar é necessário apenas descomentar
# print('Tempo:', timeit.timeit('"-".join(str(n) for n in range(100))', number=10000))
