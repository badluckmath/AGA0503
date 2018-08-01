
# AGA 0503 - Métodos Numéricos para Astronomia
# Professor Dr. Alex Carciofi
# Terceiro Exercício de Programação (EP3)

# 2) Interpolação Spline (4 pontos)

#Sugestão: leia esse código em full screen, para que todos comentários estejam organizados de forma mais apropriada.

# OBS: nesse aqui eu usei o pacote Interpolate do SciPy pra comparação com meu código original.
# NÃO considerar esse aqui.

#Bibliotecas:

import scipy.interpolate as sp
import numpy
import pylab

# Define-se a função teórica

def f(x):
    return 1/(1+25*x*x)

# xx e yy fornecerão, para nós, o gráfico verdadeiro da função teórica

xx = numpy.linspace(-1, 1, 1000)
yy = f(xx)

# Aqui temos os intervalos dos dados fornecidos, gravados nas variáveis x e y

x = numpy.linspace(-1, 1, 10)
y = f(x)

# Operação de interpolação Spline-Cúbica pelo pacote "Interpolate" do SciPy

fc = sp.interp1d(x, y,kind='cubic')

print("Interpolação bem-sucedida!")
print (fc)

# Preparando pra plotar

#Plotando a função teórica separadamente
xnew = numpy.linspace(-1, 1, 100)
pylab.subplot(211)
pylab.plot(xx, yy)
pylab.legend(['f(x)=1/(1+25*x*x)'], loc='best')

# Plotando a sobreposição dos pontos fornecidos ('o'), da função teórica e da interpolação
pylab.subplot(212)
pylab.plot(xx, yy, x, y, 'o', xnew, fc(xnew))
pylab.legend(['Teórico','Dados', 'Spline'], loc='upper left')

# Revelando o resultado.
pylab.show()



