
# AGA 0503 - Métodos Numéricos para Astronomia
# Professor Dr. Alex Carciofi
# Terceiro Exercício de Programação (EP3)

# 4) Implementar método de Chi^2 para ajuste de parábolas (3 pontos)

# Implemente uma subrotina que, dado um conjunto m de pontos (x, y), faça o ajuste de uma parábola aos pontos, usando o método dos mínimos quadrados, sem pesos, 
# usando a expressão: y = a+b*x+c*x**2. A rotina deve retornar valores de a, b e c. 

#Sugestão: leia esse código em full screen, para que todos comentários estejam organizados de forma mais apropriada.

#Bibliotecas:

import numpy as np
import matplotlib.pyplot as plt
import math
import pylab

""" ------------------------------------ Chi-quadrado --------------------------------------------------------------------------------------------------------- """
                                         # Faremos ajuste de chi-quadrado com funções de segundo grau.
                                         # Logo f_1(x) = 1, f_2(x) = x e f_3(x) = x**2
                                         # Noso input deve ser uma lista de valores x e y

def f_1(x):                              # Defino f_1(x) em uma função separada, por conveniência. 
    return 1

def f_2(x):                              # Defino f_2(x) em uma função separada, por conveniência.
    return x

def f_3(x):                              # Defino f_3(x) em uma função separada, por conveniência.
    return x**2

def chiq (x, y):                         # x e y são listas de valores tal que y = y(x) para cada par ordenado.

    m = len(x)                           # Defino len(x) = m para ficar na notação do enunciado
    if m != len(y):                      # Se o tamanhos das listas inputadas é diferente, melhor alertar o usuário e pedir para inputar de novo ao invés de ignorar
                                         # certos valores, eu acredito. 
        print ("Sistema mal condicionado, tamanhos de listas diferentes para x e y(x)")
        return False
    else:
        pass

    f1 = []                              # Define-se f1 uma coleção de f_1(x) para cada x da lista inputada  
    for i in range (m):
        f1.append(f_1(x[i]))
        
    f2 = []                              # Define-se f2 uma coleção de f_2(x) para cada x da lista inputada
    for i in range (m):
        f2.append(f_2(x[i]))
        
    f3 = []                              # Define-se f3 uma coleção de f_3(x) para cada x da lista inputada
    for i in range (m):
        f3.append(f_3(x[i]))

    F = [f1, f2, f3]                     # Define-se F uma lista dos f1, f2 e f3. 
    
    F_ok = []                            # F_ok é a matriz a ser inputada na algoritmo de Gauss (EP2) para resolução de equações lineares
    for i in range (3):                  # Precisamos de 3 linhas de equações lineares, já que estamos ajustando para polinômios de grau 2
        add = []
        for j in range (3):              # Agora para cada elemento F_ok[i][j] da matriz aplica-se as regras do sistema exposto na página 102 da apostila
                                         # tal que F_ok[i][j] = Soma de 0 a m-1 de F[i] * F[j] (para isso usamos a função multiply do Numpy, que é a mesma coisa que
                                         # multiplicar arrays do Python, sem ter que transformar a classe). 
            valor = sum(np.multiply(F[i], F[j]))
            add.append(valor)
        F_ok.append(add)

    sol = []                             # sol é a matriz de soluções das equações lineares a ser inputada no algoritmo de Gauss. 
    for i in range (3):
        valor = sum(np.multiply(y, F[i]))# Uso a mesma estratégia do F_ok, mas agora vai ficar no formato sol[i] = Soma de 0 a m-1 de y[i]*F[i]
        sol.append(valor)

    R = gauss(F_ok, sol)                 # Aplica-se Gauss tal que y = a + b*x + c*x**2
    R_1 = R[0]                           # R_1 é o primeiro coeficiente (a), termo independente
    R_2 = R[1]                           # R_2 é o segundo coeficiente (b), termo que multiplica x
    R_3 = R[2]                           # R_3 é o terceiro coeficiente (c), termo que multiplica x**2

                                         #### A partir desse ponto só falta plotar e printar pro usuário o resultado. ###

    def func(x):                         # Define-se a função polinomial de segundo grau utilizando os coeficientes acima explicitados.
        return R_1 + R_2 * x + R_3 * x * x
    x_ordenado = ordena(x)               # Só ordeno os valores pra, na hora de plotar, os pontos serem criados desde o menor valor até o maior, ao invés de qualquer
                                         # intervalo aleatório de um input desordenado. 
    x_func = np.linspace(x_ordenado[0], x_ordenado[m-1])
                                         # Calcula-se uma coleção de x_func que são calculados no intervalo [x[0];x[m]] aplicados ao polinômio encontrado em func.

    print("Os coeficientes encontrado no ajuste são: a =",R_1 , ", b = ",R_2 ,"e c =",R_3 )
                                        
    plt.scatter (x, y, c = "black")      # Só plotar!! 
    plt.plot(x_func, func(x_func), "r--")
    plt.xlabel("x")
    plt.ylabel("y (x)")
    plt.title("Ajuste por chi-quadrado")
    plt.gca().legend(('Ajuste','Dados'))
    plt.show()

    return R

