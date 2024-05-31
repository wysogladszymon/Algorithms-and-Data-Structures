import numpy as np 
from bitarray import bitarray
import time


primeNumbers = [167,3943,2591,7681,239,109,53,113,241,191,193,97,127,263,229,79,83,251,181,139]
powersOf2 = [128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]

def readTextFromFile(filePath):
  with open(filePath, encoding='utf-8') as f:
    text = f.readlines()
  return ' '.join(text).lower()

def countTime(f):
  tStart = time.perf_counter()
  res = f()
  tStop = time.perf_counter()
  print("Czas obliczeń:", "{:.7f}".format(tStop - tStart))
  return res

class BloomFilter:
  def __init__(self, P=0.001, n=20):
    self.n = n
    self.P = P
    self.b = int(-n * np.log(P) / (np.log(2) ** 2))
    self.k = int(self.b / n * np.log(2))
    # bitarray dla oszczednosci pamieciowych
    self.table = bitarray(self.b)
    self.hashes = None
  
  def setHashes(self, hashes):
    self.hashes = hashes
  
  def hash(self, word, d=256, q=101):
    hW = 0
    for char in word:
      hW = (hW * d + ord(char)) % q
    return hW
  
  def add(self, word):
    for q, d in self.hashes:
      hW = self.hash(word, d, q)
      self.table[hW % self.b] = 1
    
  def addAll(self, patterns):
    self.table.setall(False)
    for word in patterns:
      self.add(word)
      
  def checkWord(self, word, patterns):
    for p in patterns:
      if p == word:
        return True
    return False
  
  def checkHashes(self, hW):
    for h in hW:
      if not self.table[h % self.b]:
        return False
    return True
    
  def searchSpecificLength(self, text, N, patterns):
    self.addAll(patterns)
    X = len(text)
    h = [d ** (N-1) % q for q, d in self.hashes]
    
    hW = []
    prev = []
    indices = {x : [] for x in patterns}
    for i in range(X-N+1):
      word = text[i:N+i] # i:N+i-1
      for j, m in enumerate(self.hashes):
        q = m[0]
        d = m[1]
        if i == 0:
          hW.append(self.hash(word, d, q))
        else:
          hW[j] = (q + d * (prev[j] - ord(text[i-1]) * h[j]) + ord(text[i-1 + N])) % q
      prev = hW.copy()
           
      if self.checkHashes(hW):
        if self.checkWord(word, patterns):
          indices[word].append(i)        
    return indices
          
  
def testSpecificLength(text, patterns, N):
  P = 0.001
  n = len(patterns)
  Bf = BloomFilter(P, n)
  # określenie funkcji hashujących
  hashes = [(primeNumbers[i], powersOf2[i // 2]) for i in range(Bf.k)]
  Bf.setHashes(hashes)
  return Bf.searchSpecificLength(text, N, patterns)

def main():
  text = readTextFromFile('lotr.txt')
  patterns1 = ['gandalf', 'looking', 'blocked', 'comment', 'pouring', 'finally', 'hundred', 'hobbits', 'however', 'popular', 'nothing', 'enjoyed', 'stuffed', 'relaxed', 'himself', 'present', 'deliver', 'welcome', 'baggins', 'further']
  N = len(patterns1[0])
  f1 = lambda : testSpecificLength(text,patterns1, N)
  patterns = ['gandalf']
  f2 = lambda : testSpecificLength(text, patterns,N)
  
  print('Jeden wzorzec:')
  indices = countTime(f2)
  # for k, v in indices.items():
  #   print(f'{k}: {v}')
  print('20 wzorców:')
  indices =countTime(f1)  
  # for k, v in indices.items():
  #   print(f'{k}: {v}')
  
if __name__ == '__main__':
  main()
