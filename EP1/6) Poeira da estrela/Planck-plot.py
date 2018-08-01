
# AGA 0503 - Métodos Numéricos para Astronomia
# Professor Dr. Alex Carciofi
# Primeiro Exercício de Programação (EP1)

# bibliotecas usadas
import matplotlib.pyplot as plt
import numpy as np

h = 6.626e-34
c = 3.0e+8
k = 1.38e-23
pi = np.pi

def planck(wav, temp):
    a = 2.0*h*c**2
    b = h*c/(wav*k*temp)
    intensidade = a/ ( (wav**5) * (np.exp(b) - 1.0) )
    return intensidade

# Para utilizar a função escrita e plotar, temos que determinar um intervalo #
# Determina-se, ainda, um espaçamento entre os pontos de 1e-9 #
range_lambda = np.arange(1e-7, 1e-5, 1e-9) 

# intensity at 4000K, 5000K, 6000K, 7000K
I_estrela = planck(range_lambda, 3000.)
plt.plot(range_lambda*1e9, I_estrela, 'b-')   #Linha azul para a função da estrela#
plt.suptitle('Função de Planck - estrela')
plt.xlabel(' Wavelength (nm) ', fontsize=14) #nomeia eixo x#
plt.ylabel(' Intensidade ', fontsize=14)     #nomeia eixo y#
plt.show()

I_poeira = planck(range_lambda, 800.)
plt.plot(range_lambda*1e9, I_poeira, 'k-')     #Linha preta para a função da poeira#
plt.suptitle('Função de Planck - poeira')
plt.xlabel(' Wavelength (nm) ', fontsize=14)  #nomeia eixo x#
plt.ylabel(' Intensidade ', fontsize=14)      #nomeia eixo y#
plt.show()

plt.hold(True) 



