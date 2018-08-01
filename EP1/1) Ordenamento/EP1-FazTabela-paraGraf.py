
# AGA 0503 - Métodos Numéricos para Astronomia
# Professor Dr. Alex Carciofi
# Primeiro Exercício de Programação (EP1)


# 1) Ordenamento de um conjunto de dados (2 pontos)

# bibliotecas usadas
from random import *
import math

x_0 = 0
x_N = 10
final = []

for N in range (10, 105, 5):
	array = [] 
	Npassos = 0 #contador de passos	

# o trecho de código abaixo gera um array de dimensão N preenchido com os números pseudo-aleatórios

	for j in range (0, N): 
		rand = uniform (x_0, x_N)
		array.append (rand)
		
	# Agora, para ordenar o array, podemos usar algoritmo estilo BubbleSort: 

	for x in range (0, N):
		Npassos = Npassos + 1
		for y in range (0, N-1):
			Npassos = Npassos + 1
			if array[y] > array[y+1]:
				aux = array[y+1]
				array[y+1] = array[y]
				array[y] = aux

	N_Np = [N, Npassos]
				
	final.append(N_Np)
