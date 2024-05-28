from graph import Graph, Vertex
import numpy as np
from copy import deepcopy

#-------------------------------------------
def ullmann1(G : "Graph", P :"Graph"):
  Y = len(P.vertices())
  X = len(G.vertices())
  M = np.zeros((Y, X))
  matrices = []
  usedCols = [False] * X
  calls = 0
  def generateRecursive(matrix, row):
    nonlocal matrices, Y, X, G, P, calls
    calls += 1
    if (row == Y):
      if np.all(P.matrix == matrix @ np.transpose(matrix @ G.matrix)):
        matrices.append(matrix.copy())
      return
    
    for col in range(X):
      if not usedCols[col]:
        usedCols[col] = True
        matrix[row, col] = 1
        generateRecursive(matrix, row + 1)
        matrix[row, col] = 0
        usedCols[col] = False
  generateRecursive(M, 0)
  return matrices, calls

#-------------------------------------------
def ullmann2(G : "Graph", P :"Graph"):
  Y = len(P.vertices())
  X = len(G.vertices())
  M = np.zeros((Y, X))
  matrices = []
  usedCols = [False] * X
  calls = 0
  # counting M0
  M0 = np.zeros((Y,X), dtype=bool)
  for i in range(Y):
    degVi = len(P.neighbours(i))
    for j in range(X):
      degVj = len(G.neighbours(j))
      if degVi <= degVj:
        M0[i, j] = True
          
  def generateRecursive(matrix, row):
    nonlocal matrices, Y, X, G, P, calls, M0
    calls += 1
    # stop condition
    if (row == Y):
      if np.all(P.matrix == matrix @ np.transpose(matrix @ G.matrix)):
        matrices.append(matrix.copy())
      return
    
    for col in range(X):
      if not usedCols[col] and M0[row, col]:
        usedCols[col] = True
        matrix[row, col] = 1
        generateRecursive(matrix, row + 1)
        matrix[row, col] = 0
        usedCols[col] = False
  generateRecursive(M, 0)
  return matrices, calls            

#-------------------------------------------
def exist(matrix, neighboursP, neighboursG):
  for x in neighboursP:
    exist = False
    for y in neighboursG:
      if matrix[x][y]:
        exist = True
    if not exist:
      return False
  return True

def prune(matrix, G : 'Graph', P : 'Graph', row):
  Y, X = matrix.shape
  change = True
  while change:
    change = False
    for i in range(row, Y):
      for j in range(X):
        if matrix[i][j] == 0:
          continue
        
        neighboursP = [P.getVertexID(x) for x, _ in P.neighbours(i)]
        neighboursG = [G.getVertexID(y) for y, _ in G.neighbours(j)]
        e = exist(matrix, neighboursP, neighboursG)
        if not e:
          matrix[i][j] = 0
          change = True
          break
        
  return matrix
             
    
def ullmann3(G : "Graph", P :"Graph"):
  Y = len(P.vertices())
  X = len(G.vertices())
  M = np.zeros((Y, X))
  matrices = []
  usedCols = [False] * X
  calls = 0
  # counting M0
  M0 = np.zeros((Y,X), dtype=int)
  for i in range(Y):
    degVi = len(P.neighbours(i))
    for j in range(X):
      degVj = len(G.neighbours(j))
      if degVi <= degVj:
        M0[i, j] = 1
  
  def backtrack(matrix, row):
    nonlocal matrices, Y, X, G, P, calls
    calls += 1
    # stop condition
    if (row == Y):
      if np.all(P.matrix == matrix @ np.transpose(matrix @ G.matrix)):
        matrices.append(matrix)
      return
    prune(matrix, G, P, row)
    for col in range(X):
      if not usedCols[col] and matrix[row, col]:
        newM = deepcopy(matrix)
        usedCols[col] = True
        newM[row, :] = 0
        newM[row, col] = 1
        backtrack(newM, row + 1)
        usedCols[col] = False
  backtrack(M0, 0)
  return matrices, calls



def main():
  graph_G = [ ('A','B',1), ('B','F',1), ('B','C',1), ('C','D',1), ('C','E',1), ('D','E',1)]
  graph_P = [ ('A','B',1), ('B','C',1), ('A','C',1)]  
  G = Graph()
  P = Graph()
  
  for e in graph_G:
    v1 = G.get_vertex(e[0])
    if not v1:
      v1 = Vertex(e[0])
      G.insert_vertex(v1)
    v2 = G.get_vertex(e[1])
    if not v2:
      v2 = Vertex(e[1])
      G.insert_vertex(v2)
    G.insert_edge(v1, v2, e[2])
  
  for e in graph_P:
    v1 = P.get_vertex(e[0])
    if not v1:
      v1 = Vertex(e[0])
      P.insert_vertex(v1)
    v2 = P.get_vertex(e[1])
    if not v2:
      v2 = Vertex(e[1])
      P.insert_vertex(v2)
    P.insert_edge(v1, v2, e[2])

  m, i = ullmann1(G, P)
  print(f'{len(m)}, {i}')
  m, i = ullmann2(G, P)
  print(f'{len(m)}, {i}')
  m, i = ullmann3(G, P)
  print(f'{len(m)}, {i}')
    
      
    
  
if __name__ == '__main__':
  main()