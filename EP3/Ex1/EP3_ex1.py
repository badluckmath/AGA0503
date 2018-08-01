
# AGA 0503 - Métodos Numéricos para Astronomia
# Professor Dr. Alex Carciofi
# Terceiro Exercício de Programação (EP3)

# 1) Procurando um valor em uma tabela (2 pontos)

#Sugestão: leia esse código em full screen, para que todos comentários estejam organizados de forma mais apropriada.

#Bibliotecas:

import numpy as np
import matplotlib.pyplot as plt
import math

""" ------------------------------------ Bubble Sort ----------------------------------------------------------------------------------------------------------- """

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

""" ------------------------------------ Bissecção ------------------------------------------------------------------------------------------------------------- """

def bis(lista, x):                              #Recebe uma lista qualquer, previamente ordenada, e devolve a posição na qual o valor x se encontra

                                                # Aqui eu pensei em chamar a função de ordenar lista, mas como o exercício falava explicitamente que essa rotina
                                                # já recebia uma lista ordenada, acabei não fazendo. 
                
    array = lista[:]                            # Crio uma lista ordenada dos valores da lista de entrada
    array0 = array[:]
    N = len(array)                              # Variável que representa o tamanho da lista
    x_1 = array[0]                              # Registra-se o primeiro valor da lista (menor valor)
    x_n = array[N-1]                            # Registra-se o primeiro valor da lista (maior valor)

    if x < x_1:
        return 0
    if x > x_n:
        return N 

    while len(array) > 1:                       # Aqui eu usei while pra fazer a rotina enquanto o tamanho do array for maior que 1
        pos = len(array) // 2                   # Olhamos para o valor na posição do meio da lista
        if array[pos] < x:      
            array = array[pos:]                 # Se o valor nessa posição é menor que aquele desejado, jogamos fora a primeira metade da lista 
        elif array[pos] > x:
            array = array[:pos]                 # Se o valor nessa posição é maior que aquele desejado, jogamos fora a segunda metade da lista 
        else:
            for i in range (len(lista)):        # Se o valor nessa posição é igual àquele desejado, é só retornar essa posição. 
                if array[pos] == lista[i]:      # Para isso, como eu já sei que o valor desejado está contido na lista, eu busco por ele e registro a posição. 
                    return i + 1                # Aqui é i+1 já que a contagem do python começa no zero para as posições nas listas. 
                else:
                    pass
                    
    difer = []                                 # Lista de diferenças entre os valores da lista e o x desejado. 
    for i in range (len(lista)):               # Aqui a gente precisa fazer algo pra pegar o valor mais próximo daquele desejado, já que verificou-se que, na lista,
                                               # não tem um valor igualzinho. 
        dif = abs(lista[i] - x)                # Para isso, vou verificando a diferença entre cada elemento da lista e o x desejado e registro tais diferenças
        difer.append(dif)                      # numa lita de diferenças tal que len(difer) = len(lista). Daí é só procurar o mínimo dessas diferenças e retornar
                                               # a posição na qual ele se encontra. 
    for i in range (len(difer)):
        if min(difer) == difer[i]:
            return i + 1












    
