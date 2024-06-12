from typing import List

def generateAllSuffixes(word : str):
  suffixes = []
  w = ''
  i = len(word) -1
  while i >= 0:
    w = word[i] + w
    suffixes.append(w)
    i -=1
  
  return suffixes[::-1]

class Node:
  def __init__(self, key, children):
    self.key = key
    self.children : List = children 
    self.size = 0

  def addChildren(self, child):
    self.children.append(child)
    self.size += 1

  def childExists(self, childKey):
    for child in self.children:
      if child.key == childKey:
        return True, child
    return False, None
  
  def isLeaf(self):
    return len(self.children) == 0
  
  def __str__(self):
    return f'{self.key}'
  
  def __repr__(self):
    return self.__str__()
  
  def merge(self, other : "Node"):
    self.children.remove(other)
    self.key += other.key
    self.children.extend(other.children)

class SuffixTree:
  def __init__(self, word):
    self.suffixes = generateAllSuffixes(word)
    self.root = Node('', [])
    self.createTree()
    self.compressTree()

  def createTree(self):
    node = self.root
    for word in self.suffixes:
      node = self.root

      for sign in word:
        exists, child = node.childExists(sign)        
        if exists:
          node = child
        else:
          n = Node(sign, [])
          node.addChildren(n)
          node = n

  def compressTree(self):
    node = self.root

    def dfs(node):
      if len(node.children) == 0:
        return node 
      for ch in node.children:
        n = dfs(ch)

      if len(node.children) == 1:
        node.merge(n)
      return node
    
    dfs(node)
  
  def findInTree(self, suffix):
    node = self.root
    word = suffix + '\0'
    found = False

    while not node.isLeaf() and len(word) != 0:
      go = False
      for ch in node.children:
        if ch.key == word:
          found = True
          go = True
          break
        elif ch.key == word[:len(ch.key)]:
          word = word[len(ch.key): ]
          node = ch
          go = True
          break
      if not go:
        return False, 0
      if found:
        break

    if word != '\0':
      exist, node = node.childExists(word)
    if found:
      counter = 0
      def dfs(vertex):
        nonlocal counter
        if vertex.isLeaf():
          counter += 1

        for ch in vertex.children:
          dfs(ch)
      dfs(node)
      return True, counter
    else:
      return False, 0



  def print_tree(self):
    print("=======SUFFIX TREE=======")
    self._print_tree(self.root, 0)
    print("=========================")

  def _print_tree(self, node, lvl):
      print('  ' * lvl + str(node))
      for child in node.children:
          self._print_tree(child, lvl + 1)

class SuffixTable:
  def __init__(self, word):
    self.suffixes = [(i, x) for i, x in enumerate(generateAllSuffixes(word))]
    self.suffixes.sort(key=lambda x : x[1])

  def search(self, suffix):
    l = 0
    r = len(self.suffixes) - 1
    while l < r:
      mid = (l+r) // 2
      if self.suffixes[mid][1] < suffix:
        l = mid +1
      else:
        r = mid
    if self.suffixes[l][1] == suffix:
      return True
    else: 
      return False


def main():
  word = 'banana\0'
  tree = SuffixTree(word)
  # tree.print_tree()

  for i, s in enumerate(generateAllSuffixes(word)):
    res = tree.findInTree(s[:-1])
    print(f'{i}) {s}: {res[1]}')

  table = SuffixTable(word)
  print(f'na\\0 : {table.search('na\0')}')
  print(f'ba\\0 : {table.search('ba\0')}')

  
if __name__ == '__main__':
  main()  