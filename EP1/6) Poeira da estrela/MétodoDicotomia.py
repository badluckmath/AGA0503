
# AGA 0503 - Métodos Numéricos para Astronomia
# Professor Dr. Alex Carciofi
# Primeiro Exercício de Programação (EP1)

# bibliotecas usadas
import math
import numpy as np
import matplotlib.pyplot as plt

# there is only one root
def fn(x):
    return x**2 +x -20 

# Método da Bissecção ou da Dicotomia
def root( f, a, b, epsilon ):
    array = [[0,a,b, ( a + b ) / 2.0 , abs(b-a)/2 ]]
    f_a, f_b = f(a), f(b)

#Precisa-se garantir que há troca de sinal entre os valores para a função analizada nas bordas do intervalo inicial ##
    if f_a * f_b > 0:
        
        x = np.arange(10*a, 10*b, 0.1)  # Ajustando coordenadas no eixo x #
        y = f(x)                        # Ajustando coordenadas no eixo y #

        plt.plot(x, y)                  # Plota-se a função com intervalor 10 * [a,b] para que o usuário verifique um outro possível intervalo
        plt.show()
        raise Exception('Sem troca de sinal, bissecção não é possível')   ## Caso não aconteça a troca de sinal, chama-se um alerta de Erro ##

    while abs(b - a) > 2 * epsilon :
        i = 0
        valores = []                   # Para problema 3 da lista #
        x_m = ( a + b ) / 2.0
        f_x = f(x_m)
        if f_x * f_a > 0:
            a = x_m
        else:
            b = x_m
        e = abs(b-a)/2         ### Erro associado ### 
        i = i + 1
        valores.append(i)                  # Para problema 3 da lista #
        valores.append(a)                  # Para problema 3 da lista #
        valores.append(b)                  # Para problema 3 da lista #
        valores.append(( a + b ) / 2.0)    # Para problema 3 da lista #
        valores.append(e)                  # Para problema 3 da lista #
        array.append(valores)              # Para problema 3 da lista #

    print (array)
      
    return ( x_m , e )


