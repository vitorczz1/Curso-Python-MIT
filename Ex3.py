##################################################
## Crie uma função que aceita uma lista e retorna o último elemento
## dessa lista.
##
## Exemplo
## [1, 2, 3] --> 3
##
## ['a', 'b', 'c'] --> 'c'
##
## [True, False, True] --> True
##
## [7, 'String', False] --> False
##################################################
def get_last_item(lst):
    tam = len(lst)
    print ("O último elemento é o: ",lst[tam-1])
    
lst = []

n = int(input("Digite o número de Elementos: ")) 

for i in range(0, n): 
    el = input()
  
    lst.append(el)

get_last_item(lst)