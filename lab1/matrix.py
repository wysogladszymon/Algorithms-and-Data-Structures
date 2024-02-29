from typing import List, Tuple, Union

class Matrix:
  def __init__(self, lists, a=0): 
    if (isinstance(lists,tuple)):
      r, c = lists
      self._matrix = [[a]* c for x in range(r)]
    else:
      if len(lists) == 0:
        self._matrix == [[]]
      else:
        length = len(lists[0])
        for row in lists:
          if len(row) != length:
            raise ValueError('Lists should have same length')
        self._matrix = lists

  def size(self):
    return len(self._matrix), len(self._matrix[0]) 
  
  def __getitem__(self, indeks):
       if isinstance(indeks, tuple):
           wiersz, kolumna = indeks
           return self._matrix[wiersz][kolumna]
       elif isinstance(indeks, int):
           return self._matrix[indeks]
       else:
           raise TypeError('Wrong indices of array!')

  def __add__(self, other):
    size = self.size() 
    if size != other.size():
      raise ValueError('Matrices have different shapes')
    res = []
    for r in range(size[0]):
      row = []
      for c in range(size[1]):
        row.append(self[r,c] + other[r,c])
      res.append(row)
    return Matrix(res)
  
  def __mul__(self, other):
    r1, c1 = self.size()
    r2, c2 = other.size()
    if c1 != r2:
      raise ValueError('Matrices cannot be multiplied! Wrong shapes!')
    l = []
    for r in range(r1):
      row = []
      for c in range(c2):
        m = 0
        for i in range(c1):
          m += self[r, i] * other[i, c]
        row.append(m)
      l.append(row)

    return Matrix(l)
  
  def __str__(self):
    rows, cols = self.size()
    s = ''
    for r in range(rows):
      s += '|'
      for c in range(cols):
          s += '{:5d} '.format(self[r][c])
      if r == rows - 1:
        s+= '|'
      else:  
        s+= '|\n'      
    return s
  
  def transpose(self):
    rows, cols = self.size()
    
    res = Matrix((cols, rows), 0)
    for r in range(rows):
      for c in range(cols):
        res[c][r] = self[r][c]
    return res




  
    

    


