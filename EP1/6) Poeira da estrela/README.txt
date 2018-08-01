

Essa pasta contém os arquivos referentes à resolução do Primeiro Exercício de Programação (EP1) da disciplina AGA0503 - Métodos Numéricos em Astromia oferecida pelo IAG-USP no primeiro semestre de 2018 e ministrada pelo Prof. Dr. Alex Carciofi.

O programa "Planck-plot" que calcula e plota funções de Planck para diferentes comprimentos de ondas e temperaturas. Por default, deixei esse programa plotando funções de corponegro para temperaturas de 3000K e 800K, que eram os parâmetros para o trabalho na época. O(a) usuário(a) pode alterar facilmente esses parâmetros para plotar a função de corponegro na temperatura que ele(a) quiser.

A implementação "MétodoDicotomia" utiliza o Método da Bissecção ou Dicotomia para calcular raízes de funções genéricas. 

O arquivo EsferaPlot3D não é muito útil. A ideia é plotar uma superfície esférica em vermelho, representando a esfera, e outros dois wireframes esféricos em azul, representando a casca de poeira ao redor da mesma. Contudo, na realidade a casca de poeira é tão gigantescamente maior que a estrela que nem da pra ver o pontinho vermelho. Hahaha. 

O arquivo "CalculaDensidadeGrãos" usa os dois primeiros programas para calcular a densidade de grão por unidade de volume de uma nuvem de poeira ao redor de uma estrela genérica. As propriedades da nuvem, da poeira e da estrela podem ser customizadas e o Default está implementado para fornecer a resposta conforme dados do EP1 fornecidos. 

Os parâmetros originais do trabalho eram: 

### Incógnitas utilizadas, com temperaturas em KELVIN e distâncias em METROS ###
h = 6.6e-34     # Constante de Planck
c = 3e+8        # Velocidade da luz no vácuo, em mícrons por segundo #
k = 1.38e-23    # Constante de boltzmann [k] = J/K #
Dsol = 1.4e+9   # Diâmetro do Sol # 
Rsol = Dsol / 2 # raio do Sol, em função de seu diâmetro conhecido, em metros #

### Incógnitas fornecidas pelo problema proposto original ### 
R = 10 * Rsol       # Raio da estrela em função daquele do Sol #
Tef = 3e+3          # Temperatura da superfíce da estrela # 
Ri = 2e+2 * Rsol    # Raio interno de um anel de poeira  ao redor da estrela de Ramo Assintótico das Gigantes #
Re = 2e+3 * Rsol    # Raio externo de um anel de poeira  ao redor da estrela de Ramo Assintótico das Gigantes #
a = 2e-7            # Raio de um grão presumidamente esférico #     
Tpoeira = 8e+2      # Temperatura de cada grão de poeira #
epsilon = 1e-6      # critério de convergência do método de determinação das raízes
jk = 6e-1           # J-K é o índice de cor observado. 
lambda_k = 2.2e-6   # comprimento de onda associado à banda K
lambda_j = 1.6e-6   # comprimento de onda associado à banda J