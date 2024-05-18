from graph import Vertex, Graph
from graf_mst import graph


class UnionFind:
  def __init__(self, n):
    self.p = [x for x in range(n)]
    self.size = [1 for _ in range(n)]
    self.n = n
  
  def find(self, v ):
    if self.p[v] == v:
      return v
    
    self.p[v] = self.find(self.p[v])
    return self.p[v]
  
  def union_sets(self, u, v):
    uRoot = self.find(u)
    vRoot = self.find(v)
    if self.size[uRoot] > self.size[vRoot]:
      self.p[vRoot] = uRoot
    elif self.size[uRoot] < self.size[vRoot]:
      self.p[uRoot] = vRoot
    elif uRoot != vRoot:
      self.p[uRoot] = vRoot
      self.size[vRoot] += 1

  def same_components(self, s1, s2):
    return self.find(s1) == self.find(s2)
  
def convertToNumber(sign):
  return ord(sign) - 65


def test1():
  n = 6
  edges = [(1,2),(1,4), (1,5), (4,5)]
  check = [(1,2),(2,3),(4,5), (1,4)]
  vertices = []
  uf = UnionFind(n)
  for i in range(n):
    vertices.append(n)
    
  
  for v1, v2 in edges:
    uf.union_sets(v1, v2)
  for v1, v2 in check:
    print(uf.same_components(v1,v2))
    

def kruskal(edges):
  edges = sorted(edges, key= lambda edge : (edge[2], edge[0], edge[1]))
  g = Graph()
  
  for n1, n2, e in edges:
    g.insert_edge(n1,n2, e)
    
  uf = UnionFind(g.size())
  for v1, v2, _ in edges:
    if uf.same_components(v1, v2):
      g.delete_edge(v1,v2)
    else:
      uf.union_sets(v1, v2)
  return g
  
  
def main():
  g = kruskal(graph)
  g.printGraph()
  
if __name__ == '__main__':
  main()