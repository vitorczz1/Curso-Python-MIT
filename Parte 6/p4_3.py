
class Rational:    

    def _init_(self, num, denom):
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
        n = self.num
        d = self.denom
        while (d != 0):
          r = (n%d)
          n = d
          d = r
        m = n
        self.num = self.num/m
        self.denom = self.denom/m
        return self

    def MDC(self):
      n = self.num
      d = self.denom
      while (d != 0):
        r = (n%d)
        n = d
        d = r
      return n

    def _add_(self, other):
      if isinstance(other, Rational):
        self.num = ((self.num * other.denom) + (other.num * self.denom))
        self.denom = (self.denom * other.denom)
        m = self.MDC()
        return Rational((self.num/m), (self.denom/m))
      elif isinstance(other, int):
        self.num = ((self.denom * other) + self.num)
        self.denom = (self.denom)
        m = self.MDC()
        return Rational((self.num/m), (self.denom/m))
      elif isinstance(other, float):
        result = (self.num/self.denom)
        return float (result + other)
      else:
        return None

    def _mul_(self, other):
      if isinstance(other, Rational):
          num_mul = (self.num * other.num)
          denom_mul = (self.denom * other.denom)
          n = (self.num * other.num)
          d = (self.denom * other.denom)
          while (d != 0):
            r = (n%d)
            n = d
            d = r
          m = n
          num_final = num_mul/m
          denom_final = denom_mul/m
          return Rational(num_final, denom_final)
      elif isinstance(other, int):
            num_mul = (self.num * other)
            denom_mul = (self.denom)
            n = (self.num * other)
            d = (self.denom)
            while (d != 0):
              r = (n%d)
              n = d
              d = r
            m = n
            num_final = num_mul/m
            denom_final = denom_mul/m
            return Rational(num_final, denom_final)
      elif isinstance(other, float):
            result = (self.num/self.denom)
            return float (result * other)
      else:
             return None

    def _truediv_(self, other):
      if isinstance(other, Rational):
        num_truediv = (self.num * other.denom)
        denom_truediv = (self.denom * other.num)
        n = (self.num * other.denom)
        d = (self.denom * other.num)
        while (d != 0):
          r = (n%d)
          n = d
          d = r
        m = n
        num_final = num_truediv/m
        denom_final = denom_truediv/m
        return Rational(num_final, denom_final)

      elif isinstance(other, int):
          num_truediv = (self.num)
          denom_truediv = (self.denom * other)
          n = (self.num)
          d = (self.denom * other)
          while (d != 0):
            r = (n%d)
            n = d
            d = r
          m = n
          num_final = num_truediv/m
          denom_final = denom_truediv/m
          return Rational(num_final, denom_final)

      elif isinstance(other, float):
          result = (self.num/self.denom)
          return float (result/other)
      else:
             return None

    def _sub_(self, other):
        if isinstance(other, Rational):
           num_sub = ((self.num * other.denom) - (other.num * self.denom))
           denom_sub = (self.denom * other.denom)
           self.num = num_sub
           self.denom = denom_sub
           m = self.MDC()
           num_sub = self.num/m
           denom_sub = self.denom/m
           return Rational(num_sub, denom_sub)

        elif isinstance(other, int):
             num_sub = ((self.denom * other) - self.num)
             denom_sub = (self.denom)
             self.num = num_sub
             self.denom = denom_sub
             m = self.MDC()
             num_sub = self.num/m
             denom_sub = self.denom/m
             return Rational(num_sub, denom_sub)
        elif isinstance(other, float):
             result = (self.num/self.denom)
             return float (result - other)
        else:
             return None