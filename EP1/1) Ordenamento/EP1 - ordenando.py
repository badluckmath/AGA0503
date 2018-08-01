
# AGA 0503 - Métodos Numéricos para Astronomia
# Professor Dr. Alex Carciofi
# Primeiro Exercício de Programação (EP1)


# 1) Ordenamento de um conjunto de dados (2 pontos)

# bibliotecas usadas
from random import *
import math

def array (N, x_0 , x_N): # constrói um array de dimensão N e o preenche com números pseudo-aleatórios entre x_0 e x_N

        array = [] 
        Npassos = 0 #contador de passos 

# o trecho de código abaixo gera um array de dimensão N preenchido com os números pseudo-aleatórios

        for i in range (0, N): 
                rand = uniform (x_0, x_N)
                array.append (rand)
                
        #registra-se o valor do array ainda desorganizado
        array_0 = array[:]
                
        # Agora, para ordenar o array, podemos usar algoritmo estilo BubbleSort: 
  
        if N <= 1:
                return array
        if N > 1:
                for i in range (0, N):
                        Npassos = Npassos + 1
                        for j in range (0, N-1):
                                Npassos = Npassos + 1
                                if array[j] > array[j+1]:
                                        aux = array[j+1]
                                        array[j+1] = array[j]
                                        array[j] = aux

        print ("Para valores entre", x_0, "e", x_N, "temos:")
        print ()
        print ("Array desorganizado, formado por número pseudo-aleatórios:")
        print (array_0)
        print ()
        print ("Array organizado:")
        print (array)

# Ao fim da subrotina, ou função, retorna-se o Array organizado e o número de passos foi contabilizado.

        return array
