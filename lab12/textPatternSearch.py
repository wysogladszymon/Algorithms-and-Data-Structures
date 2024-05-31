import time

def countTime(f):
  tStart = time.perf_counter()
  res = f()
  tStop = time.perf_counter()
  print("Czas obliczeń:", "{:.7f}".format(tStop - tStart))
  return res
  
def naive(text, pattern):
  counter = 0
  indices = []
  for i in range(len(text)):
    same = True
    for m in range(len(pattern)):
      counter += 1
      if text[i + m] != pattern[m]:
        same = False
        break
    if same == True:
      indices.append(i)
  return indices, counter
      
def hash(word, d=256, q=101):
  hW = 0
  N = len(word)
  for i in range(N):
    hW = (hW*d + ord(word[i])) % q
  return hW

def RabinKarp1(S, W):
  hW = hash(W)
  M = len(S)
  N = len(W)
  counter = 0
  indices = []
  for m in range(M-N+1):
    hS = hash(S[m:m+N])
    counter += 1
    if hS == hW:
      if S[m:m+N] == W:
        indices.append(m)
  return indices, counter

def RabinKarp2(S, W):
  # rolling hash veriosn
  hW = hash(W)
  M = len(S)
  N = len(W)
  d = 256
  q = 101
  h = 1
  for _ in range(N-1):
    h = (h*d) % q
  errCount = 0
  counter = 0
  indices = []
  prevHash = hash(S[:N], d, q)
  
  for m in range(M-N+1):
    if m == 0:
      hS = prevHash
    else:
      hS = (d * (prevHash - ord(S[m-1]) * h) + ord(S[m-1 + N]) ) % q
    counter += 1
    prevHash = hS
    if hS == hW:
      if S[m:m+N] == W:
        indices.append(m)
      else:
        errCount += 1
  return indices, counter, errCount

def main():
  with open("lotr.txt", encoding='utf-8') as f:
    text = f.readlines()

  S = ' '.join(text).lower()
  
  pattern = 'time.'
  f = lambda : naive(S, pattern)
  # indices, counter = countTime(f)
  
  indices, counter = f()
  print(f'{len(indices)};{counter}')
  
  # g = lambda : RabinKarp1(S, pattern)
  # indices, counter = countTime(g)
  # print(f'{len(indices)};{counter}')
  
  h = lambda : RabinKarp2(S, pattern)
  # indices, counter, errCount = countTime(h)
  indices, counter, errCount = h()
  print(f'{len(indices)};{counter};{errCount}')
  
  
    
if __name__ == '__main__':
  main()