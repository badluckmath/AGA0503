
# AGA 0503 - Métodos Numéricos para Astronomia
# Professor Dr. Alex Carciofi
# Segundo Exercício de Programação (EP2)

# 1) O problema do círculo (2 pontos)

# Comentários importantes:

#No problema do círculo, há duas possibilidades de erro: o sistema pode estar mal condicionado, com pontos fornecidos APROXIMADAMENTE sobre uma mesma reta, ou
#o sistema pode não ter solução, com os pontos fornecido de fato sobre uma mesma reta (sem solução).

#Passo a serem seguidos:
#a) Construir a matrix 3x3 bem como o vetor de termos independentes;
#b) Normalizar a matriz;
#c) Calcular a equação da circunferência por Método de Gauss com Pivotamento Parcial (vide problema 1);
#d) Calcular o determinante dessa matriz e informar ao usuário se o sistema é mal condicionado, indeterminado ou bem condicionado.

#Sugestão: leia esse código em full screen, para que todos comentários estejam organizados de forma mais apropriada.

#Bibliotecas:

import numpy as np

""" ------------------------------------ Função "Circle" que amarra tudo e dá as respostas ao usuário       ---------------------------------------------------- """

def circle(x_1,y_1,x_2,y_2,x_3,y_3):

  A,b = matrix(x_1,y_1,x_2,y_2,x_3,y_3)  #Começamos com as matrizes A e b (vide função "matrix").
  n = len(A)
  M = A[:]
  X = det(M)
  
  if not check(x_1,y_1,x_2,y_2,x_3,y_3):
    print("Sistema impossível (todos os pontos pertencem a uma mesma reta).")
    return False
  elif 0 < X < 1:
    print("Sistema mal condicionado.")
    return False
  else:
    pass
  x = gauss(A,b)
  a = x[0]
  b = x[1]
  k = x[2]
  r = ( a**2 + b**2 - k )**0.5

  print("A equação dessa circunferência é do tipo (x-a)^2 + (y-b)^2 = r^2, tal que (a,b) são coordenadas do centro e r é o raio.")
  print("Para os dados fornecidos, (a,b) =",(a,b),"e r =",r,".")
  return ([a,b,r])
      

""" ------------------------------------ Calcula determinante de matriz M (d) ---------------------------------------------------------------------------------- """

def det(M):                              #Como o cálculo do determinante não era objeto principal do EP, achei razoável usar a função pronta do Numpy.

  Det = np.linalg.det(M)

  return(Det)

""" ------------------------------------ Checa se a circunferência é possível ---------------------------------------------------------------------------------- """

def check(x_1,y_1,x_2,y_2,x_3,y_3):
    coef1 = (y_2 - y_1) / (x_2 - x_1)    #Coeficiente linear de uma reta entre os pontos (x_1,y_1) e (x_2,y_2)
    coef2 = (y_2 - y_3) / (x_2 - x_3)    #Coeficiente linear de uma reta entre os pontos (x_3,y_3) e (x_2,y_2)
    if coef1 == coef2:
        return False
    else:
        return True
    
""" ------------------------------------ Função de construir matriz (a) ---------------------------------------------------------------------------------------- """

def matrix(x_1,y_1,x_2,y_2,x_3,y_3):    #Recebe-se do usuário os três pontos COPLANARES para formar o possível círculo.
                                        #Queremos construir algo para resolver no formato A.x = B, então vou devolver A e B pra próxima rotina.

                                        #Equação da circunferência: (x - a)^2 + (y - b)^2 = r^2, onde:
                                        #x e y são coordenadas de um ponto genérico da circunferência, a e b são coordenadas do centro da mesma e r é seu raio. 

    A = [[ 2*x_1 , 2*y_1 , -1 ],        #Matriz das somas das coornadas, vide página 62 da apostila, seção 5.2.2. 
         [ 2*x_2 , 2*y_2 , -1 ],
         [ 2*x_3 , 2*y_3 , -1 ]]

    B = [ x_1**2 + y_1**2 ,             #Matriz dos resultados das somas das coordenadas, vide página 62 da apostila, seção 5.2.2.
          x_2**2 + y_2**2 ,
          x_3**2 + y_3**2 ]

    return(A,B)

""" ------------------------------------ Resolução do problema 1, que utilizamos aqui (c)  -------------------------------------------------------------------- """

""" ------------------------------------ Função de normalizar matriz (b) -------------------------------------------------------------------------------------- """

def normal (M):                         #Para normalizarmos, faz-se a normalização de cada vetor elemento da matriz de entrada M.

  n = len(M)                            # ||vetor|| = sqrt(v1^2 + v2^2 + ... + vn^2), tal que v1, v2, ..., vn são os n elementos do vetor. 
  m = len(M[0])                         #nº de colunas de M.
  for i in range (n):
    norma2 = 0                          #Aqui inicializamos a variável que guarda o valor do quadrado da norma. 
    for j in range (m):
      norma2 = norma2 + M[i][j]**2      #Atualiza-se, a cada iteração, o valor do quadrado da norma (vamos somando os quadrados dos elementos).
      norma = norma2 ** 0.5             #Norma é raíz da Norma^2. 
    for k in range (m):
      M[i][k] = M[i][k] / norma         #Atualizam-se os valores da matriz M com aqueles referentes à normalização da mesma. 
  X = M[:]  
  return(X)

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
   
  for i in range(n): 
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
