interest_rate = 1 #100%
out = 2 #tempo

if (interest_rate != 0):
   aux = 0

   while (out <= 2):
      out = out * (1 + interest_rate)
      aux = aux + 1
   out = aux
   print(out)

if (interest_rate == 0):
   out = ("NEVER")
   print(out)