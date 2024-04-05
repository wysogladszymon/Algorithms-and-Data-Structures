from typing import Union
maxDiff = 1

class Node:
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.left = None
    self.right = None
    self.height = 1

  def __str__(self):
    return f'{self.key} {self.value}'

class AVL:
  def __init__(self):
    self.root = None
    
  def search(self, key):
    n = self.__search(self.root, key)
    return n
    
  def __search(self, node : Union[Node, None], key):
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
    self.root = self.__insert(self.root, key, value)
  
  def __insert(self, node : Union[Node, None], key, value):
    if not node:
      node = Node(key, value)
    if key < node.key:
      node.left = self.__insert(node.left, key, value)
    elif key > node.key:
      node.right = self.__insert(node.right, key, value)
    else:
      # key == node.key
      node.value = value
    node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
    balance = self.getBalance(node)
    # Right Right
    if balance < -maxDiff and self.getBalance(node.left) < 0:
      return self.rightRotate(node)
    
    # Left Left
    if balance > maxDiff and self.getBalance(node.right) > 0:
      return self.leftRotate(node)
    
    # Left Right
    if balance < -maxDiff and self.getBalance(node.left) > 0:
      node.left = self.leftRotate(node.left)
      return self.rightRotate(node)
    
    # Right Left
    if balance > maxDiff and self.getBalance(node.right) < 0:
      node.right = self.rightRotate(node.right)
      return self.leftRotate(node)
    
    return node

  def delete(self, key):
    self.__delete(self.root, key)
    
  def __delete(self, node : Union[Node, None], key):
    "have to finish"
    if not node:
      return None
    if key < node.key:
      node.left = self.__delete(node.left,key)
    elif key > node.key:
      node.right = self.__delete(node.right, key)
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
      
    node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
    balance = self.getBalance(node)
    # Right Right
    if balance < -maxDiff and self.getBalance(node.left) < 0:
      return self.rightRotate(node)
    
    # Left Left
    if balance > maxDiff and self.getBalance(node.right) > 0:
      return self.leftRotate(node)
    
    # Left Right
    if balance < -maxDiff and self.getBalance(node.left) > 0:
      node.left = self.leftRotate(node.left)
      return self.rightRotate(node)
    
    # Right Left
    if balance > maxDiff and self.getBalance(node.right) < 0:
      node.right = self.rightRotate(node.right)
      return self.leftRotate(node)
    
    return node
  
  def leftRotate(self, z):  
    y = z.right
    d = y.left
    
    z.right = d
    y.left = z

    z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
    y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
    return y 
  
  def rightRotate(self, z): 
    y = z.left
    d = y.right
    
    z.left = d
    y.right = z
    
    z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
    y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
    return y
  
          
  def getHeight(self, node): 
    if not node: 
      return 0
    return node.height 
  
  def getBalance(self, node): 
    if not node: 
      return 0
    return self.getHeight(node.right) - self.getHeight(node.left) 
  
  
  
  def print(self):
    print(self)
  
  def height(self):
    max = 0
    def dfs(node : Union[Node, None], height):
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

    def dfs(node : Union[Node, None]):
      nonlocal d
      if not node:
        return
      else:
        d[node.key] = node.value
        dfs(node.left)
        dfs(node.right)
    dfs(self.root)
    d = dict(sorted(d.items()))
    res = ""
    for key, val in d.items():
      res +=f'{key} {val},'
    return res
    

def main():
  t = AVL()
  data =  {50:'A', 15:'B', 62:'C', 5:'D', 2:'E', 1:'F', 11:'G', 100:'H', 7:'I', 6:'J', 55:'K', 52:'L', 51:'M', 57:'N', 8:'O', 9:'P', 10:'R', 99:'S', 12:'T'}
  for key, val in data.items():
    t.insert(key, val)
  t.print_tree()
  t.print()  
  print(t.search(10))
  t.delete(50)
  t.delete(52)
  t.delete(11)
  t.delete(57)
  t.delete(1)
  t.delete(12)
  t.insert(3,"AA")
  t.insert(4,"BB")
  t.delete(7)
  t.delete(8)
  t.print_tree()
  t.print()
  
  
if __name__ == "__main__":
  main()