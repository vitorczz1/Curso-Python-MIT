p_d = 5
cells_square = p_d ** 2
cells_circle = 0
matriz = [[0 for i in range(p_d)] for j in range(p_d)]

centro = (p_d // 2)

for i in range(p_d): # 0
  for j in range(p_d): # 0
    if (i <= centro):
      matriz[i][j] = (i-centro, centro - j)
    elif (i > centro):
      matriz[i][j] = ((centro-i) * -1, (j-centro) * -1)

for j in range (p_d):
  for i in range(p_d):
    xy = []
    xy = matriz[i][j]
    x = xy[0]
    y = xy[1]

    dist = ((x ** 2) + (y ** 2)) ** 0.5
  
    if (dist <= p_d/2):
      cells_circle = cells_circle + 1
  
out = (cells_circle/cells_square) * 4

print(out)
