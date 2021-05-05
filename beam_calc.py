from sympy import *

def simplify_mm(expr):
  x = symbols("x")
  ei = symbols("E") * symbols("I")
  expr = expand(expr)
  expr = collect(expr, x)
  expr = expand(expr)
  return expr

def main():
  ra = symbols("R_A")
  rd = symbols("R_D")
  w = symbols("w")
  l = symbols("l")
  ma = symbols("M_A")
  md = symbols("M_D")
  x = symbols("x")
  ei = symbols("E") * symbols("I")
  c1 = symbols("C_1")
  c2 = symbols("C_2")
  c3 = symbols("C_3")
  c4 = symbols("C_4")
  d = symbols("d")
  
  balance_force = Eq(ra + rd - w*l, 0)
  balance_moment1 = Eq(ma + Rational(1, 2)*w*l**2 - ra*l, 0)
  balance_moment2 = Eq(rd*l - md, 0)
  
  mab = (-1*Rational(1, 2)*w*x**2 + ra*x - ma)*-1
  mcd = (-rd*x + 2*rd*l - md)*-1

  iab = -1/ ei * (integrate(mab, x) + c1)
  yab = integrate(iab, x) + c2
  icd = -1 / ei * (integrate(mcd, x) + c3)
  ycd = integrate(icd, x) + c4

  apply_list = [iab, yab, icd, ycd]

  for expr in apply_list:
    expr = simplify_mm(expr)
    pprint(expr, order="ilex")

  const_list = [c1, c2, c3, c4]
  pos_list = [0, 0, 2*l, 2*l]
  
  for i in range(4):
    const = solve(Eq(apply_list[i].subs(x, pos_list[i]), 0), const_list[i])[0]
    for j in range(4):
      apply_list[j] = apply_list[j].subs(const_list[i], const)
    const_list[i] = const
    pprint(const_list[i])

  pprint(apply_list)

  solves = solve([balance_force, balance_moment1, balance_moment2, Eq(apply_list[1].subs(x, l), apply_list[3].subs(x, l))], [ra, rd, ma, md])
  pprint(solves)

  """
  c1 = solve(Eq(iab.subs(x, 0), 0), c1)[0]
  c2 = solve(Eq(yab.subs(x, 0), 0), c2)[0]

  c3_ = solve(Eq(icd.subs(x, 2*l), 0), c3)[0]
  ycd = ycd.subs(c3, c3_)
  c3 = c3_
  c4 = solve(Eq(ycd.subs(x, 2*l), 0), c4)[0]

  pprint(c3)
  pprint(c3_)
  pprint(c4)"""

if __name__ == "__main__":
  main()