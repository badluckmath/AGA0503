
# AGA 0503 - Métodos Numéricos para Astronomia
# Professor Dr. Alex Carciofi
# Segundo Exercício de Programação (EP2)

# 3) Método de Gauss-Seidel (3 pontos)

# Comentários importantes:

#No Método de Gauss-Seidel do EP, importante notar que considera-se que o usuário irá fornece uma matriz A de NxN elementos e um vetor de termos independentes.

#a) Verificar se a matriz satisfaz o critério das linhas;
#b) Verificar se a matriz satisfaz o critério de Sassenfeld;
#c) Resolver o sistema por Gauss-Seidel com e < 10e-5;
#d) O programa deve ser capaz de resolver um sistema de n equações.

#Temos sistemas de equações da forma A.x = b.

#Sugestão: leia esse código em full screen, para que todos comentários estejam organizados de forma mais apropriada.

#Bibliotecas:

import numpy as np

""" ------------------------------------ Critério das linhas ------------------------------------------------------------------------------------------------ """

def linhas(M):

    A = M[:]                                                        #Cópia da matriz de entrada, conveniência (para não acontecer de alterar o valor no id de M)

    n = len(M)                                                      #nº elementos na matriz de entrada (nº linhas)
    m = len(M[0])                                                   #nº elementos no primeiro elemento da matriz de entrada (nº colunas)

    for i in range(n):
        for j in range(m):
            soma = 0
            if i == j:
                diag = A[i][j]                                      #Guardamos o valor da diagonal daquela linha
            else:
                soma = soma + abs(A[i][j])                          #Vamos somando os módulos dos valores dos elemento da linha i
            if abs(diag) < abs(soma) or diag == 0:                  #Verifica-se a condição de que a somatória dos valores absolutos dos elementos da linha 
                return False                                        #devem ser menores que o absoluto do elemento da diagonal associada e cada elemento da mesma
                                                                    #deve ser diferente de zero. 
    return True

""" ------------------------------------ Critério de Sassenfeld --------------------------------------------------------------------------------------------- """

def sassenfeld(M):

    A = M[:]                                                        #Cópia da matriz de entrada, conveniência (para não acontecer de alterar o valor no id de M)
    Betas = []                                                      #Matriz que acumula valores de Beta, pra depois avaliar se todas satisfazem max(Betas) < 1.  

    n = len(M)                                                      #nº elementos na matriz de entrada (nº linhas)
    m = len(M[0])                                                   #nº elementos no primeiro elemento da matriz de entrada (nº colunas)

    for i in range(n):
        beta = 0                                                    #Inicializa a variável beta, que vai apresentar o valor do mesmo em cada linha
        for j in range(m):
            if i != j:
                beta = beta + abs(A[i][j])                          #Conforme apostila, Beta é a soma dos módulos dos valores da linhas divididos pelo valor absoluto
        beta = beta / abs(A[i][i])                                  #do elemento da diagonal associado. 
        Betas.append(beta)                                          #Juntamos os Betas todo.     

    if max(Betas) > 1:                                              #Aqui checamos a hipótese.
        return False                                                #Retorna False pq, caso não role o Sassenfeld, não vai ter Gauss-Seidel 
    else:
        return True

""" ------------------------------------ Calcula por Gauss-Seidel ------------------------------------------------------------------------------------------- """

def seidel(M,B,e,x):
                                                                     
    if linhas(M) == False:                                          #Checamos o critério das linhas. 
        print("A matriz não passou no critério das linhas.")        #Se não passar no critério das linhas tem que continuar normal né, já que o Gauss-Seidel
    else:                                                           #só precisa passar pelo de Sassenfeld, menos restritivo. 
        pass

    if sassenfeld(M) == False:                                      #Checamos o critério das linhas.
        print("A matriz não passou no critério de Sassenfeld.")     #Aqui sim, se falhar o teste do Sassenfeld retorna False, pq não pode acontecer o Gaus-Seidel.
        return False
    else:
        pass

    n = len(M)                                                      #nº elementos na matriz de entrada (nº linhas)
    m = len(M[0])                                                   #nº elementos no primeiro elemento da matriz de entrada (nº colunas)

    erro = []                                                       #Inicializa-se a matriz que acumulará os erros de cada elemento, por conveniência. 
    for i in range(n):                                      
        erro.append(0)                                              #Inicializo com zeros pq eu sabia que assim não ia dar problema pra frente.
                                                                    
    X = x[:]                                                        #A matriz X (maiúsculo) (chute inicial) é fornecida pelo usuário. 
    if len(X) != len(B):
        print("Querido usuário, o nº de elementos de X (chute inicial) de entrada deve ser igual ao número de elementos da matriz com as respostas b.")

    comp = []                                                       #Inicializa-se a matriz que acumulará o valores das multiplicações de índices pelos 
    for i in range(n):                                              #valores de x_n que vão sendo atualizados, para comparar com o resultado de cada equação linear. 
        comp.append(0)

    A = M[:]                                                        #Cópia da matriz de entrada, conveniência (para não acontecer de alterar o valor no id de M)
    b = B[:]                                                        #Cópia da matriz resposta de entrada, conveniência (mesmo caso de cima)
        
    limite = 1000                                                   #Aqui coloquei ese limitador só pra não ficar iterando pra sempre caso tivesse algo estranho
    k = 0
    while k < limite:
        soma = 0
        k = k + 1                                                   #Então, aqui nesse primeiro "for" fiquei calculando valores de x[n], aí no próximo ia vendo erro. 
        for i in range(n):                                          #Assim foi o jeito que eu arranjei pra não dar problemas com os
            soma = 0 
            for j in range(m):
                if (j != i):
                    soma = soma + A[i][j] * x[j]               
            x[i] = (b[i] - soma)/A[i][i]
            #print("x["+str(i)+"]:"+str(x[i]))                      #Isso aqui ficaria printando os valores dos x[n], usei na verificação. 
        del erro[:]

        for i in range(n):                                          #Como no "for" de cima eu fiquei calculando x[n], agora poso calcular só os erros
            soma = 0
            for j in range(m):
                soma = soma + A[i][j] * x[j]
            comp[i] = soma
            check = abs(comp[i] - b[i])
            erro.append(check)                                      #Acúmulo de valores de "check", que verificam em cada elemeento da matriz a diferença entre 
        #print("Número da iteração:",k)                             #o x[n] multiplicado pelo índice menos o b[n] correspondente. 
        if all(i <= e for i in erro) == True:                       #Aqui, depois dos erros acumulados é só ver se todos satisfazem meu erro. 
            break

    return(x)
            


