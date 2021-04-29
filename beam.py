import sympy

class BeamElement():
  def __init__(self):
    self.length = length
    self.start = 0
    
    self.reaction_force = [None, None]
    self.reaction_moment = [None, None]
    self.external_force = [None, None]
    self.external_moment = [None, None]
    self.distributed_load = None

    self.condition_diflection = [None, None]
    self.condition_angle = [None, None]

class Beam():
  def __init__(self):
    self.beams = list()
    self.element_num = 0

  def append(self, elem, type=None):
    self.beams.append(elem)
    self.element_num += 1