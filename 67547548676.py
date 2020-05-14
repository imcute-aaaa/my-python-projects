class Grid:
  def __init__(self,rows,cols):
    self.val=[[None]*rows]*cols


class Cube:
  def __init__(self, wid, hei, dep):
    self.val = [[[None]*wid]*hei]*dep
