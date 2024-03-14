

def realloc(tab, size):
    oldSize = len(tab)
    return [tab[i] if i<oldSize else None  for i in range(size)]

class FIFO:
  def __init__(self) -> None:
    self.head = 0
    self.tail = 0
    self.size = 5
    self.tab = [None for i in range(self.size)]
    
  def is_empty(self) -> bool:
    return self.tail == self.head
  
  def peek(self):
    if self.tail == self.head and self.tab[self.tail] is None:
      return None
    return self.tab[self.head]

  def dequeue(self):
    if self.tail == self.head and self.tab[self.head] is None:
      return None
    ret = self.tab[self.head]
    self.tab[self.head] = None
    self.head += 1
    self.head = self.head % self.size
    return ret
  
  def enqueue(self, item):
    self.tab[self.tail] = item
    self.tail += 1
    self.tail = self.tail % self.size
    if self.tail == self.head and self.tab[self.tail] is not None:
      move = self.tab[self.tail:]
      oldSize = self.size
      self.size *= 2
      self.tab = realloc(self.tab, self.size)
      self.tab[oldSize + self.tail:] = move
      self.tab[self.tail:oldSize] = [None] * (oldSize - self.tail)
      self.head = oldSize + self.tail
  
  def __str__(self):
    res = "["
    i = self.head
    if self.head == self.tail:
      return "[]"
    while i != self.tail:
      res += f"{self.tab[i]}, "
      i += 1
      i = i % self.size
       
    return res[:-2] +']'
    