""" ----------------------------------------------------------------------------------------------------------------------------------------------------------- """

#### USANDO GAUSS DO EP2 ###

""" ------------------------------------ Calcula determinante de matriz M ------------------------------------------------------------------------------------- """

def det(M):                              #Como o cálculo do determinante não era objeto do EP, achei razoável usar a função pronta do Numpy.

  Det = np.linalg.det(M)

  return(Det)
  
""" ------------------------------------ Função de normalizar matriz  ----------------------------------------------------------------------------------------- """

def normal (M,n):                       #Para normalizarmos, faz-se a normalização de cada vetor elemento da matriz de entrada M.
                                        # ||vetor|| = sqrt(v1^2 + v2^2 + ... + vn^2), tal que v1, v2, ..., vn são os n elementos do vetor. 
  m = len(M[0])                         #nº de colunas de M.
  for i in range (n):
    norma2 = 0                          #Aqui inicializamos a variável que guarda o valor do quadrado da norma. 
    for j in range (m):
      norma2 = norma2 + M[i][j]**2      #Atualiza-se, a cada iteração, o valor do quadrado da norma (vamos somando os quadrados dos elementos).
      norma = norma2 ** 0.5             #Norma é raíz da Norma^2. 
    for k in range (m):
      M[i][k] = M[i][k] / normal        #Atualizam-se os valores da matriz M com aqueles referentes à normalização da mesma. 

  return(M)

""" ------------------------------------ Função de Pivotamento Parcial ---------------------------------------------------------------------------------------- """

def pivot(M,n):                         #Função de Pivotamento Parcial (Aqui eu coloquei o n = "número de linhas da matriz"
                                        #como uma entrada porque estava tendo problemas de identação).
  for i in range(n):
   for j in range(i+1,n):               #Começamos o "for" do i+1 já que, evidentemente, nao precisamos comparar um valor com ele mesmo.
     if abs(M[j][i]) > abs(M[i][i]):    #Aqui, queremos o maior valor absoluto possível na primeira posição da matriz
        M[i], M[j] = M[j],M[i]          #então a cada iteração compara-se o primeiro valor de uma linha com o primeiro valor da de baixo
     else:                              #e realizam-se as trocas necessárias, colocando as linhas com os maiores primeiros valores para cima. 
        pass

  return(M)                             #Retorna matriz pivotada.

""" ------------------------------------ Função de Eliminação ------------------------------------------------------------------------------------------------- """

def elim(M,n):                          #Função de Eliminação (Aqui, de novo, eu coloquei o n = "número de linhas da matriz"
                                        #como uma entrada porque estava tendo problemas de identação).
  for i in range(n):
   for j in range(i+1,n):               #Começamos o "for" do i+1 já que, evidentemente, nao precisamos comparar um valor com ele mesmo.
    fator = float(M[j][i]) / M[i][i]    #Avaliamos o fator pelo qual devemos multiplicar a linha avaliada para que ela elimine o primeiro elemento da próxima.
    for k in range(i, n+1):
      if fator != 0:                    #Se o fato é nulo, não precisamos fazer nada.
        M[j][k] -= ( fator * M[i][k] )  #Realizamos as subtrações de uma linha pela outra.
      else:
        pass
  return(M)

""" ------------------------------------ Função de Gauss propriamente dita ------------------------------------------------------------------------------------- """

