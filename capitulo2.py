#Exercício 2.1
# Repetindo o meu conselho do capítulo anterior, sempre que você aprender um recurso novo,
# você deve testá-lo no modo interativo e fazer erros de propósito para ver o que acontece.

#Vimos que n = 42 é legal. E 42 = n?
#42 = a
#print(a)
#SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
#Ou x = y = 1?
b = c = 1
print(b)

# Em algumas linguagens, cada instrução termina em um ponto e vírgula ;.
# O que acontece se você puser um ponto e vírgula no fim de uma instrução no Python?

d = 1;

#E se puser um ponto no fim de uma instrução?
e = 1.

# Em notação matemática é possível multiplicar x e y desta forma: xy.
# O que acontece se você tentar fazer o mesmo no Python?

#1 O volume de uma esfera com raio r é Fórmula – Volume de uma esfera.. Qual é o volume de uma esfera com raio 5?
#raio = 4/3*pi*raio³

r = 4/3*3.14159265358979323846*(5**3)

print(f'Raio = {r}')

#2 Suponha que o preço de capa de um livro seja R$ 24,95, mas as livrarias recebem um desconto de 40%. 
# O transporte custa R$ 3,00 para o primeiro exemplar e 75 centavos para cada exemplar adicional. 
# Qual é o custo total de atacado para 60 cópias?

preço = 24.95
desconto = 40/100
transporte1 = 3
transporte = 0.75
copias = 60

total = (preço * desconto) + transporte1 + (transporte*copias)
print(f'Valor total = {total}')

#3 Se eu sair da minha casa às 6:52 e correr 1 quilômetro a um certo passo (8min15s por quilômetro), 
# então 3 quilômetros a um passo mais rápido (7min12s por quilômetro) e 
# 1 quilômetro no mesmo passo usado em primeiro lugar, que horas chego em casa para o café da manhã?

#6:52
t0 = 6 * 60 * 60 + 52 * 60
#8min15s
t1 =((8*60)+15)
#7min12s*3
t2 =((7*60)+12)*3
#8min15s
t3 = t1

total = t0+ t1 + t2 + t3

#Função para converter os segundos para hora:minuto:segundos
def convert(seconds): 
    seconds = seconds % (24 * 3600) 
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "%d:%02d:%02d" % (hour, minutes, seconds) 
      
n = total
print(convert(n)) 