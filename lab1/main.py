from matrix import Matrix
from chio_det import det

def main():
  m1 = Matrix(
  [ [1, 0, 2],
    [-1, 3, 1] ]
  )
  m2 = Matrix((2,3),1)
  m3 = Matrix([[3,1],[2,1],[1,0]])
  print(m1 + m2,'\n')
  print(m1 * m3)

  m4 = Matrix([[5,1,1,2,3],
              [4,2,1,7,3],
              [2,1,2,4,7],
              [9,1,0,7,0],
              [1,4,7,2,2]])
  
  m5 = Matrix([[0,1,1,2,3],
            [4,2,1,7,3],
            [2,1,2,4,7],
            [9,1,0,7,0],
            [1,4,7,2,2]])
  print(det(m4))
  print(det(m5))

if __name__ == '__main__':
  main()

