import sympy
from enum import Enum, auto

class BeamElement():
  def __init__(self, length, start, load=0):
    self.length = length
    self.start = start
    self.load = load
    self.load_strength = 0
    self.load_pos = 0

    self.shear_force = None
    self.moment = None
    self.angle = None
    self.deflection = None

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
    for elem in self.elements:
      self.balance_vertical += elem.convert_load(self.x)[0]
    for node in self.nodes:
      
