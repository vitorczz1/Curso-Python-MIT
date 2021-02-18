
def prime(num):
    multiplo = 0

    if (num >= 0):
       for i in range(2,num):
           if (num % i == 0):
              multiplo = multiplo + 1
           
       if ((multiplo == 0) and (num != 1 and num != 0)):
          return True
          
       else:
          return False