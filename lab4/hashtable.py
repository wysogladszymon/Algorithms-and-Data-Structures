keyWasDeleted = 'DEL'

class Node:
  def __init__(self, key, value):
    self.key = key
    self.value = value
    
  def __str__(self):
    return f'{self.key}:{self.value}'
    
    
class MixedList:
  def __init__(self, size, c1 = 1, c2 = 0):
    self.tab = [None for i in range(size)]
    self.c1 = c1
    self.c2 = c2
    self.size = size
    
  def h(self, k):
    if isinstance(k,str):
      counter = 0
      for ch in k:
        counter += ord(ch) 
      k = counter
    return k % self.size
  
  def H(self, k, i):
    return (self.h(k) + self.c1 * i + self.c2 * i ** 2) % self.size 
    
  def search(self, key):
    for i in range(self.size):
      index = self.H(key, i)
      node = self.tab[index]
      if isinstance(node,Node) and node.key == key:
        return node.value
      # if the key was deleted earlier
      if node == keyWasDeleted:
        continue
      if not node:
        print('Brak danej')
        return None
    print('Brak danej')
    return None
      
  
  def insert(self, key, value):
    node = Node(key, value)
    for i in range(self.size):
      index = self.H(key, i)
      el = self.tab[index]
      # if its free
      if not el or el == keyWasDeleted:
        self.tab[index] = node
        return
      if isinstance(el, Node) and el.key == key:
        self.tab[index] = node
        return
    print('Brak miejsca')
    return None
      
  
  def remove(self, key):
    for i in range(self.size):
      index = self.H(key, i)
      node = self.tab[index]
      if isinstance(node, Node) and node.key == key:
        self.tab[index] = keyWasDeleted 
        return
      if not node:
        break
    print('Brak danej')
    return None

  def __str__(self):
    res = '{'
    for elem in self.tab:
      if isinstance(elem, Node):
         res += f'{elem}, '
      else:
        res += 'None, '
    if len(res) < 3:
      return '{}'
    return res[:-2] + '}'
  
  
def test1(size=13, c1 = 1, c2 = 0):
  hashTable = MixedList(size, c1, c2)
  r = [x for x in range(1, 16)]
  r[5] = 18
  r[6] = 31
  data = {el: chr(ord('A') + i ) for i, el in enumerate(r)}
  
  for i in r:
    hashTable.insert(i, data[i])
    
  print(hashTable)
  print(hashTable.search(5))
  hashTable.search(14)
  hashTable.insert(5,'Z')
  print(hashTable.search(5))
  hashTable.remove(5)
  print(hashTable)
  hashTable.search(31)
  hashTable.insert('test', 'W')
  print(hashTable)
  print(hashTable.search('test'))
  
  
def test2(size=13, c1 = 1, c2 = 0):
  hashTable = MixedList(size, c1, c2)
  r = [x for x in range(0, 16 * 13, 13)]
  print(r)
  r[5] = 18 * 13
  r[6] = 31 * 13
  data = {element: chr(ord('A') + index ) for index, element in enumerate(r)}
  
  for i in r:
    hashTable.insert(i, data[i])
    
  print(hashTable)
  
  
def  main():
  test1(13,1,0)
  test2(13,1,0)
  test2(13, 0, 1)
  test1(13,0,1)
  
  
if __name__ == "__main__":
  main()