
#Parte 1

numportas = 10
portas = [] 

#Parte 2

def ndoors(numportas):
    portas = [] 
    for i in range(numportas):
        portas.append(False) # fechada   
        
    for i in range(numportas):
        contador = i + 1
        for y in range(i, numportas, contador):
            if (portas[y]):
                portas[y] = False # fechada
            else:
                portas[y] = True # Aberta
    list_porta = []

    for i in range(numportas):
        contador = i + 1
        if (portas[i]):
            list_porta.append(contador)
    return(list_porta)