
# AGA 0503 - Métodos Numéricos para Astronomia
# Professor Dr. Alex Carciofi
# Quarto Exercício de Programação (EP4)

# bibliotecas usadas
import math
import numpy as np
from pylab import *
import matplotlib.pyplot as plt


### Constantes utilizadas, com temperaturas em CGS ### 
h = 6.63e-27    #Planck
c = 2.99e+10    #Luz
k = 1.38e-16    #Boltzmann
sigma = 5.67e-5 #Stefan

"""
### Constantes utilizadas, com temperaturas em SI ### 
h = 6.6e-34     
c = 3e+8       
k = 1.38e-23    
sigma = 5.67e-8 
"""     

def blackbody ( wav , temp ):
        
        expoente = (h*c / (wav*k*temp))
        div = ((wav ** 5 )) * ((np.exp(expoente))-1.0)
        blackbody = 2*h*(c**2) / div
        return blackbody


# Passo 1

tabela = np.loadtxt("dados.txt", skiprows=1)
lbd = tabela[:,0]
lbd = lbd * 1e-8 # Transformando para centimetro
#lbd = lbd * 1e-10 # Transformando para metro
flux = tabela[:,1]
flux = flux * 1e8
err = tabela[:,2]
err = err * 1e8

"""
fernanda = blackbody (lbd , 7000)
fernanda1 = blackbody (lbd ,300)
print (fernanda)
print (fernanda1)
"""

# Passo 2

Tsmin = input("Valor de temperatura minima da estrela: ")
Tsmax = input("Valor de temperatura maxima da estrela: ")
Tpmin = input("Valor de temperatura minima da poeira: ")
Tpmax = input("Valor de temperatura maxima da poeira: ")
N = input("Espaçamentos entre os maximos e minimos de temperatura: ")
print("")

# Gerando N valores de temperatura para estrela e N valores de temperatura para poeira

Ts = np.linspace(Tsmin, Tsmax, N) # Conjunto de temperaturas da estrela a serem usados (vetorizado, numpy)
Tp = np.linspace(Tpmin, Tpmax, N) # Conjunto de temperaturas da poeira a serem usados (vetorizado, numpy)

# Construindo mapa de chi-quadrado agora.

# Calculando espectro teoricos

def espectro ( wav, T1, T2 ):
        B1 = (blackbody (wav, T1)) / (sigma * T1**4)
        B2 = (blackbody (wav, T2)) / (sigma * T2**4)
        soma = B1 + B2
        return soma


S = [] # S eh o mapa de espectros teoricos
print("Calculando modelos teoricos... Aguarde.")
print("")
for i in range (len(Ts)):
        lista = []
        for j in range (len(Tp)):
                fluxo = list(espectro(x, Ts[i], Tp[j]) for x in lbd)
                lista.append(fluxo)
        S.append(lista)

print("Procurando o melhor ajuste...")
print("")


# migueh
for i in range (len(S)):
        for j in range (len(S[0])):
                for k in range (len(S[0][0])):
                     S[i][j][k] = S[i][j][k] * np.pi


def chi2 (Si, S, sig):
        # Si eh o fluxo observado
        # S eh o fluxo teorico
        # sig eh o erro observacional
        chiq = []
        for i in range (len(S)):
                lista = []
                for j in range (len(S[0])):
                        chi = sum( ((flux - S[i][j])/sig)**2 )
                        lista.append(chi)
                chiq.append(lista)
        return chiq

chiq = chi2(flux, S, err)



# Encontrando o minimo do chi-quadrado

chiq_min = chiq[0][0]
index_min = (0,0)
for i in range (len(chiq)):
        for j in range (len(chiq[0])):
                if chiq[i][i] < chiq_min:
                        chiq_min = chiq[i][j]
                        index_min = (i,j)

f = index_min[0]
g = index_min[1]
Ts_min = Ts[f]
Tp_min = Tp[g]
chiqP = chiq[g]
chiqS = chiq[f]

chiq_plot = []
for i in range(len(chiq)):
        add = []
        for j in range (len(chiq[0])):
                add.append(chiq[i][j])
        chiq_plot.append(add)
           
minimo = chiq_plot[0][0]
for i in range(len(chiq_plot)):
        for j in range (len(chiq_plot[0])):
                if chiq_plot[i][j] < minimo:
                        minimo = chiq_plot[i][j]


for i in range(len(chiq_plot)):
        for j in range (len(chiq_plot[0])):
                if chiq_plot[i][j] > 1.5 * minimo:
                        chiq_plot[i][j] = 1.5 * minimo
                        

for i in range (len(chiqS)):
        if chiqS[i] > 1.5* min(chiqS):
                chiqS[i] = 1.5* min(chiqS)


for i in range (len(chiqP)):
        if chiqP[i] > 1.5* min(chiqP):
                chiqP[i] = 1.5* min(chiqP)


print "Temperatura da estrela:", round(Ts_min,1),"Kelvin."

print "Temperatura da poeira:", round(Tp_min,2),"Kelvin." 

print("")


### chi=((observado-teorico)**2)/(sigma**2) ###


plt.figure()

plt.errorbar(lbd * 1e4, flux , yerr=err)
"""
# trecho pra plotar todos os modelos

for i in range (len(S)):
        for j in range (len(S[0])):
                plt.plot(lbd * 1e4, S[i][j])
"""

#Plota o melhor modelo com os dados
plt.plot(lbd * 1e4, S[f][g], 'ko--')
plt.gca().legend(('Dados','Modelo Teorico'))
plt.title("Dados plotados")
plt.xlabel("Comprimento de onda (microns)")
plt.ylabel("Fluxo (erg/s)")
plt.yscale('log')
plt.xscale("log")
plt.savefig("espectro.png")
plt.show()


#plota chi-quadrado com temperatura da estrela
plt.figure()
plt.title("Chi-quadrado vs. Temperatura da estrela")
plt.xlabel("Temperaturas da estrela (K)")
plt.ylabel("Chi-quadrado")
plt.plot(Ts, chiqS, 'k.-')
plt.savefig("Chi2_temp_estrela.png")
plt.show()

#plota chi-quadrado com temperatura da poeira
plt.figure()
plt.title("Chi-quadrado vs. Temperatura da poeira")
plt.xlabel("Temperaturas da poeira (K)")
plt.ylabel("Chi-quadrado")
plt.plot(Tp, chiqP, 'k.-')
plt.savefig("Chi2_temp_poeira.png")
plt.show()

#plota mapa de chi-quadrado

plt.axes([0.025,0.025,0.95,0.95])
plt.title("Mapa de chi-quadrado")
plt.xlabel("Temperatura estrela")
plt.ylabel("Temperatura poeira")
plt.imshow(chiq_plot, interpolation='nearest', cmap='bone', origin = 'lower')
plt.colorbar(shrink=.92)
plt.xticks([]), plt.yticks([])
plt.savefig("Mapa_cortado.png")
plt.show()

plt.axes([0.025,0.025,0.95,0.95])
plt.title("Mapa de chi-quadrado")
plt.xlabel("Temperatura estrela")
plt.ylabel("Temperatura poeira")
plt.imshow(chiq, interpolation='nearest', cmap='bone', origin = 'lower')
plt.colorbar(shrink=.92)
plt.xticks([]), plt.yticks([])
plt.savefig("Mapa.png")
plt.show()

#Plot para resíduos
plt.figure()
residuo = (array(S[f][g]) - flux)/err
plt.scatter(lbd, residuo)
plt.xlim(-0.0001,0.01)
plt.title('Residuos')
plt.grid()
plt.savefig('residuos.png')
plt.show()


