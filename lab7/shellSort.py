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


def insertionSort(arr):
  n = len(arr)
  for i in range(n):
    j = i
    while j > 0 and arr[j] < arr[j-1]:
      arr[j], arr[j-1] = arr[j-1], arr[j]
      j -= 1
  return arr
      

def shellSort(arr, h = None):
  n = len(arr)
  if not h:
    h = n // 2
    
  while h > 0:
    for i in range(h,n):
      j = i
      while j - h >= 0 and arr[j] < arr[j-h]:
        arr[j], arr[j-h] = arr[j-h], arr[j]
        j -= h
    h = h // 2
  return arr

  
def testSorting(f):
    data = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
    nodes = [Node(p,q) for p,q in data]
    print(f(nodes))
  
def testTime(f):
  t_start = time.perf_counter()
  ans = f()
  t_stop = time.perf_counter()
  print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
  return ans

def generateRandomArray(n=10000, min=0, max=100):
  data = []
  for _ in range(n):
    data.append(int(random.random() * (max - min) + min))
  return data

def main():
  testSorting(insertionSort)
  print("Algorytm jest stabilny")
  testSorting(shellSort)
  print("Algorytm jest niestabilny")
  
  arr = generateRandomArray()
  
  testTime(lambda : insertionSort(arr[:]))
  testTime(lambda : shellSort(arr))

if __name__ == "__main__":
  main()