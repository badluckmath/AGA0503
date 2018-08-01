

Essa pasta cont�m os arquivos referentes � resolu��o do Primeiro Exerc�cio de Programa��o (EP1) da disciplina AGA0503 - M�todos Num�ricos em Astromia oferecida pelo IAG-USP no primeiro semestre de 2018 e ministrada pelo Prof. Dr. Alex Carciofi.

O programa "Planck-plot" que calcula e plota fun��es de Planck para diferentes comprimentos de ondas e temperaturas. Por default, deixei esse programa plotando fun��es de corponegro para temperaturas de 3000K e 800K, que eram os par�metros para o trabalho na �poca. O(a) usu�rio(a) pode alterar facilmente esses par�metros para plotar a fun��o de corponegro na temperatura que ele(a) quiser.

A implementa��o "M�todoDicotomia" utiliza o M�todo da Bissec��o ou Dicotomia para calcular ra�zes de fun��es gen�ricas. 

O arquivo EsferaPlot3D n�o � muito �til. A ideia � plotar uma superf�cie esf�rica em vermelho, representando a esfera, e outros dois wireframes esf�ricos em azul, representando a casca de poeira ao redor da mesma. Contudo, na realidade a casca de poeira � t�o gigantescamente maior que a estrela que nem da pra ver o pontinho vermelho. Hahaha. 

O arquivo "CalculaDensidadeGr�os" usa os dois primeiros programas para calcular a densidade de gr�o por unidade de volume de uma nuvem de poeira ao redor de uma estrela gen�rica. As propriedades da nuvem, da poeira e da estrela podem ser customizadas e o Default est� implementado para fornecer a resposta conforme dados do EP1 fornecidos. 

Os par�metros originais do trabalho eram: 

### Inc�gnitas utilizadas, com temperaturas em KELVIN e dist�ncias em METROS ###
h = 6.6e-34     # Constante de Planck
c = 3e+8        # Velocidade da luz no v�cuo, em m�crons por segundo #
k = 1.38e-23    # Constante de boltzmann [k] = J/K #
Dsol = 1.4e+9   # Di�metro do Sol # 
Rsol = Dsol / 2 # raio do Sol, em fun��o de seu di�metro conhecido, em metros #

### Inc�gnitas fornecidas pelo problema proposto original ### 
R = 10 * Rsol       # Raio da estrela em fun��o daquele do Sol #
Tef = 3e+3          # Temperatura da superf�ce da estrela # 
Ri = 2e+2 * Rsol    # Raio interno de um anel de poeira  ao redor da estrela de Ramo Assint�tico das Gigantes #
Re = 2e+3 * Rsol    # Raio externo de um anel de poeira  ao redor da estrela de Ramo Assint�tico das Gigantes #
a = 2e-7            # Raio de um gr�o presumidamente esf�rico #     
Tpoeira = 8e+2      # Temperatura de cada gr�o de poeira #
epsilon = 1e-6      # crit�rio de converg�ncia do m�todo de determina��o das ra�zes
jk = 6e-1           # J-K � o �ndice de cor observado. 
lambda_k = 2.2e-6   # comprimento de onda associado � banda K
lambda_j = 1.6e-6   # comprimento de onda associado � banda J