class Node:
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.left = None
    self.right = None

  def __str__(self):
    return f'{self.key}:{self.value}'

class BST:
  def __init__(self):
    self.root = None
    
  def search(self, key):
    n = self.__search(self.root, key)
    return n
    
  def __search(self, node , key):
    "recursion"
    if not node:
      return None
    
    if key < node.key:
      return self.__search(node.left ,key)
    elif key > node.key:
      return self.__search(node.right, key)
    else:
      # key == node.key
      return node.value      
  
  def insert(self, key, value):
    return self.__insert(self.root, key, value)
  
  def __insert(self, node , key, value):
    if not self.root:
      self.root = Node(key, value)
      return node
    if not node:
      node = Node(key, value)
      return node
    if key < node.key:
      node.left = self.__insert(node.left, key, value)
      return node
    elif key > node.key:
      node.right = self.__insert(node.right, key, value)
      return node
    else:
      # key == node.key
      node.value = value
      return node      
      
  def delete(self, key):
    self.__delete(self.root, key)
    
  def __delete(self, node , key):
    "have to finish"
    if not node:
      return None
    if key < node.key:
      node.left = self.__delete(node.left,key)
      return node
    elif key > node.key:
      node.right = self.__delete(node.right, key)
      return node
    else:
      # key == node.key
      # 0 or 1 children
      if not node.left or not node.right:
        return node.left if node.left else node.right
      # 2 children
      else:
        n = node.right
        #min value on the right
        while n.left:
          n = n.left
        node.key = n.key
        node.value = n.value
        node.right = self.__delete(node.right, n.key)                
        return node
          
  
  def print(self):
    print(self)
  
  def height(self):
    max = 0
    def dfs(node , height):
      nonlocal max
      if not node:
        return
      height += 1
      if height > max:
        max = height
      
      dfs(node.left, height)
      dfs(node.right, height)
    dfs(self.root, 0)
    return max
      
  
  def print_tree(self):
    print("==============")
    self.__print_tree(self.root, 0)
    print("==============")

  def __print_tree(self, node, lvl):
    if node!=None:
      self.__print_tree(node.right, lvl+5)
      print()
      print(lvl*" ", node.key, node.value)
      self.__print_tree(node.left, lvl+5)
  
  def __str__(self):
    d = {}

  def __str__(self):
    d = ""
    def dfs(node ):
      nonlocal d
      if not node:
        return
      else:
        dfs(node.left)
        d += f'{node.key} {node.value},'
        dfs(node.right)
    dfs(self.root)
    return d
    

def main():
  t = BST()
  data = {50:'A', 15:'B', 62:'C', 5:'D', 20:'E', 58:'F', 91:'G', 3:'H', 8:'I', 37:'J', 60:'K', 24:'L'}
  for key, val in data.items():
    t.insert(key, val)
  t.print_tree()
  t.print()  
  print(t.search(24))
  t.insert(20,"AA")
  t.insert(6,"M")
  t.delete(62)
  t.insert(59,"N")
  t.insert(100, "P")
  t.delete(8)
  t.delete(15)
  t.insert(55,"R")
  t.delete(50)
  t.delete(5)
  t.delete(24)
  print(t.height())
  t.print()
  t.print_tree()

if __name__ == "__main__":
  main()