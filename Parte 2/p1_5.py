size = 'small'
toppings = ['presunto', 'abacaxi']

#m
if (size == 'small'):
   custoinicial = 14

if (size == 'medium'):
   custoinicial = 16

if (size == 'large'):
   custoinicial = 18

#n
primeiracobert = 0
segundacobert = 1
terceiracobert = 2

custo1 = (12 + primeiracobert + len(toppings[0])) / 100 #0.2
custo2 = (12 + segundacobert + len(toppings[1])) / 100 #0.2

custotopping1 = custoinicial * custo1 #2.8

parcial = custoinicial + custotopping1 #14+2.8 = 16.8

custotopping2 = parcial * custo2 #3,36

custo = custoinicial + custotopping1 + custotopping2

out = round(custo, 2)

for i in range(2):
    if (toppings[i] == 'anchovas' or 'bacon'):
       custo += (custo * (20/100))

print(out)

