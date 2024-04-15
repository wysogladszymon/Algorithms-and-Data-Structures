from typing import List



class Node:
  def __init__(self, priority, data):
    self.__data = data
    self.__priority = priority
    
  def __lt__(self, other : "Node"):
    return self.__priority < other.__priority
  
  def __gt__(self, other : "Node"):
    return self.__priority > other.__priority
  
  def __repr__(self):
    return f'{self.__priority} : {self.__data}'

class PriorityQueue:
  def __init__(self):
    self.arr : List[Node] = []
    self.size = 0
  
  def is_empty(self):
    return self.size == 0
  
  def peek(self):
    if (self.is_empty()):
      return None
    return self.arr[0]
    
  def fix(self, index = 0):
    while True:
      left = self.left(index)
      right = self.right(index)
      parent = index
      
      if left < self.size and self.arr[left] > self.arr[parent]:
        parent = left
      if right < self.size and self.arr[right] > self.arr[parent]:
        parent = right 
        
      if parent != index:
        self.arr[index], self.arr[parent] = self.arr[parent], self.arr[index]
        index = parent
      else:
        break
    
  def dequeue(self):
    if (self.is_empty()):
      return None
    self.size -= 1
    #swap two elements
    self.arr[0], self.arr[self.size] = self.arr[self.size], self.arr[0]
    self.fix(0)
    return self.arr[self.size]
  
  def enqueue(self, node : Node):
    if len(self.arr) == self.size:
      self.arr.append(node)
    else:
      self.arr[self.size] = node
    index = self.size
    self.size += 1
    pIndex = self.parent(index)
    
    while (index > 0 and node > self.arr[pIndex]):
      self.arr[index], self.arr[pIndex] = self.arr[pIndex], node 
      index = pIndex
      pIndex = self.parent(index)
      
  
  def left(self, idx : int):
    return 2 * idx + 1
  
  def right(self, idx):
    return 2 * idx + 2
  
  def parent(self, idx):
    return (idx - 1) // 2
  
  def print_tab(self):
    print ('{', end=' ')
    print(*self.arr[:self.size], sep=', ', end = ' ')
    print( '}')
    
  def print_tree(self, idx = 0, lvl = 0):
    if idx<self.size:           
      self.print_tree(self.right(idx), lvl+1)
      print(2*lvl*'  ', self.arr[idx] if self.arr[idx] else None)           
      self.print_tree(self.left(idx), lvl+1)

  
def main():
  q = PriorityQueue()
  priorities = [7, 5, 1, 2, 5, 3, 4, 8, 9]
  values = "GRYMOTYLA"
  for i in range(len(priorities)):
    n = Node(priorities[i], values[i])
    q.enqueue(n)
  q.print_tree()
  q.print_tab()
  d = q.dequeue()
  print(q.peek())
  q.print_tab()
  print(d)
  while not q.is_empty():
    q.dequeue()
  q.print_tab()

  
if __name__ == "__main__":
  main()