import numpy as np
import time

def testTime(f):
  t_start = time.perf_counter()
  ans = f()
  t_stop = time.perf_counter()
  print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
  return ans

# -----------------------------------------------------------------------------
# a)
def stringCompare(word1, word2, i, j):
  if i == 0:
    return j
  if j == 0:
    return i
  switch = stringCompare(word1, word2, i-1,j-1) + (word1[i] != word2[j])
  insertion = stringCompare(word1, word2, i, j-1) + 1
  delete = stringCompare(word1, word2, i-1, j) + 1

  return np.min([switch, insertion, delete])

# def DPStringCompare(word1, word2, returnPath = False):
#   Y = len(word1)
#   X = len(word2)
#   D = np.zeros((Y, X), dtype=int)
#   D[0] = np.arange(0, X, 1)
#   D.T[0] = np.arange(0, Y, 1)
#   parents = np.full((Y,X), 'X')
#   parents[0] = np.array(['I'] * X)
#   parents.T[0] = np.array(['D'] * Y)
#   parents[0][0] = 'X'

#   def dp(word1, word2, i, j):
#     nonlocal parents, D
#     if parents[i][j] != 'X':
#       return D[i][j]
#     if i == 0:
#       D[:j, i] = j
#       return j
#     if j == 0:
#       return i

#     switch = dp(word1, word2, i-1,j-1) + (word1[i] != word2[j])
#     insertion = dp(word1, word2, i, j-1) + 1
#     delete = dp(word1, word2, i-1, j) + 1

#     if word1[i] == word2[j] and switch <= insertion and switch <= delete:
#       D[i][j] = switch
#       parents[i][j] = 'M'
#     elif switch <= insertion and  switch <= delete:
#       D[i][j] = switch + 1
#       parents[i][j] = 'S'
#     elif insertion <= switch and  insertion <= delete:
#       D[i][j] = insertion
#       parents[i][j] = 'I'
#     else:
#       D[i][j] = delete
#       parents[i][j] = 'D'

#     return D[i][j]

#   ret1 = dp(word1, word2, Y-1, X-1)
#   ret2 = reconstructPath(parents, Y, X) if returnPath else None
#   return ret1, ret2 

# -----------------------------------------------------------------------------
# b)
def DPStringCompare(word1, word2, returnPath = False):
  Y = len(word1)
  X = len(word2)
  D = np.zeros((Y, X), dtype=int)
  D[0] = np.arange(0, X, 1)
  D.T[0] = np.arange(0, Y, 1)
  parents = np.full((Y,X), 'X')
  parents[0] = np.array(['I'] * X)
  parents.T[0] = np.array(['D'] * Y)
  parents[0][0] = 'X'

  for i in range(1, Y):
    for j in range(1, X):
      switch = D[i-1][j-1] + (word1[i] != word2[j])
      delete = D[i-1][j] + 1 # usuwamy z word1
      insertion = D[i][j-1] + 1 # dodajemy do word2

      if word1[i] == word2[j] and switch <= insertion and switch <= delete:
        D[i][j] = switch
        parents[i][j] = 'M'
      elif switch <= insertion and  switch <= delete:
        D[i][j] = switch + 1
        parents[i][j] = 'S'
      elif insertion <= switch and  insertion <= delete:
        D[i][j] = insertion
        parents[i][j] = 'I'
      else:
        D[i][j] = delete
        parents[i][j] = 'D'
  
  ret1 = D[-1][-1]
  ret2 = reconstructPath(parents, Y, X) if returnPath else None
  return ret1, ret2
  
# -----------------------------------------------------------------------------
# c)
def reconstructPath(parents, Y, X):
  path = ''
  y, x = Y-1, X-1
  while parents[y][x] != 'X':
    path += parents[y][x]
    if parents[y][x] == 'M' or parents[y][x] == 'S':
      y-=1
      x-=1
    elif parents[y][x] == 'I':
      x-=1
    else:
      y -=1
  return path[::-1]

# -----------------------------------------------------------------------------
# d)
def substringSearch(word1, word2, returnPath = False):
  Y = len(word1)
  X = len(word2)
  D = np.zeros((Y, X), dtype=int)
  # D[0] = np.arange(0, X, 1)
  D.T[0] = np.arange(0, Y, 1)
  parents = np.full((Y,X), 'X')
  # parents[0] = np.array(['I'] * X)
  parents.T[0] = np.array(['D'] * Y)
  parents[0][0] = 'X'

  for i in range(1, Y):
    for j in range(1, X):
      switch = D[i-1][j-1] + (word1[i] != word2[j])
      delete = D[i-1][j] + 1 # usuwamy z word1
      insertion = D[i][j-1] + 1 # dodajemy do word2

      if word1[i] == word2[j] and switch <= insertion and switch <= delete:
        D[i][j] = switch
        parents[i][j] = 'M'
      elif switch <= insertion and  switch <= delete:
        D[i][j] = switch + 1
        parents[i][j] = 'S'
      elif insertion <= switch and  insertion <= delete:
        D[i][j] = insertion
        parents[i][j] = 'I'
      else:
        D[i][j] = delete
        parents[i][j] = 'D'
  return goal_cell(word1, word2, D)

def goal_cell(word1, word2, D):
  i = len(word1) - 1
  j = 0
  for k in range(1,len(word2)):
    if D[i][k] < D[i][j]:
      j = k
  return j
# -----------------------------------------------------------------------------
# e) + f)
def longestCommonSequence(word1, word2):
  Y = len(word1)
  X = len(word2)
  D = np.zeros((Y, X), dtype=int)
  parents = np.full((Y,X), 'X')
  
  parents[0] = np.array(['I'] * X)
  parents.T[0] = np.array(['D'] * Y)
  parents[0][0] = 'X'
  
  for i in range(1, Y):
    for j in range(1, X):
      if word1[i] == word2[j]:
        D[i][j] = D[i-1][j-1] + 1
        parents[i][j] = 'M'
      else:
        if D[i-1][j] >= D[i][j-1]:
          D[i][j] = D[i-1][j]
          parents[i][j] = 'D'
        else:
          D[i][j] = D[i][j-1]
          parents[i][j] = 'I'
  
  ret1 = D[-1][-1]

  ret2 = ''
  i = Y-1
  j = X-1
  while i > 0 and j > 0:
    if parents[i, j] == 'M':
      ret2 += word1[i]
      i -= 1
      j -= 1
    elif parents[i, j] == 'D':
      i -= 1
    else:
      j -= 1
  return ret1, ret2[::-1]


def main():
  # a) recursive 
  P = ' kot'
  T = ' pies'
  print(stringCompare(P, T, len(P)-1, len(T)-1))
  # b) dp
  P = ' biały autobus'
  T = ' czarny autokar'
  res = DPStringCompare(P,T)
  print(res[0])
  # c) path reconstruction
  P = ' thou shalt not'
  T = ' you should not'
  res = DPStringCompare(P,T,returnPath=True)
  print(res[1])
  # d) substring match
  P = ' ban'
  T = ' mokeyssbanana'
  res = substringSearch(P,T)
  print(res - len(P) + 1)
  # e) longest common sequence
  P = ' democrat'
  T = ' republican'
  # not finished
  res = longestCommonSequence(P, T)
  print(res[1])
  # f) longest common sorted subsequence 
  T = ' 243517698'
  arr = list(T)
  arr = sorted(arr)
  P=''
  for i in arr:
    P += i
  res = longestCommonSequence(P, T)
  print(res[1])

if __name__ == '__main__':
  main()