class Matrix:
    def _init_(self, lista):
        self.lista = lista
        Matrix._sub_ = Matrix.sub
        Matrix._add_ = Matrix.add
    
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
        print(transposed)
        return Matrix(transposed)

    def add(self, other):
      lista_add = []
      add = []
      if isinstance(other, Matrix):
        if (self.size() == (other.size())):
          for i in range(self.size()[0]):
            for j in range(self.size()[1]):
              lista_add.append(self.lista[i][j] + other.lista[i][j])
            add.append(lista_add)
            lista_add = []
          return Matrix(add)
        else:
          return None
      elif isinstance(other, int):
        for i in range(self.size()[0]):
          for j in range(self.size()[1]):
            lista_add.append(self.lista[i][j] + other)
          add.append(lista_add)
          lista_add = []
        return Matrix(add)
      elif (other, float):
        for i in range(self.size()[0]):
          for j in range(self.size()[1]):
            lista_add.append(self.lista[i][j] + other)
          add.append(lista_add)
          lista_add = []
        return Matrix(add)
      else:
        return None

    def sub(self, other):
      lista_add = []
      add = []
      if isinstance(other, Matrix):
        if (self.size() == (other.size())):
          for i in range(self.size()[0]):
            for j in range(self.size()[1]):
              lista_add.append(self.lista[i][j] - other.lista[i][j])
            add.append(lista_add)
            lista_add = []
          return Matrix(add)
        else:
          return None
      elif isinstance(other, int):
        for i in range(self.size()[0]):
          for j in range(self.size()[1]):
            lista_add.append(self.lista[i][j] - other)
          add.append(lista_add)
          lista_add = []
        return Matrix(add)
      elif (other, float):
        for i in range(self.size()[0]):
          for j in range(self.size()[1]):
            lista_add.append(self.lista[i][j] - other)
          add.append(lista_add)
          lista_add = []
        return Matrix(add)
      else:
        return None