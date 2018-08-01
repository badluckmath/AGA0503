
# AGA 0503 - Métodos Numéricos para Astronomia
# Professor Dr. Alex Carciofi
# Primeiro Exercício de Programação (EP1)

### Esse Programa encontra raízes de funções pelo Método das Secantes ##

def f(x):                ## Função a qual queremos as raízes ##
    result = x **2 -2
    return result

def erro (x2, x1):
    e = abs(x2 - x1)/x1
    return e

x1 = 1 # x1 e x2 formam o intervalo inicial fornecido pelo usuário #
x2 = 2
x3 = x2 - ( (x2 - x1)*f(x2) / ( f(x2) - f(x1) ) )
x4 = x3 - ( (x3 - x2)*f(x3) / ( f(x3) - f(x2) ) )
x5 = x4 - ( (x4 - x3)*f(x4) / ( f(x4) - f(x3) ) )
x6 = x5 - ( (x5 - x4)*f(x5) / ( f(x5) - f(x4) ) )
x7 = x6 - ( (x6 - x5)*f(x6) / ( f(x6) - f(x5) ) )
x8 = x7 - ( (x7 - x6)*f(x7) / ( f(x7) - f(x6) ) ) # Aqui pode usar quantas iterações quiser #
x9 = x8 - ( (x8 - x7)*f(x8) / ( f(x8) - f(x7) ) )

i = [0,1,2,3,4,5,6,7,8]
x = [x1, x2,x3,x4,x5,x6,x7,x8,x9]
f_x = [f(x1), f(x2), f(x3), f(x4), f(x5), f(x6), f(x7), f(x8), f(x9)]
erro = [erro(x3,x2), erro(x4,x3), erro(x5,x4), erro(x6,x5), erro(x7,x6) ]

print ("i", end = " ")
print ("x", end = " ")
print ("f(x)", end = " ")
print ("Erro")

for j in range (5):            # Printa de forma organizada os resultados #
    print(i[j], end = " ")     # com nº da iteração, valor de x e f(x) e erro #
    print (x[j], end = " ")
    print (f_x[j], end = " ")
    print (erro[j])
