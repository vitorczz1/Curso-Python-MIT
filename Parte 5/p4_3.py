
class Rational:    

    def __init__(self, num, denom):
        self.num = num
        self.denom = denom

    def get_numerator(self):
        return (self.num)

    def get_denominator(self):
        return (self.denom) 

    def to_float(self):
        return (self.num / self.denom)

    def reciprocal(self):
        reciprocal_num = self.denom
        reciprocal_denom = self.num
        return Rational(reciprocal_num, reciprocal_denom)

    def reduce(self):
        num_cp = self.num
        denom_cp = self.denom
    
        while (not denom_cp == 0):
              resto = (num_cp % denom_cp)
              num_cp = denom_cp
              denom_cp = resto
        max = num_cp
        num_final = self.num/max
        denom_final = self.denom/max
        self.num = num_final
        self.denom = denom_final
        return self

    def __sub__(self, other):
        if isinstance(other, Rational):
           num_sub = ((self.num * other.denom) - (other.num * self.denom))
           denom_sub = (self.denom * other.denom)

           self.num = num_sub
           self.denom = denom_sub

           num_cp = self.num
           denom_cp = self.denom

           while (not denom_cp == 0):
                  resto = (num_cp % denom_cp)
                  num_cp = denom_cp
                  denom_cp = resto
           max = num_cp
           num_sub = self.num/max
           denom_sub = self.denom/max
           return Rational(num_sub, denom_sub)

        elif isinstance(other, int):
             num_sub = ((self.denom * other) - self.num)
             denom_sub = (self.denom)
             self.num = num_sub
             self.denom = denom_sub

             num_cp = self.num
             denom_cp = self.denom

             while (not denom_cp == 0):
                   resto = (num_cp % denom_cp)
                   num_cp = denom_cp
                   denom_cp = resto
             max = num_cp
             num_sub = self.num/max
             denom_sub = self.denom/max
             return Rational(num_sub, denom_sub)

        elif isinstance(other, float):
             result = (self.num/self.denom)
             return (result - other)

        else:
             return None

    def __truediv__(self, other):
        if isinstance(other, Rational):
           num_truediv = (self.num * other.denom)
           denom_truediv = (self.denom * other.num)

           num_cp = num_truediv
           denom_cp = denom_truediv

           while (not denom_cp == 0):
                  resto = (num_cp % denom_cp)
                  num_cp = denom_cp
                  denom_cp = resto
           max = num_cp

           num_final = num_truediv/max
           denom_final = denom_truediv/max

           return Rational(num_final, denom_final)

        elif isinstance(other, int):
             num_truediv = (self.num)
             denom_truediv = (self.denom * other)
             num_cp = num_truediv
             denom_cp = denom_truediv

             while (not denom_cp == 0):
                   resto = (num_cp % denom_cp)
                   num_cp = denom_cp
                   denom_cp = resto
             max = num_cp

             num_final = num_truediv/max
             denom_final = denom_truediv/max
             return Rational(num_final, denom_final)

        elif isinstance(other, float):
             result = (self.num/self.denom)
             return (result/other)

        else:
             return None

    def __mul__(self, other):
        if isinstance(other, Rational):
           num_mul = (self.num * other.num)
           denom_mul = (self.denom * other.denom)
           num_cp = num_mul
           denom_cp = denom_mul

           while (not denom_cp == 0):
                 resto = (num_cp % denom_cp)
                 num_cp = denom_cp
                 denom_cp = resto
           max = num_cp

           num_final = num_mul/max
           denom_final = denom_mul/max

           return Rational(num_final, denom_final)  

        elif isinstance(other, int):
             num_mul = (self.num * other)
             denom_mul = (self.denom)
             num_cp = num_mul
             denom_cp = denom_mul

             while (not denom_cp == 0):
              resto = (num_cp % denom_cp)
              num_cp = denom_cp
              denom_cp = resto
             max = num_cp

             num_final = num_mul/max
             denom_final = denom_mul/max

             return Rational(num_final, denom_final)

        elif isinstance(other, float):
             result = (self.num/self.denom)
             return (result * other)

        else:
             return None

    def __add__(self, other):
        if isinstance(other, Rational):
           num_add = ((self.num * other.denom) + (other.num * self.denom))
           denom_add = (self.denom * other.denom)

           self.num = num_add
           self.denom = denom_add

           num_cp = self.num
           denom_cp = self.denom

           while (not denom_cp == 0):
                 resto = (num_cp % denom_cp)
                 num_cp = denom_cp
                 denom_cp = resto
           max = num_cp
           num_add = self.num/max
           denom_add = self.denom/max
           return Rational(num_add, denom_add)

        elif isinstance(other, int):
            num_add = ((self.denom * other) + self.num)
            denom_add = (self.denom)

            self.num = num_add
            self.denom = denom_add

            num_cp = self.num
            denom_cp = self.denom

            while (not denom_cp == 0):
                  resto = (num_cp % denom_cp)
                  num_cp = denom_cp
                  denom_cp = resto
            max = num_cp
            num_add = self.num/max
            denom_add = self.denom/max
            return Rational(num_add, denom_add)
    
        elif isinstance(other, float):
             result = (self.num/self.denom)
             return (result + other)
        else:
             return None