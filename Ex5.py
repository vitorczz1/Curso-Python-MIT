##################################################
## Escreva uma função que recebe uma lista de inteiros e retorna a
## soma dos valores absolutos de cada elemento da lista.
##
## Exemplo:
##
## [2, -1, 4, 8, 10] --> 25
##
## [-3, -4, -10, -2, -3] --> 22
##
## [2, 4, 6, 8, 10] --> 30
## 
## [-1] --> 1
##################################################
def compute_abs_sum(lst,n):
    for x in range(0,n):
        soma = lst[:x] + lst[x]
    print(soma)
    
lst = []
    
n = int(input("Elementos: "))

for i in range(0,n):
    el = int(input("Valores: "))
    
    lst.append(el)
    
compute_abs_sum(lst,n)