
# AGA 0503 - Métodos Numéricos para Astronomia
# Professor Dr. Alex Carciofi
# Segundo Exercício de Programação (EP2)

# 1) Método de Gauss (3 pontos)

# Comentários importantes:

#No Método de Eliminação de Gauss, o pivô é o primeiro elemento da linha que
#está sendo usada para eliminar termos das demais.

#Em casos nos quais o pivô é muito pequeno, podem acontecer erros graves de
#arredondamento. Logo, utiliza-se o método do pivotamento parcial, no qual
#trocamos as linhas entre si de tal sorte que o primeiro elemento da primeiro
#linha seja o de maior valor posivel. 

#Sugere-se que sejam implementadas duas subrotinas, uma para o cálculo da
#eliminação e outra para a substituição para trás, usando o esquema de
#armazenar os multiplicadores e os pivotamentos feitos.

#Temos sistemas de equações da forma A.x = b.

#Sugestão: leia esse código em full screen, para que todos comentários estejam organizados de forma mais apropriada.

#Bibliotecas:

import numpy as np

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
  for i in range(len(A)):              #Aqui eu vejo se não tem linha de elementos nulos.
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

""" ------------------------------------------------------------------------------------------------------------------------------------------------------------- """












    
