import sympy

def main():
  integ = sympy.integrate(sympy.symbols("x"), (sympy.symbols("x"), 0, sympy.symbols("x")))
  print(integ)

if __name__ == "__main__":
  main()