import numpy as np
import matplotlib.pyplot as plt
import os
import math

# ---------------------------------------------------------------------------------------
# Etapa 1
# ---------------------------------------------------------------------------------------


def calculaMedia(dados):
    """
    Calcula o valor médio de qualquer
    amostra de números, nesta aplicação
    calcula a média do tempo de queda


    Recebe:
    dados   => Dados provenientes de arquivo
    de texto, passando por forma de vetor


    Retorna:
    media (s)    => Valor médio da amostra
    """
    os.remove(os.getcwd() + "/temp.txt")
    media = 0
    vet = []
    for i in range(len(dados)):
        media += dados[i]
        if(((i + 1) % 5) == 0):
            vet.append(media / 5.0)
            media = 0
    return(vet)


def calculaDesvio(dados, md):
    """
    Calcula o desvio padrão de qualquer
    amostra de números, nesta aplicação
    calcula a desvio padrão do tempo de
    queda


    Recebe:
    dados  => Dados provenientes de arquivo
    de texto, passando por forma de vetor
    md   => Valor médio da amostra


    Retorna:
    desvio (s)  => Desvio padrão da amostra
    """
    desvio = 0
    vet = []
    j = 0
    for i in range(len(dados)):
        desvio += ((dados[i] - md[j]) * (dados[i] - md[j]))
        if(((i + 1) % 5) == 0):
            vet.append(np.sqrt(desvio / 5))
            desvio = 0
            j += 1
    return(vet)


def juntaDados():
    """
    Junta as cinco lista para fins de
    analise, se necessario


    Recebe: NADA


    Retorna:
    dados   => Um vetor com todos os intens da listas
    """
    diretorio = os.getcwd()
    with open("temp.txt", "w") as f:
        for temp in [diretorio + "/dados/dados1.txt", diretorio + "/dados/dados2.txt", diretorio + "/dados/dados3.txt", diretorio + "/dados/dados4.txt", diretorio + "/dados/dados5.txt"]:
            with open(temp, "r") as t:
                f.writelines(t)
    dados = np.loadtxt('temp.txt')
    return(dados)


def escreveDados(alturas, media, desvio):
    """
    Recebe os dados processos e retorna
    a altura, o tempo e o desvio padrão
    em um arquivo de texto


    Recebe:
    alturas (m)  => Rece as alturas passadas
    previamente pelo usuário
    media (s)   => A média do tempo de queda
    desvio (s)  => Recebe o desvio padrão de
    cada tempo


    Retorna:
    Cria um arquivo com os itens recebidos
    listados em colunas
    """
    f = open('dados-finais.txt', 'w')
    for i in range(5):
        # Altura em metros
        f.write(str(round(alturas[i], 2)))
        f.write(' ')
        # Média em segundos
        f.write(str(round(media[i], 2)))
        f.write(' ')
        # Desvio Padrão em segundos
        f.write(str(round(desvio[i], 2)))
        f.write('\n')
    f.close()


def tempoReal(alturas, g):
    """
    Gera os pontos de tempo segundo a
    formula t = sqrt(2*h/g)


    Recebe:
    alturas (m)  => Rece as alturas passadas
    previamente pelo usuário


    Retorna:
    temp    => Tempo real de queda do objeto
    """
    temp = []
    for i in range(len(alturas)):
        temp.append(np.sqrt(2 * alturas[i] / g))
    return(temp)


def criaGrafico(alturas, media, desvio, temp):
    """
    Gera os pontos de tempo segundo a
    formula t = sqrt(2*h/g)


    Recebe:
    alturas (m)  => Rece as alturas passadas
    previamente pelo usuário
    media (s)  => A média do tempo de queda
    desvio (s)  => Recebe o desvio padrão de
    cada tempo
    temp    => Tempo real de queda do objeto


    Retorna:
    Gráfico de altura x tempo com o desvio
    padrão e a reta de tempo real
    """
    plt.plot(np.array(alturas), temp, "r",
             label='Tempo real com '"$g = 9.81 m/s^2$")
    plt.errorbar(np.array(alturas), media, np.array(desvio), linestyle='None', marker='o',
                 label='Desvio padrão')
    plt.title('Gráfico - Tempo x Altura')
    plt.xlabel('Altura (m)')
    plt.ylabel('Tempo (s)')
    plt.margins(0.05)
    plt.grid()
    plt.legend(loc='lower right')
    plt.savefig('grafico.png')
    # plt.show()

# ---------------------------------------------------------------------------------------
# Etapa 2
# ---------------------------------------------------------------------------------------


def leDadosReduzidos(dadosReduzidos):
    """
    Recebe os dados reduzidos e retorna
    um vetor de float para análise


    Recebe:
    dadosReduzidos  => Arquivo de dados reduzidos


    Retorna:
    h  => Retorna um vetor de altura(m)
    t  => Retorna um vetor de média do tempo(s)
    d  => Retorna um vetor de desvio padrão(s)
    """

    h, t, d = np.loadtxt(dadosReduzidos, dtype='float', unpack=True)
    return(h, t, d)


def ajustaReta(h, t):
    """
    Recebe os dados amostrais de altura e
    tempo médio e aplica o método de mínimos
    quadrados para achar o melhor ajuste de
    reta com menor erro


    Recebe:
    h(m)  => A altura amostral
    t(s)  => A média do tempo de queda amostral


    Retorna:
    a  => Retorna o coeficiente angular
    b  => Retorna o coeficiente linear
    """

    lnx = 0
    lny = 0
    lnxy = 0
    lnxx = 0

    for i in range(len(h)):
        lnx += np.log(h[i])
        lny += np.log(t[i])
        lnxy += np.log(h[i]) * np.log(t[i])
        lnxx += np.log(h[i]) * np.log(h[i])

    a = ((len(h)) * lnxy - lnx * lny) / ((len(h)) * lnxx - (lnx * lnx))
    b = math.e ** ((lnxx * lny - lnxy * lnx) / ((len(h)) * lnxx - (lnx * lnx)))

    return(a, b)


def criaGraficoFinal(alturas, media, desvio, temp, p):
    """
    Gera os pontos de tempo segundo a
    formula t = sqrt(2*h/g)


    Recebe:
    alturas (m)  => Rece as alturas passadas
    previamente pelo usuário
    media (s)  => A média do tempo de queda
    desvio (s)  => Recebe o desvio padrão de
    cada tempo
    temp    => Tempo real de queda do objeto
    p => Postos do gráfico com gravidade
    encontrada através da analise


    Retorna:
    Gráfico de altura x tempo com o desvio
    padrão e a reta de tempo real
    """

    plt.plot(np.array(alturas), temp, "r", label="$g = 9.81 m/s^2$")
    plt.plot(np.array(alturas), p, "y", label="$g = 9.55 m/s^2$")
    plt.errorbar(np.array(alturas), media, np.array(desvio), linestyle='None', marker='o',
                 label='Dados')
    plt.title('Gráfico - Tempo x Altura')
    plt.xlabel('Altura (m)')
    plt.ylabel('Tempo (s)')
    plt.margins(0.05)
    plt.grid()
    plt.legend(loc='lower right')
    plt.savefig('grafico.png')
    # plt.show()


def gAmostral(b):
    """
    Recebe o coeficiente linear para achar
    a gravidade da amostra através da
    formula achada na análise da hipótese
    e^ln((2/g)^(1/2)) = e^b


    Recebe:
    b  => Recebe o coeficiente linear


    Retorna:
    (2 / float(b * b))  => Retorna a gravidade da amostra
    """

    return(2 / float(b * b))
