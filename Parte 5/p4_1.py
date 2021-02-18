
#Parte 1

def warehouse_process(d, t):
    
    if (not t[1] in d.keys() and t[0] == 'receive'):
        d[t[1]] = t[2]
    
    elif (t[1] in d.keys() and t[0] == 'ship'):
        d[t[1]] -= t[2]

        if (d[t[1]] < 0): 
            d[t[1]] = 0
            print ("not enough")   
        
    elif (t[1] in d.keys() and t[0] == 'receive'):
        d[t[1]] += t[2]

#Parte 2

class Warehouse:
    def __init__(self):
        self.d = {}

    def process(self, t):
        if (not t[1] in self.d.keys() and t[0] == 'receive'):
            self.d[t[1]] = t[2]
        
        elif (t[1] in self.d.keys() and t[0] == 'ship'):
            self.d[t[1]] -= t[2]

            if (self.d[t[1]] < 0): 
                self.d[t[1]] = 0
                print ("not enough")   
            
        elif (t[1] in self.d.keys() and t[0] == 'receive'):
            self.d[t[1]] += t[2]

    def lookup(self, key):
        if (not key in self.d.keys()):
            return 0

        total = self.d[key]
        return total