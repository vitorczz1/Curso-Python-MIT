def hailstone_sequence(a_0):

    val = [a_0] #tupla dos valores
    
    while (a_0 != 1) :  # ate atingir a[k] = 1
        if (a_0 % 2) == 0:  # verifica se é par
            a_0 /= 2 #formula 1 
            val.append(a_0)

        else:
            a_0 = (a_0 * 3) + 1 #formula 2
            val.append(a_0)
    return val
