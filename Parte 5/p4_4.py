
class Vector():

    def __init__(self, vet):
        self.vet = vet

    def as_list(self):
        return (self.vet)

    def size(self):
        tam = len(self.vet)
        return (tam)

    def magnitude(self):
        total = 0
        for i in self.vet:
            total += (i ** 2) 
        result = total ** 0.5
        return (result)

    def euclidean_distance(self, other):
        result = 0
        for i in range(self.size()):
            result += ((other.vet[i] - self.vet[i])**2)
        result **= 0.5
        return result

    def normalized(self):
        magnitude_v = self.magnitude()
        v_normalized = []
        if (magnitude_v > 0):
            for num in self.vet:
                v_normalized.append(num/magnitude_v)
        self.vet = v_normalized
        return self

    def cosine_similarity(self, other):
        produto_interno = 0
        magnitude_vector = self.magnitude()
        v = Vector(other.vet)
        magnitude_vector_other = v.magnitude()
        produto_normalizado = (magnitude_vector * magnitude_vector_other)
        for i in range(self.size()):
            produto_interno += self.vet[i] * other.vet[i]
        result = (produto_interno / produto_normalizado)
        return result

    def __add__(self, other):
        if isinstance(other, Vector):
           if (self.size() != other.size()):
              return None
           else:
              vector = []
              for i in range(self.size()):
                  vector.append(self.vet[i] + other.vet[i])
              return Vector(vector)

    def __sub__(self, other):
        if isinstance(other, Vector):
          if (self.size() != other.size()):
             return None
          else:
             vector = []
             for i in range(self.size()):
                 vector.append(self.vet[i] - other.vet[i])
             return Vector(vector)

    def __mul__(self, other):
        if isinstance(other, Vector):
           if (self.size() != other.size()):
              return None
           else:
              produto_escal = 0
        
              for i in range(self.size()):
                  produto_escal += self.vet[i] * other.vet[i]
              return produto_escal
    
        elif isinstance(other, int):
             vector = []
             for num in self.vet:
                 vector.append(num * other)
             return Vector(vector)
    
        elif isinstance(other, float):
             vector = []
             for num in self.vet:
                 vector.append(num * other)
             return Vector(vector)

    def __truediv__(self, other):
        if isinstance(other, int):
           vector = []
           for num in self.vet:
               vector.append(num / other)
           return Vector(vector)
    
        elif isinstance(other, float):
             vector = []
             for num in self.vet:
                vector.append(num / other)
             return Vector(vector)
        else:
             return None
