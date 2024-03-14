
class Node2:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None
  
  def __str__(self):
    return self.data.__str__()

class TwoWayLinkedList:
  def __init__(self) -> None:
    self.head = None
    self.tail = None
  
  def destroy(self):
    "it destroys a list"
    curr = self.head
    while curr != self.tail:
      a = curr
      curr = curr.next
      a.next = None
    self.head = None
    self.tail.prev = None  
    self.tail = None
    
  def add(self, node : Node2):
    'adds to a beginning of a list'
    if self.head:
      second = self.head
      self.head = node
      self.head.next = second
    else:
      self.head = node
      
  def append(self, node : Node2):
    "it adds element to the end of a list"
    if not self.head:
      self.head = node
    else:
      curr = self.head
      while curr != self.tail:
        curr = curr.next
      curr.next = node
      node.prev = curr 
    self.tail = node
  
  def remove(self):
    'removes first element, and returns it'
    first = self.head
    if not first:
      return
    if self.head == self.tail:
      self.head = None
      self.tail = None
      return first
    self.head = first.next
    return first
    
  
  def remove_end(self):
    "removes last element and returns it"
    if not self.tail:
      return
    if self.tail == self.head:
      first = self.head
      self.tail = None
      self.head = None
      return first
    last = self.tail
    self.tail = last.prev
    self.tail.next = None
    return last
      
    
  def is_empty(self) -> bool:
    "returns True if the list is empty"
    return self.head is None    
  
  def length(self):
    "returns number of elements"
    if not self.head:
      return 0
    curr = self.head
    counter = 1
    while curr != self.tail:
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
    while curr != self.tail.next:
      res += f"-> {curr} \n"
      curr = curr.next
    return res
    