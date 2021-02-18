
class Matrix():
    def __init__(self, lista):
        self.lista = lista
        Matrix._add_ = Matrix.add
        Matrix._sub_ = Matrix.sub

    def size(self):
        numrows = 0
        numcols = 0
        cont = 0
        for i in range(len(self.lista)):
          numrows += 1
          for j in range(len(self.lista[0])):
            if (cont == 0):
              numcols += 1
          cont = 1
        return (numrows, numcols)

    def row(self, n):
        x = self.lista[n]
        return x
    
    def col(self, n):
      #for
        list_col = []

        for i in range(len(self.lista)):
            list_col.append(self.lista[i][n])
        return list_col
      
    def get(self, r, c):
        get_rc = self.lista[r][c]
        return get_rc
      
    def set(self, r, c, val):
        value = val
        self.lista[r][c] = value

    def transpose(self):
        transposed = list(map(list, zip(*self.lista)))
        return Matrix(transposed)          
  
    def mul(self, other):
        matriz_mul = []
        list_line = []
        if isinstance(other, Matrix):
           if (self.size()[1] == (other.size()[0])):
              return None
           else:
              for i in range(self.size()[0]):           
                  matriz_mul.append([])
                  for j in range(other.size()[1]):
                      list_mul = [z*v for z, v in zip(self.row(i), other.col(j))]
                      matriz_mul[i].append(sum(list_mul))
                  new_matriz = Matrix(matriz_mul)
                  return new_matriz
        elif isinstance(other, (int, float)):
              for index_main in range(self.size()[0]):
                for index_secondary in range(self.size()[1]):
                    list_line.append(self.lista[index_main][index_secondary] * other)
                    matriz_mul.append(list_line)
                    list_line = []
                    new_matriz = Matrix(matriz_mul)
                    return new_matriz
        else:
              return None

    def add(self, other):
        matriz_add = []
        list_line = []
        if isinstance(other, Matrix):
           if (self.size() == (other.size())):
              return None
           else:
              for line in range(self.size()[0]):
                  for col in range(self.size()[1]):
                      list_line.append(self.lista[line][col] + other.lista[line][col])
                      matriz_add.append(list_line)
                      list_line = []
                      new_matriz = Matrix(matriz_add)
                      return new_matriz
        elif isinstance(other, (int, float)):
             for index_main in range(self.size()[0]):
                 for index_secondary in range(self.size()[1]):
                     list_line.append(self.lista[index_main][index_secondary] + other)
                     matriz_add.append(list_line)
                     list_line = []
                     new_matriz = Matrix(matriz_add)
                     return new_matriz
        else:
              return None

    def sub(self, other):
        lista_sub = []
        sub = []
        if isinstance(other, Matrix):
           if (self.size() == (other.size())):
              for i in range(self.size()[0]):
                  for j in range(self.size()[1]):
                      lista_sub.append(self.lista[i][j] - other.lista[i][j])
                  sub.append(lista_sub)
                  lista_sub = []
              return Matrix(sub)
           else:
              return None

        elif isinstance(other, int):
             for i in range(self.size()[0]):
                 for j in range(self.size()[1]):
                     lista_sub.append(self.lista[i][j] - other)
                 sub.append(lista_sub)
                 lista_sub = []
             return Matrix(sub)

        elif (other, float):
             for i in range(self.size()[0]):
                 for j in range(self.size()[1]):
                     lista_sub.append(self.lista[i][j] + other)
                 sub.append(lista_sub)
                 lista_sub = []
             return Matrix(sub)
        else:
             return None