#Calculadora by Vitor Costa

x = int(input("Digite o primeiro valor: "))
sinal = input("Digite a operação: ")
y = int(input("Digite o segundo valor: "))

def soma():
    som = x + y
    print(som)
 
def subtracao():
    sub = x - y
    print(sub)

def multiplicacao():
    mult = x * y
    print(mult)
    
def divisao():
    div = x / y
    print(div)
    
def modulo():
    mod = x % y
    print(mod)


if sinal == '+':
    soma()
    
elif sinal == '-':
    subtracao()

elif sinal == '*':
    multiplicacao()
    
elif sinal == '/':
    divisao()
    
elif sinal == '%':
    modulo()

else:
    print ("Erro !")