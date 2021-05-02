import sympy
from enum import Enum, auto

class BeamElement():
  class Force():
    def __init__(self, strength, pos):
      self.strength = strength
      self.pos = pos

  def __init__(self, length, start, load=0):
    self.length = length
    self.start = start
    self.load = load
    self.shear_force = None
    self.moment = None
    self.angle = None
    self.deflection = None

  def convert_load(self, x, start=self.start, end=(self.start + self.length)):
    if not self.load:
      return BeamElement.Force(0, 0)

    integ = sympy.integrate(self.load, (x, start, end))
    if not integ:
      return BeamElement.Force(0, 0)

    integ_x = sympy.integrate(self.load * x, (x, start, end))
    
    return BeamElement.Force(integ, integ_x / integ)

class BeamNode():
  def __init__(self, rf=0, rm=0, ef=0, em=0):
    self.reaction_force = rf
    self.reaction_moment = rm
    self.external_force = ef
    self.external_moment = em

class Beam():
  def __init__(self):
    self.elements = list()
    self.nodes = list()
    self.element_num = 0
    self.x = None
    self.balance_vertical = None
    self.balance_moment = None

  def create_beam(self, x, elements, nodes):
    if len(elements) != len(nodes + 1):
      raise IndexError()

    self.x = x
    self.element_num = len(elements)
    self.elements = elements
    self.nodes = nodes

  def calc_balance(self):
    self.balance_vertical = 0
    self.balance_moment = 0
    for elem in self.elements:
      self.balance_vertical += elem.convert_load(self.x).strength
      self.balance_moment += (elem.convert_load(self.x).strength * elem.convert_load(self.x).pos)
    for node in self.nodes:
      self.balance_vertical += (node.reaction_force + node.external_force)
      self.balance_moment += (node.reaction_moment + node.external_moment)
    
  def calc_shear_force(self):
  prev_expr = 0
    for elem in self.elements:
      self.
    