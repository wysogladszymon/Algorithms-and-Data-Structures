
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
  
  def __str__(self):
    return self.data.__str__()

class LinkedList:
  def __init__(self) -> None:
    self.head = None
  
  def destroy(self):
    "it destroys a list"
    self.head = None
  
  def add(self, node : Node):
    'adds to a beginning of a list'
    if self.head:
      second = self.head
      self.head = node
      self.head.next = second
    else:
      self.head = node
      
  def append(self, node : Node):
    "it adds element to the end of a list"
    if not self.head:
      self.head = node
    else:
      curr = self.head
      while curr:
        if not curr.next:
          break
        curr = curr.next
      curr.next = node
  
  def remove(self):
    'removes first element, and returns it'
    first = self.head
    if not first:
      return
    if not first.next:
      self.head = None
      return
    self.head = first.next
    return first
    
  
  def remove_end(self):
    "removes last element and returns it"
    if not self.head:
      return 
    else:
      prev = None
      curr = self.head
      while curr.next:
        if not curr.next:
          break
        prev = curr
        curr = curr.next
      if not prev:
        self.head = None
      else:
        prev.next = None
      return curr        
      
    
  def is_empty(self) -> bool:
    "returns True if the list is empty"
    return self.head is None    
  
  def length(self):
    "returns number of elements"
    if not self.head:
      return 0
    curr = self.head
    counter = 0
    while curr:
      counter += 1
      curr = curr.next
    return counter
    
  def get(self):
    "returns first element's data"
    if self.head:
      return self.head.data
    
  def __str__(self):
    res = ''
    if not self.head:
      return res
    curr = self.head
    while curr:
      res += f"-> {curr} \n"
      curr = curr.next
    return res
    