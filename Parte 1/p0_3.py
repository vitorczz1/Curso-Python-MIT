kwh_used = 1000

custo1 = 0.45
custo2 = 0.74
custo3 = 1.25
custo4 = 2.00

if (kwh_used <= 500):
    out = custo1 * kwh_used
    #(0.45 * 1000)

if (kwh_used > 500 and kwh_used <= 1500):
    out = ((kwh_used - 500) * custo2) + (custo1 * 500)
    #(0.74 * 1000) + 20%

if (kwh_used > 1500 and kwh_used <= 2500):
    out = ((kwh_used - 1500) * custo3) + ((custo1 * 500) + (custo2 * 1000))
    #(1.25 * 1000) + 20%

if (kwh_used > 2500):
    out = ((kwh_used - 2500) * custo4) + ((custo1 * 500) + (custo2 * 1000) + (custo3 * 1500))
    #(2.00 * 1000) + 20%

#out = 595 + 20% = 714

taxa = out * (20 / 100)

out += taxa

print(out)