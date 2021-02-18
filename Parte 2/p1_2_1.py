numbers = [2, 7, 3, 9, 13]

if (not numbers):
   print("None")

tam = len(numbers)

for i in range(tam):
   out = (numbers[0] + numbers[1] + numbers[2] + numbers[3] + numbers[4]) / tam 

print(out)