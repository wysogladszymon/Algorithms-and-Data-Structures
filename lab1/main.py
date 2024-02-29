from matrix import Matrix

def main():
  m1 = Matrix(
  [ [1, 0, 2],
    [-1, 3, 1] ]
  )
  m2 = Matrix((2,3),1)
  m3 = Matrix([[3,1],[2,1],[1,0]])
  print(m1 + m2,'\n')
  print(m1 * m3)

if __name__ == '__main__':
  main()
