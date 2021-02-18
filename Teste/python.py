def soma():
  result = x + y
  print("O resultado é: ",result)

def sub():
  result = x - y
  print("O resultado é: ",result)

def mul():
  result = x * y
  print("O resultado é: ",result)

def div():
  result = x / y
  print("O resultado é: ",result)



print('digite o valor de x')
x = int(input())

print('digite a operacao desejada: ')
op = input()

print('digite o valor de y')
y = int(input())

if ((x or y or op) < 0):
  print("erro")

elif (op == '+'):
    soma()

elif (op == '-'):
    sub()

elif (op == '*'):
    mul()

elif (op == '/'):
    div()







