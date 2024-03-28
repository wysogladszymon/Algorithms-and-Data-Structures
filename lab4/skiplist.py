import random

def displayList_(self):
  node = self.head.tab[0]  # pierwszy element na poziomie 0
  keys = [ ]                        # lista kluczy na tym poziomie
  while node is not None:
      keys.append(node.key)
      node = node.tab[0]
  for lvl in range(self.maxLevel - 1, -1, -1):
      print(f"{lvl}  ", end=" ")
      node = self.head.tab[lvl]
      idx = 0
      while node is not None:
          while node.key > keys[idx]:
              print(end=5*" ")
              idx += 1
          idx += 1
          print(f"{node.key:2d}:{node.value:2s}", end="")
          node = node.tab[lvl]
      print()
      
      
def randomLevel(p, maxLevel):
  lvl = 1   
  while random.random() < p and lvl <maxLevel:
        lvl = lvl + 1
  return lvl

class Node:
  def __init__(self, key, value, level):
    self.key = key
    self.value = value
    self.tab = [None] * level
    
  def __str__(self):
    return f'{self.key}:{self.value}'

class SkipiList:
  def __init__(self, height):
    self.head = Node(None, None, height)
    self.maxLevel = height

  def search(self, key):
    node = self.head
    level = self.maxLevel - 1
    while level >= 0:
      while node.tab[level] and node.tab[level].key <= key:
        node = node.tab[level]
      level -= 1
      if node.key == key:
        return node.value
    return None
      
  def insert(self, key, value):
    if not self.head.key:
      self.head = Node(key, value, self.maxLevel)
      return
    else:
      level = self.maxLevel 
      update = [self.head] * level
      level -= 1
      node = self.head
      while level >= 0:
        while node.tab[level] and node.tab[level].key <= key:
          node = node.tab[level]
        update[level] = node
        level -= 1
        if node.key == key:
          node.value = value
          return 
      randomLvl = randomLevel(0.5, self.maxLevel)
      n = Node(key, value, randomLvl)
      for i in range(randomLvl):
        n.tab[i] = update[i].tab[i]
        update[i].tab[i] = n
  
  def remove(self, key):
    level = self.maxLevel
    update = [self.head] * level
    level -= 1
    node = self.head
    while level >= 0:
      while node.tab[level] and node.tab[level].key < key:
        node = node.tab[level]
      update[level] = node
      level -= 1
    if node.tab[0].key == key:
      node = node.tab[0]
      for i in range(len(node.tab)):
        update[i].tab[i] = node.tab[i]
        node.tab[i] = None

  
  def __str__(self):
    res = "["
    node = self.head
    if not node:
      return "[]"
    while node:
      res += f'{node}, '
      node = node.tab[0]
    return res[:-2] + ']'
  
def test(r):
  maxLvl = 6
  slist = SkipiList(maxLvl)
  for i in r:
    slist.insert(i, chr(64+i))
  print(slist)
  displayList_(slist)
  print(slist.search(2))
  slist.insert(2,'Z')
  print(slist.search(2))
  for i in range(5,8):
    slist.remove(i)
  print(slist)
  slist.insert(6, "W")
  print(slist)  

def main():
  random.seed(42)
  r = range(1,16)
  test(r)
  # test()
  test(r[::-1])
  

if __name__ == "__main__":
    main()