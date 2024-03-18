nodeSize = 6

class Node:
  def __init__(self):
    self.next = None
    self.tab = [None for _ in range(nodeSize)]
    self.size = 0
    
  def insert(self, index, value):
    if index > self.size:
      index = self.size 
      
    if self.size < nodeSize:
      self.tab.insert(index, value)
      self.tab.pop()
      self.size += 1
      return
    newNode = Node()
    newNode.next = self.next
    self.next = newNode
    for i in range(nodeSize//2, nodeSize):
      newNode.tab[i - nodeSize//2] = self.tab[i]
      newNode.size += 1
      self.tab[i] = None
      self.size -= 1
      
    if index > nodeSize//2:
      newNode.insert(index - nodeSize // 2, value)
    else:
      self.insert(index, value)
  def delete(self, index):
    if index >= self.size:
      index = self.size - 1
    
    self.tab.pop(index)
    self.tab.append(None)
    self.size -= 1
    if self.size < (nodeSize + 1)//2 and self.next:
      nextNode = self.next
      self.insert(self.size, nextNode.tab[0])
      nextNode.tab.pop(0)
      nextNode.size -= 1
      nextNode.tab.append(None)
      if nextNode.size < (nodeSize + 1)//2:
        for el in nextNode.tab:
          if el is not None:
            self.insert(self.size, el)
        self.next = nextNode.next
    return
        
  
class ULL:
  def __init__(self):
    self.head = None
    self.size = 0

  def get(self, index):
    if self.head is None:
      return None
    currentNode = self.head
    i = 0
    
    while currentNode:
      if i + currentNode.size > index:
        return currentNode.tab[index - i]
      i += currentNode.size
      if currentNode.next is None:
        return currentNode.tab[currentNode.size - 1]
      currentNode = currentNode.next
    
  
  def insert(self, index, value):
    if self.head is None:
      self.head = Node()
      self.head.tab[0] = value
      self.head.size = 1
      return
    currentNode = self.head
    i = 0
    while currentNode:
      if i + currentNode.size > index:
        currentNode.insert(index - i, value)
        return
      if not currentNode.next:
        currentNode.insert(currentNode.size, value)
        return
      i += currentNode.size
      currentNode = currentNode.next
      
  def delete(self, index):
    if self.head is None:
      return 
    currentNode = self.head
    i = 0
    while currentNode:
      if i + currentNode.size > index:
        currentNode.delete(index - i)
        return
      i += currentNode.size
      currentNode = currentNode.next

  def __str__(self):
    result = "["
    current_node : Node | None = self.head
    while current_node:
        for i in range(current_node.size):
            result += str(current_node.tab[i])
            if i < current_node.size - 1 or current_node.next:
                result += ", "
        current_node = current_node.next
    result += "]"
    return result

def printNode(node):
  while node:
    print(node.tab)
    node = node.next
  print("")
  
def main():
  ull = ULL()
  for i in range(1,10):
    ull.insert(i, i)
  print(ull.get(4))
  ull.insert(1,10)
  ull.insert(8,11)
  print(ull)
  ull.delete(1)
  ull.delete(2)
  print(ull)
  printNode(ull.head)
  
if __name__ == "__main__":
  main()
  