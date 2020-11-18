##################################################
## Crie uma função que recebe uma lista de números inteiros e retorna
## os dois menores números da lista. 
##
## Exemplo:
## [34, 15, 88, 2] --> 15, 2
## [34, -345, -1, 100] --> -345, -1
## [7, 7, 7] --> 7, 7
##################################################
def find_smallest_numbers(lst):
    lst.sort()
    print(lst[0], lst[1])
    
lst = []

n = int(input("Digite o número de Elementos: ")) 

for i in range(0, n): 
    el = int(input()) 
  
    lst.append(el)

find_smallest_numbers(lst)
    