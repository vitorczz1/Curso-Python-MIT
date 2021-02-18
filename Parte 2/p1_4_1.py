
poly = [0, 0, 1/2]  # representando 1/2 x^2

out = []

for i in range (1, len(poly)):
    out.append(int(poly[i] * (i + 1)))

print(out)