def gauss(A,b):

  if len(b) > len(A):                   #Nessa região do código, ajustamos a quantidade de linhas da matriz A com a quantidade de elementos da matriz b
      x = len(b) - len(A)               #já que, independentemente do sistema ter reposta ou não, devemos operar com um número de equações igual à quantidade
      for i in range (x):               #de respostas disponíveis, evidentemente. 
          b.pop()
  elif len(b) < len(A):
      x = len(A) - len(b)
      for i in range (x):
          A.pop()
  else:                                 #Caso o número de repostas seja igual ao número de equações, não precisamos reduzir o número de elementos em A ou em b
      pass                              #isto é, só falta avaliar se o número de equações que sobram é suficiente para resolver cada uma das incógnitas

                                        ####### Agora, precisamos igualar o número de colunas ao número de linhas na matriz A. #######
    
  if len(A) > len(A[0]):                #Nesse caso, temos muitas equações para poucas incógnitas. Isto é, há equações desnecessárias e as removemos.
      x = len(A) - len(A[0])
      for i in range (x):
          A.pop()
  elif len(A) < len(A[0]):              #Nesse caso, temos várias incógnitas, mas não tantas equações. Logo, é impossível encontrar solução. 
      print("Sistema impossível.")
      return False
  elif 0 < det(A) < 1:
    print("Sistema mal condicionado (0 < det < 1).")
    return False
  for i in range(len(A)):               #Aqui eu vejo se não tem linha de elementos nulos.
    fator = 0
    for j in range (len(A[0])):
      fator = fator + A[i][j]
    if fator == 0:
      print("Sistema mal condicionado (linha de elementos nulos na matriz).")  
      return False
  else:                                 #Caso o número de linhas e colunas já seja igual, podemos seguir em frente. 
      pass

                                        #Agora começamos a fazer as operações de fato, apó garantirmos que o número de elementos de b é igual ao de A e que os
                                        #números de linhas e colunas de A são iguais.
      
  n = len(A)                            # nº linhas matriz A.
  M = A                                 # Cria-se uma cópia de A, por conveniência.

  for i in range(n):                    #Cria-se a matriz aumentada, por conveniência.
   M[i].append(b[i])

  for i in range(n):                    #Realizam-se as operações de pivotamento ("pivot") e eliminação ("elim") cabíveis.
   M = pivot(M,n)
   M = elim(M,n)
                                        #Nesse ponto, já temos a matriz aumentada totalmente ajustada para que sejam descobertos os valores x_1, x_2, ..., x_n
  x = solver(M,n)                       #e para esse desafio vamos calculando os valores da matriz x (resposta) de baixo para cima de M.

  return(x)

""" ------------------------------------ Função que calcula x a partir da matriz aumentada triangularizada M ---------------------------------------------------- """

def solver(M,n):

  m = n-1                               #Defino a variável m como n-1, por conveniência, já que vamos usar a posição n-1 várias vezes,
                                        #dado que o Python começa a contagem de posições em vetores do zero.
  x = []                                #Inicio um vetor x vazio, a fim de que eu possa ir colecionando as respostas do sistema aqui. 
    
  for i in range(n):                    #Preencho o x com zeros, já que este é o elemento nulo da soma.  
    x.append(0)

  x[m] = float(M[m][n]) / M[m][m]       #Aqui, pegamos a matriz triangularizada, vide função "pivot", e usamos o valor acumulado na última linha para encontrar
                                        #a primeira incógnita

  for i in range(m,-1,-1):              #Agora é só ir fazendo as operações em sequência, de baixo para cima, na matriz triangularizada, baseando-se
                                        #no fato de que conhecemos, já, um dos valores da matriz resposta x (por isso o passo -1 no "for").
    fator = 0                           #Inicia-se um fator nulo, para que acumulemos os multiplicadores, sempre isolando a incógnita ainda desconhecida.
    for j in range(i+1,n):
      fator = fator + float(M[i][j]) * x[j] 
    x[i] = float(M[i][n] - fator) / M[i][i]

  return (x)

""" ------------------------------------ Bubble Sort (EP1) ------------------------------------------------------------------------------------------------------ """

# Ordena uma lista de valores para uma sequência crescente #
# Copiei essa rotina do EP1 só pra poder ficar colocando qualquer lista #

def ordena (lista):

    array = lista[:]
                
    # Agora, para ordenar o array, podemos usar algoritmo estilo BubbleSort: 
    N = len(array)

    for i in range (0, N):

            for j in range (0, N-1):

                    if array[j] > array[j+1]:
                            aux = array[j+1]
                            array[j+1] = array[j]
                            array[j] = aux

# Ao fim da subrotina, ou função, retorna-se o Array organizado e o número de passos foi contabilizado.

    return array

""" ------------------------------------------------------------------------------------------------------------------------------------------------------------- """
