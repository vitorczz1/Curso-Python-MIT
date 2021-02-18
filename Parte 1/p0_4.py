import math

year = 2017
month = 1  # 1 = janeiro, 2 = fevereiro, ..., 12 = dezembro
day = 9

if (month == 1 or 2):
    year = year - 1     #2016
    month = month + 12   #13

if (month != 1 or 2):
    year = year
    month = month

y2 = year % 100
c = math.floor(year / 100)

out = (day + math.floor(13 * (month + 1) / 5) + y2 + math.floor(y2 / 4) + math.floor(c / 4) - 2 * c) % 7

print(out)