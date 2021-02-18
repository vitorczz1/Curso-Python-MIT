def approx_derivative_2 (f, delta = 1e-6): 
  return lambda x: (f(x + delta) - f(x - delta))/(2*delta)

def approx_derivative(f, x, delta = 1e-6): 
  dividend = f(x + delta) - f(x - delta)
  divisor = 2*delta
  return dividend/divisor

def approx_integral(f, lo, hi, num_regions):
    value = 0
    h = (hi - lo)/num_regions
    x = (lo + h)
    contador = 1
    while (contador != num_regions):
      value += f(x)
      x += h 
      contador += 1
    aproximacao_integral = (( f(lo) + f(hi))/ 2 + value)
    aproximacao_integral *= h
    return aproximacao_integral