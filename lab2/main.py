from twoWayLinkedList import TwoWayLinkedList, Node2

def main():
  l = TwoWayLinkedList()
  universities = [('AGH', 'Kraków', 1919),
    ('UJ', 'Kraków', 1364),
    ('PW', 'Warszawa', 1915),
    ('UW', 'Warszawa', 1915),
    ('UP', 'Poznań', 1919),
    ('PG', 'Gdańsk', 1945)]
  for university in universities[:3]:
    e = Node2(university)
    l.append(e)
  
  for university in universities[3:]:
    e = Node2(university)
    l.add(e)
  
  print(l)
  print(l.length())
  l.remove()
  print(l.get())
  l.remove_end()
  print(l)
  l.destroy()
  print(l.is_empty())
  #dotąd dziala
  l.remove()
  l.append(Node2(universities[0]))
  l.remove_end()
  print(l.is_empty())
  
    
if __name__ == '__main__':
  main()

