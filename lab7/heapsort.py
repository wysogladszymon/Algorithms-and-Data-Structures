from typing import List
import random
import time


class Node:
  def __init__(self, priority, data):
    self.__data = data
    self.__priority = priority
    
  def __lt__(self, other : "Node"):
    return self.__priority < other.__priority
  
  def __gt__(self, other : "Node"):
    return self.__priority > other.__priority 
  
  def __repr__(self):
    return f'{self.__priority} : {self.__data}' if self.__data else str(self.__priority)

class PriorityQueue:
  def __init__(self, nodes = None):
    self.arr : List["Node"] = nodes if nodes else []
    self.size = len(self.arr)
    self.__makeHeap()
  
  def is_empty(self):
    return self.size == 0
  
  def peek(self):
    if (self.is_empty()):
      return None
    return self.arr[0]
  
  def __makeHeap(self):
    i = self.parent(self.size - 1)
    while i >= 0:
      self.fix(i)
      i -= 1
    return self.arr
  
  def heapSort(self):
    x = self.size
    while x > 0:
      self.dequeue()
      x -= 1
    return self.arr
  
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

def test1():
  data = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
  nodes = [Node(p,d) for p,d in data]
  heap = PriorityQueue(nodes)
  heap.print_tab()
  heap.print_tree()
  l = heap.heapSort()
  print(l) 
  
  
def test2():
  data = []
  for i in range(10000):
    data.append(int(random.random() * 100)) 
  t_start = time.perf_counter()
  q = PriorityQueue(data)
  q.heapSort()
  t_stop = time.perf_counter()
  print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
  
def swapSort(l : List):
  n = len(l)
  for i in range(n):
    min = l[i]
    for j in range(i,n):
      if min > l[j]:
        l[j], l[i] = l[i], l[j]
        min = l[j]
  return l
    
def shiftSort(l : List):
  n = len(l)
  for i in range(n):
    min = l[i]
    for j in range(i,n):
      if min > l[j]:
        min = l[j]
        l.insert(i, l.pop(j))
  return l
    
def test3():
  data = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
  data2 = data[:]
  print(swapSort(data))
  print(shiftSort(data2))
  
def test4():
  data = []
  for i in range(10000):
    data.append(int(random.random() * 100)) 
  data2 = data[:]
  
  t_start = time.perf_counter()
  swapSort(data)
  t_stop = time.perf_counter()
  print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

  t_start = time.perf_counter()
  shiftSort(data2)
  t_stop = time.perf_counter()
  print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
  
  
def main():
  test1()
  test2()
  test3()
  test4()
  
if __name__ == "__main__":
  main()