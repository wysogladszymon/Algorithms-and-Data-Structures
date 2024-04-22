from typing import List

class Node:
  def __init__(self, maxChildren):
    self.keys : List = [None] * (maxChildren - 1)
    self.children = [None] * maxChildren
    self.maxChildren = maxChildren
    self.size = 0
    
  def isLeaf(self):
    return self.children[0] is None
  
  def isFull(self):
    return self.size >= self.maxChildren - 1
  
  def findIndex(self, key):
    for i in range(self.size):
      if key < self.keys[i]:
        return i
    return self.size

  def split(self):
    mid = (self.maxChildren -1 ) // 2
    midKey = self.keys[mid]
    
    left = Node(self.maxChildren)
    right = Node(self.maxChildren)

    left.size = mid
    left.keys[:mid] = self.keys[:mid]
    
    right.size = self.size - mid - 1
    right.keys[:right.size] = self.keys[mid + 1:]
    
    if not self.isLeaf():
      left.children[:mid + 1] = self.children[:mid + 1]
      right.children[:right.size + 1] = self.children[mid + 1:self.size + 1]

    return left, midKey, right
  
  def append2Leaf(self, key):
    if not self.isFull():
      i = self.findIndex(key)
      self.size += 1
      self.keys[i+1:self.size] = self.keys[i:self.size-1]
      self.keys[i] = key
      return self
    else:
      left, mid, right = self.split()
      if key < mid:
          left.append2Leaf(key)
      else:
          right.append2Leaf(key)
      return left, mid, right
    
  def appendMid(self, key, left, right):
    if not self.isFull():
      i = self.findIndex(key)
      self.size += 1
      self.keys[i+1:self.size] = self.keys[i:self.size-1]
      self.keys[i] = key
      self.children[i+2:self.size+1] = self.children[i+1:self.size]
      self.children[i] = left
      self.children[i+1] = right
      return self
    else:
      l, midKey, r = self.split()
      if key < midKey:
        l.appendMid(key, left, right)
      else:
        r.appendMid(key, left, right)
      return l, midKey, r
      
  def __repr__(self):
    return self.keys.__str__()
      

class BTree:
  def __init__(self, maxChildren):
    self.root = Node(maxChildren)
    self.maxChildren = maxChildren
    
  def __insert(self, node: "Node", key):
    if node.isLeaf():
      result = node.append2Leaf(key)
      return result
    else:
      i = node.findIndex(key)
      res = self.__insert(node.children[i], key)
      if isinstance(res, tuple):
        return node.appendMid(res[1], res[0], res[2])
      return node
  
  
  def insert(self, key):
    res = self.__insert(self.root, key)
    if isinstance(res,tuple):
      self.root = Node(self.maxChildren)
      self.root.size = 1
      self.root.keys[0] = res[1]
      self.root.children[0] = res[0]
      self.root.children[1] = res[2] 
    else:  
      self.root = res

  def print_tree(self):
    print("==============")
    self._print_tree(self.root, 0)
    print("==============")

  def _print_tree(self, node, lvl):
    if node!=None:
      for i in range(node.size+1): 	                	
        self._print_tree(node.children[i], lvl+1)
        if i<node.size:
          print(lvl*'  ', node.keys[i])

def test1():
  maxChildren = 4
  tree1 = BTree(maxChildren)
  l1 = [5, 17, 2, 14, 7, 4, 12, 1, 16, 8, 11, 9, 6, 13, 0, 3, 18 , 15, 10, 19]
  for i in l1:
    tree1.insert(i)
  tree1.print_tree()
  
  tree2 = BTree(maxChildren)
  for i in range(20):
    tree2.insert(i)
  tree2.print_tree()
  for i in range(20, 200):
    tree2.insert(i)
  tree2.print_tree()
  
  maxChildren = 6
  tree3 = BTree(maxChildren)
  for i in range(200):
    tree3.insert(i)
  tree3.print_tree()
  
  
def nodeTest():
  maxChildren = 5
  n = Node(maxChildren)
  for i in range(4):
    n.append2Leaf(i)
  left, mid, right = n.split()
  print(left)
  print(left.size)
  print(mid)
  print(right)
  n1 = Node(maxChildren)
  n1.appendMid(mid, left, right)
  print(n1.keys)
  print(n1.children)


def myBtreeTest():
  maxChildren = 4
  tree1 = BTree(maxChildren)
  end = 10
  for i in range(end):
    tree1.insert(i)
  tree1.print_tree()
  
def main():
  # nodeTest()
  test1()
  # myBtreeTest()

if __name__ == "__main__":
  main()