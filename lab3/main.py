from FIFO import FIFO

def main():
  q = FIFO()
  for i in range(1,5):
    q.enqueue(i)
  print(q.dequeue())
  print(q.peek())
  print(q)
  for i in range(5,9):
    q.enqueue(i)
  print(q.tab)
  while not q.is_empty():
    ret = q.dequeue()
    print(ret)
  print(q)
  
  
if __name__ == "__main__":
  main() 
  
  