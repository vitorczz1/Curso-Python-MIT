
a = 1
b = 2
c = 3

delta = (b ** 2) - (4 * a * c)

positivo = (-b + (delta ** 0.5)) / (2 * a)

negativo = (-b - (delta ** 0.5)) / (2 * a)

if (a != 0):
   out = positivo, negativo

print(out)