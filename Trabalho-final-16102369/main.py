import biblioteca as bib
import timeit

# ---------------------------------------------------------------------------------------
# Etapa 1
# ---------------------------------------------------------------------------------------

# Inicialmente o programa chama uma função que junta todos os arquivos de tempo
# em um arquivo só
# dados = bib.juntaDados()

# Após juntar todos os dados ele calcula a média do tempo e retorna um vetor
# md = bib.calculaMedia(dados)

# Depois ele calcula o desvio padrão
# ds = bib.calculaDesvio(dados, md)

# Aqui ele passa a altura que o usuário deve preencher previamente, decidi
# deixar para alterar direto na main para nao perde tempo tendo que perguntar
# para o usuário
# al = [1.18, 1.38, 1.58, 1.99, 2.19]

# Aqui ele calcula os tempos(pontos) reais para as alturas utilizadas para o
# teste
# temp = bib.tempoReal(al, 9.81)

# Neste passo ele retorna  o arquivo dados-finais.txt no qual contém três colunas
# com altura tempo médio e desvio padrão respectivamente
# bib.escreveDados(al, md, ds)

# Por fim ele recebe todos esses dados e faz um gráfico de tempo x altura
# bib.criaGrafico(al, md, ds, temp)

# ---------------------------------------------------------------------------------------
# Etapa 2
# ---------------------------------------------------------------------------------------

# Iniciamos a parte do trabalho final pegando os dados reduzidos e colocando eles em uma
# matriz para que posteriormente possamos manipulá los
h, t, d = bib.leDadosReduzidos("dados-finais.txt")

# Através do método de mínimos quadrados para achar o coeficientes angular e linear com
# o menor erro possível
a, b = bib.ajustaReta(h, t)

# Aqui ele calcula os tempos(pontos) reais para as alturas utilizadas para o
# teste com gravidade de 9.81 m/s^2
temp = bib.tempoReal(h, 9.81)

# Encontra a gravidade amostral
g = bib.gAmostral(b)

# Aqui ele calcula os tempos(pontos) reais para as alturas utilizadas para o
# teste com gravidade amostral
pontos = bib.tempoReal(h, g)

# Por fim ele recebe todos esses dados e faz um gráfico de tempo x altura com g=9.81 m/s^2
# Por fim ele recebe todos esses dados e faz um gráfico de tempo x altura com g amostral
bib.criaGraficoFinal(h, t, d, temp, pontos)

# ---------------------------------------------------------------------------------------
# Opcional
# ---------------------------------------------------------------------------------------

# Essa função fica a critério do usuário utilizar ou não, ela calcula o tempo de
# execução do programa. Sendo que para funcionar é necessário apenas descomentar
# print('Tempo:', timeit.timeit('"-".join(str(n) for n in range(100))', number=10000))
