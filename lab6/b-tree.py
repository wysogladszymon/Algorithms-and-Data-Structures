# from typing import List

class Node:
  def __init__(self, maxChildren):
    self.keys = [None] * (maxChildren - 1)
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
    mid = self.maxChildren // 2
    midKey = self.keys[mid]
    
    left = Node(self.maxChildren)
    right = Node(self.maxChildren)
    
    left.keys = self.keys[:mid] + [None] * (self.maxChildren - 1 - mid)
    left.size = mid
    
    right.keys = self.keys[mid+1:] + [None] * (mid)
    right.size = self.size - mid - 1
    if not self.isLeaf():
      left.children = self.children[:mid + 1] + [None] * (self.maxChildren - mid - 1)
      right.children = self.children[mid + 1:self.size + 1] + [None] * (mid)

    self.keys = [None] * (self.maxChildren - 1)
    self.children = [None] * self.maxChildren
    self.size = 0

    return left, self.keys[mid], right
  
  def append2Leaf(self, key):
    if not self.isFull():
      i = self.findIndex(key)
      self.size += 1
      self.keys = self.keys[:i] + [key] + self.keys[i:-1]
      return self
    else:
      return self.split()
    
        
  def appendMid(self, key, left, right):
    if not self.isFull():
      i = self.findIndex(key)
      self.size += 1
      self.keys = self.keys[:i] + [key] + self.keys[i:-1]
      self.children = self.children[:i] + [left, right] + self.children[i:-1]
      return self
    else:
      i = self.findIndex(key)
      k = self.keys.copy()
      k.insert(i, key)
      
  
  def __repr__(self):
    return self.keys.__str__()
      

class BTree:
  def __init__(self, maxChildren):
    self.root = Node(maxChildren)
    self.maxChildren = maxChildren
    
  def __insert(self,node : "Node",key):
    if node.isLeaf():
      return node.append2Leaf(key)
    i = node.findIndex(key)
    print(key)
    print(i)
    print(node.children)
    print(node)
    res = self.__insert(node.children[i], key)
    if isinstance(res,tuple):
      return node.appendMid(res[1], res[0], res[2])
      
  
  def insert(self, key):
    res = self.__insert(self.root, key)
    if isinstance(res,tuple):
      self.root.appendMid(res[1], res[0], res[2])
      return      
    self.root = res
    
  def __splitChild(self, parent, index):
    child = parent.children[index]
    left, mid_key, right = child.split()
    for j in range(parent.size, index, -1):
      parent.keys[j] = parent.keys[j - 1]
      parent.children[j + 1] = parent.children[j]
    parent.keys[index] = mid_key
    parent.children[index] = left
    parent.children[index + 1] = right
    parent.size += 1

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
  for i in l1[:4]:
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
  maxChildren = 4
  n = Node(maxChildren)
  for i in range(4):
    n.append2Leaf(i)
  print(n)
  
def main():
  nodeTest()

if __name__ == "__main__":
  main()