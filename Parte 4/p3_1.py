
def run_length_encode_2d(array): 
  array_1d = []
  lista_final = []
  for i in array:
    for j in i:
      array_1d.append(j)
  prox_posicao = -99999
  for i in range(len(array_1d)):
    if (not i+1 <= (prox_posicao)):
      prox_posicao = 1+i
      n_vezes = 1
      if (not prox_posicao >= (len(array_1d))):
        while (array_1d[i] == array_1d[prox_posicao]):
          prox_posicao = prox_posicao + 1
          n_vezes = n_vezes + 1
          if (not prox_posicao < (len(array_1d))):
            break
      lista_final.append((n_vezes, array_1d[i]))
  return lista_final