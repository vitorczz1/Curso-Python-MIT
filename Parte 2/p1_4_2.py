
poly = [0, 0, 1/2]  # representando 1/2 x^2

const = 5

out = []

tam = len(poly)

if poly != 0:
   out.append(const)

   for i in range(tam):
       result = (poly[i] / (i + 1))
       out.append(result)

print(out)