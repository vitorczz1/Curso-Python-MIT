##################################################
## Crie uma função que, dado um número, retorna true se ele ele é
## menor ou igual a zero.
##
## Exemplo:
## 5  --> False
## 0  --> True
## -3 --> True
##
##################################################
def less_than_or_equal_to_zero(num):
    if num <= 0:
       print("True")
    else:
        print("False")
    
num = int(input("Digite um número: "))

less_than_or_equal_to_zero(num)