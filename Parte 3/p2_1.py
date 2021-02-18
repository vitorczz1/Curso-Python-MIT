#Parte 1

def square(x):
    x **= 2
    return x

#Parte 2

def fourth_power(y):
    sq1 = square(y) 
    sq2 = square(sq1)

    return sq2

#Parte 3

def perfect_square(z):
     if (z < 0):
        print("Error")

     elif ((z == 0) or (z == 1)):
        return True
     else:
        return False