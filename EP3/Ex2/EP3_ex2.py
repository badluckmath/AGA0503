
# AGA 0503 - Métodos Numéricos para Astronomia
# Professor Dr. Alex Carciofi
# Terceiro Exercício de Programação (EP3)

# 2) Interpolação Spline (4 pontos)

#Sugestão: leia esse código em full screen, para que todos comentários estejam organizados de forma mais apropriada.

## OBS: Sei que meu plot não ficou certo, mas acho que a interpolação está correta, segui com exatidão o algoritmo. Acho que só errei na criação do plot do
## gráfico da interpolação. 

#Bibliotecas:
import math  
import matplotlib.pyplot as plt
import numpy as np
                            
def spline(x, y):                               # Define-se uma função para a operação da interpolação spline                        

  n = len(x) - 1

  # Cria-se array h de tamanho n = len(x), tal que h[i] = x[i+i] - x[i] (igual apostila)
  h = [x[i+1]-x[i] for i in range(n)]

  # Cria-se array alpha de tamanho n-1 = len(x) -1 tal que alpha[i] = 3/h[i] * (alpha[i+1] - alpha[i]) - 3/h[i-1] * (alpha[i] - alpha[i-1])
  alpha = [3*((y[i+1]-y[i])/h[i] - (y[i]-y[i-1])/h[i-1]) for i in range(1,n)]
  alpha.insert(0,0)
  print(alpha)

  # Inicializa-se arrays l, u e z tal que l_0 = 1 e u_0 = z_0 = 0
  l = [1] * (n+1)
  u = [0] * (n+1)
  z = [0] * (n+1)

  # Inicializando arrays b, c e d
  b = [0] * (n+1)
  c = [0] * (n+1)
  d = [0] * (n+1)

  # Começando as operações
  for i in range(1, n):

    # Operando array l, conforme algoritmo
    l[i] = 2*(x[i+1]-x[i-1]) - h[i-1]*u[i-1]
    # Operando array u, conforme algoritmo
    u[i] = h[i]/l[i]
    # Operando array z, conforme algoritmo
    z[i] = (alpha[i] - h[i-1]*z[i-1])/l[i] 

  # Utilizando range no sentido invertido
  for i in range(n-1, -1, -1):
    # Operando array c, conforme algoritmo
    c[i] = z[i] - u[i]*c[i+1]
    # Operando array b, conforme algoritmo
    b[i] = (y[i+1]-y[i])/h[i] - h[i]*(c[i+1] + 2*c[i])/3
    # Operando array d, conforme algoritmo
    d[i] = (c[i+1]-c[i])/(3*h[i])

  # Agora, temos os coeficientes a, b, c e d para construirmos nossos polinômios de terceiro grau
  # Vale que a[i] = y[i], então retorna o array y inputado pelo usuário
  return [y, b, c, d]
  
if __name__ == '__main__':
  def f(x):                                   # Função a ser interpolada
    return 1/(1+25*x*x)
    
  # Criando arrays da função teórica, de acordo com o input, para plotar
  x =[]
  passo = 0.1
  init = -1.0
  final = 1.0
  intervalos = int(abs(final - init)//passo + 1)
  print ("intervalos:" , intervalos)
  pts = intervalos + 1
  for i in range (pts):
    x.append(init)
    init = init + 0.1

  y = []
  for i in range (len(x)):
      y.append(f(x[i]))

  # process
  a = spline(x, y)
  
  passo = 0.02
  pontos_por_intervalo = 5
  init = -1

  # Aqui a ideia que eu tive foi criar arrays xs e ys para relacionar os valores inputados com os interpolados. 
  xs = []
  ys = []

  for k in range ( len(x)-1 ):
      xs_add = []
      for i in range (pontos_por_intervalo):
          xs_add.append(init)
          init = init + passo
      xs.append(xs_add)

  for k in range (20):
      ys_add = []
      for i in range (pontos_por_intervalo):
          ys_add.append([a[0][i] + 
               a[1][k]*(xs[k][i]) + 
               a[2][k]*(xs[k][i])**2 + 
               a[3][k]*(xs[k][i])**3])
      ys.append(ys_add)
  
  # prepare data for plotting the given function

  # Número de pontos a serem utilizados, conforme enunciado. 
  npts = 100

  # Criando intervalos pertinentes de acordo com o numero de pontos utilizando 'linspace' do Numpy
  x = np.linspace(-1, 1, npts)
  y = [f(x[i]) for i in range(len(x))]

  for i in range(len(xs)):
    plt.plot(xs[i],ys[i], 'r.-')
  plt.plot(x,y,'k--')

  plt.title('Interpolação Spline')
  plt.xlabel('x')
  plt.ylabel('f (x)')
  plt.show()

