##################################################
## Crie uma função que recebe um número inteiro como parâmetro e
## retorna "even" para cada número par e "odd" para cada número ímpar.
##
## Exemplo:
## 3   --> "odd"
##
## 146 --> "even"
##
## 19  --> "odd"
##
## Retorne "even" ou "odd" com letras minúsculas.
##################################################
def is_even_or_odd(num):
    if (num % 2 == 0):
        print("even")
    else:
        print("odd")
    
num = int(input("Digite um número: "))

is_even_or_odd(num)
    