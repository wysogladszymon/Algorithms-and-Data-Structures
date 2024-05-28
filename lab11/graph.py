from typing import List
import numpy as np

class Vertex:
  def __init__(self, id):
    self.id = id
    
  def __eq__(self, other : "Vertex"):
    return isinstance(other, Vertex) and self.id == other.id
  
  def __hash__(self):
    return hash(self.id)
  
  def __str__(self):
    return f'{self.id}'
  
  def __lt__(self, other):
      return self.id < other.id

  def __gt__(self, other):
      return self.id > other.id
  
  
  
class Graph:
  def __init__(self, empty = 0):
    self.matrix = None
    self.vertices_ = []
    self.empty = empty
    
  def dependency(self):
    return self.matrix
  
  def is_empty(self):
    return len(self.vertices_) == 0
  
  def insert_vertex(self, vertex : "Vertex"):
    if isinstance(self.matrix, type(None)):
      self.matrix = np.zeros((1,1))
      self.vertices_.append(vertex)
      return 
    if vertex in self.vertices_:
      return
    self.vertices_.append(vertex)
    
    # update of dependency matrix
    Y, X = self.matrix.shape
    # new col in dependency
    self.matrix = np.concatenate((self.matrix, np.zeros((Y, 1))), axis=1)
    # new row in dependency
    self.matrix = np.concatenate((self.matrix, np.zeros((1, X+1))))
  
  def insert_edge(self, vertex1, vertex2, edge = 1):
    self.insert_vertex(vertex1)
    self.insert_vertex(vertex2)
    i1 = self.vertices_.index(vertex1)
    i2 = self.vertices_.index(vertex2)
    self.matrix[i1][i2] = edge
    self.matrix[i2][i1] = edge
    
  def delete_vertex(self,vertex):
    index = self.vertices_.index(vertex)

    # deleting row in dependency
    self.matrix = np.delete(self.matrix, index, axis=0)
    # deleting col in dependency
    self.matrix = np.delete(self.matrix, index, axis=1)
    
    self.vertices_.pop(index)
    
  def delete_edge(self,vertex1, vertex2):
    i1 = self.getVertexID(vertex1)
    i2 = self.getVertexID(vertex2)
    
    self.matrix[i1][i2] = self.empty
    self.matrix[i2][i1] = self.empty

  def neighbours(self, vertex):
    if isinstance(vertex, Vertex):
      vertex = self.vertices_.index(vertex)
    return [(self.vertices_[i], val) for i, val in enumerate(self.matrix[vertex]) if val != self.empty]

  def vertices(self):
    return self.vertices_

  def get_vertex(self, vertexID):
    for node in self.vertices_:
      if str(node.id) == str(vertexID):
        return node
    return None
  
  def getVertexID(self, vertex):
    return self.vertices_.index(vertex)
  
  def edges(self):
    edges = set()
    for i, row in enumerate(self.matrix):
      for j, val in enumerate(row):
        if val != self.empty:
          if self.vertices_[i] < self.vertices_[j]:
            edges.add((str(self.vertices_[i]), str(self.vertices_[j])))
          else:
            edges.add((str(self.vertices_[j]), str(self.vertices_[i])))
    return edges
    
  def __iter__(self):
    return iter(self.edges())
  
# test 

# def main():
#   print('e')
#   g = Graph()
#   verticesCount = 5
#   edges = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4)]
#   for i in range(verticesCount):
#     g.insert_vertex(Vertex(i))
#   print(g.vertices_)
#   print(g.matrix)
  
#   for e in edges:
#     g.insert_edge(g.vertices_[e[0]], g.vertices_[e[1]])
  
#   g.delete_edge(g.vertices_[0], g.vertices_[1])
#   print(g.matrix)
#   print(g.neighbours(g.get_vertex(0)))

# if __name__ == "__main__":
#   main()