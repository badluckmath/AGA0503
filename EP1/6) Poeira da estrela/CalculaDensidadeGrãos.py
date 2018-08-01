
# AGA 0503 - Métodos Numéricos para Astronomia
# Professor Dr. Alex Carciofi
# Primeiro Exercício de Programação (EP1)

# bibliotecas usadas
import math
import numpy as np
import matplotlib.pyplot as plt

### Incógnitas utilizadas, com temperaturas em KELVIN e distâncias em METROS ### Definidas por mim
h = 6.6e-34     # Constante de Planck
c = 3e+8        # Velocidade da luz no vácuo, em mícrons por segundo #
k = 1.38e-23    # Constante de boltzmann [k] = J/K #
Dsol = 1.4e+9   # Diâmetro do Sol # 
Rsol = Dsol / 2 # raio do Sol, em função de seu diâmetro conhecido, em metros #

### Incógnitas utilizadas, com temperaturas em KELVIN e distâncias em METROS ### fornecidas

R = 10 * Rsol       # Raio da estrela em função daquele do Sol #
Tef = 3e+3          # Temperatura da superfíce da estrela # 
Ri = 2e+2 * Rsol    # Raio interno de um anel de poeira  ao redor da estrela de Ramo Assintótico das Gigantes #
Re = 2e+3 * Rsol    # Raio externo de um anel de poeira  ao redor da estrela de Ramo Assintótico das Gigantes #
a = 2e-7            # Raio de um grão presumidamente esférico #     
Tpoeira = 8e+2      # Temperatura de cada grão de poeira #
epsilon = 1e-6      # critério de convergência do método !!! 
jk = 6e-1           # J-K é o índice de cor observado. Para J: wavelenght_J = 1.6 microns e para K: wavelenght_K = 2.2 microns #
lambda_k = 2.2e-6
lambda_j = 1.6e-6

## Criando constantes pertinentes ##

cte1 = (h*c)/k ## Essa vai dentro da exp na Eq. de Planck, cte1 = hc/k, relacionando cte Planck, cte Boltz e veloc. da luz ##

def blackbody ( wav , temp ):
        
        expoente = (h*c / (wav*k*temp))
        divisor = (wav**5) * (np.exp(expoente)-1.0) 
        blackbody = 2*h*(c**2) / divisor
        
        return blackbody

### Aqui eu implementei essa rotina pra sempre plotar os perfis de radiação de corponegro#
### tanto da estrela quanto do grão de poeira, pra saber se tá plausível.
range_lambda = np.arange(1e-7, 1e-5, 1e-9)

I_estrela = blackbody (range_lambda, 3000.)
plt.plot (range_lambda * 1e9, I_estrela, 'b-')
plt.suptitle('Função de Planck - estrela')
plt.xlabel(' Wavelength (nm) ', fontsize=14)
plt.ylabel(' Intensidade ', fontsize=14)

plt.show () #Revela função de corponegro calculada para estrela

I_poeira = blackbody (range_lambda, 800.)
plt.plot (range_lambda * 1e-9, I_poeira, 'k-')
plt.suptitle('Função de Planck - poeira')
plt.xlabel(' Wavelength (nm) ', fontsize=14)
plt.ylabel(' Intensidade ', fontsize=14)
plt.show () #Revela função de corponegro calculada para poeira

## Fim da subrotina de Plotagem ##

def function(cor, R, Re, Ri, Tef, Tpoeira, a, lambda_j, lambda_k ): 
        
        # a variável "cor" é o índice de Cor J-K #

        pi = math.pi

        v = 4/3 * pi * (Re ** 3 - Ri ** 3) #Volume da nuvem de poeira #

        Bj_estrela = blackbody (lambda_j, Tef)     #expressão para espectro de corponegro com temperatura da estrela e comprimento de onda j #
        Bk_estrela = blackbody (lambda_k, Tef)     #expressão para espectro de corponegro com temperatura da estrela e comprimento de onda k #
        Bj_poeira = blackbody (lambda_j, Tpoeira)  #expressão para espectro de corponegro com temperatura da poeira e comprimento de onda j #
        Bk_poeira = blackbody (lambda_k, Tpoeira)  #expressão para espectro de corponegro com temperatura da poeira e comprimento de onda k #

        d_j = R**2 * Bj_estrela                    # termo referente à luminosidade da estrela para comprimento de onda j #
        d_k = R**2 * Bk_estrela                    # termo referente à luminosidade da estrela para comprimento de onda k #
        D_j = v * a**2 * Bj_poeira                 # termo referente à luminosidade da poeira para comprimento de onda j #
        D_k = v * a**2 * Bk_poeira                 # termo referente à luminosidade da poeira para comprimento de onda k #

        def f(n):
                ### Queremos que seja devolvida uma FUNÇÃO de n ###
                return cor + 2.5 * np.log10( (d_j + D_j * n) / (d_k + D_k * n) )

        return f
                
# Método da Bissecção ou da Dicotomia para cálculo de raízes de função
def root( f, a, b, epsilon ):
    f_a, f_b = f(a), f(b)

#Precisa-se garantir que há troca de sinal entre os valores para a função analizada nas bordas do intervalo inicial ##
    if f_a * f_b > 0:

        raise Exception('Sem troca de sinal, bissecção não é possível')   ## Caso não aconteça a troca de sinal, chama-se um alerta de Erro ##

    while abs(b - a) > 2 * epsilon : # Loop enquanto o erro desejado não for atingido
        x_m = ( a + b ) / 2.0        # Posição média do intervalo
        f_x = f(x_m)                 # Cálculo do valor da função no ponto médio x_m
        if f_x * f_a > 0:            # Avalia-se, aqui, qual das metades queremos no desfazer
            a = x_m                  # Implementa-se o novo intervalo
        else:
            b = x_m                  # Implementa-se o novo intervalo

    e = abs(b-a)/2    ### Erro associado ###        
    return ( x_m , e )

### Agora, eu revelo ao usuário a solução para um erro de 0.0001. É possível testar com outros valores, mas já deixei printando
### a resposta do EP1 pra facilitar e não ter que ficar colocando os dados toda hora.

resultado = function (jk, R, Re, Ri, Tef , Tpoeira, a , lambda_j, lambda_k)
raiz = root (resultado, 0 , 1e+12, epsilon)
print ()
print ("Conseguimos!")
print ("Para os dados do problema do EP1, a densidade de grãos encontrada foi:" , "{:.2e}".format(raiz[0]), "grãos por metro cúbico" )
print ()

input('Pressione ENTER para sair.')
