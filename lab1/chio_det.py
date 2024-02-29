from matrix import Matrix


def det2x2(m : Matrix):
  if m.size() == (2,2):
    return m[0][0] * m[1][1] - m[0][1] * m[1][0] 

def power(a, x):
  r = 1
  for i in range(x):
    r *= a
  return r

def det(m : Matrix):
  a = m[0][0]
  i = 0
  n, k = m.size()
  if n!= k:
    raise ValueError('Only square matrix has determinant!')
  if n <3:
    return det2x2(m)
  
  while a == 0 and i < n - 1:
    i += 1
    a = m[i][0]
  if a == 0:
    return 0
  if (i == 0):
    res = Matrix((n - 1, n - 1))
    for i in range(n - 1):
      for j in range(n - 1):
        res[i][j] = det2x2(Matrix([[m[0][0], m[0][j + 1]],
                                   [m[i + 1][0], m[i + 1][j + 1]]]))
    return det(res) / power(a, n-2)
  else:
    new = m._matrix
    r1 = m[0]
    r2 = m[i]
    new[i] = r1
    new[0] = r2
    new = Matrix(new)
    res = Matrix((n - 1, n - 1))
    for i in range(n - 1):
      for j in range(n - 1):
        res[i][j] = det2x2(Matrix([[new[0,0], new[0,j + 1]],
                                   [new[i + 1,0], new[i + 1,j + 1]]]))
    return - det(res) / power(a, n-2)
  

def main():
  m1 = Matrix([[5,1,1,2,3],
              [4,2,1,7,3],
              [2,1,2,4,7],
              [9,1,0,7,0],
              [1,4,7,2,2]])
  
  m2 = Matrix([[0,1,1,2,3],
            [4,2,1,7,3],
            [2,1,2,4,7],
            [9,1,0,7,0],
            [1,4,7,2,2]])
  print(det(m1))
  print(det(m2))

if __name__ == '__main__':
  main()