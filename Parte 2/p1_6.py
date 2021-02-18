p_d = 13
centro = (p_d // 2)
cells_square = p_d ** 2
cells_circle = 0

matriz = []
for i in range(p_d):
  matriz.append([0] * p_d)

for x in range(p_d): 
  for y in range(p_d): 
    if (x <= centro):
      matriz[x][y] = (x - centro, centro - y)
    elif (x > centro):
      matriz[x][y] = (((centro - x) * - 1), ((y - centro) * - 1))

for y in range (p_d):
  for x in range(p_d):
    xy = []
    xy = matriz[x][y]
    x = xy[0]
    y = xy[1]

    dist = ((x ** 2) + (y ** 2)) ** 0.5
  
    if (dist <= (p_d/2)):
      cells_circle = cells_circle + 1
  
out = (cells_circle/cells_square) * 4

print(out)
