
#Parte 1

def largest_number(input_list):
    best_so_far = -9999999

    if (len(input_list) == 0 or len(input_list) == 1):
        return None

    for i in input_list:
        if i > best_so_far:
            best_so_far = i
    return(best_so_far)

#Parte 2

def second_largest_number(input_list):
    best_so_far = -9999999
   
    if (len(input_list) == 0 or len(input_list) == 1):
        return None

    maior = largest_number(input_list)

    input_list.remove(maior)  

    for i in input_list:    
        if i > best_so_far:
            best_so_far = i
    return(best_so_far)