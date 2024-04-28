from typing import List

class Vertex:
  def __init__(self, id):
    self.id = id
    
  def __eq__(self, other : "Vertex"):
    return isinstance(other, Vertex) and self.id == other.id
  
  def __hash__(self):
    return hash(self.id)
  
  def __str__(self):
    return f'{self.id}'
  
  
  
class Graph:
  def __init__(self, empty = 0):
    self.matrix = [[]]
    self.vertices_ = []
    self.empty = empty
    
  def is_empty(self):
    return len(self.vertices_) == 0
  
  def insert_vertex(self, vertex : "Vertex"):
    if vertex in self.vertices_:
      return
    self.vertices_.append(vertex)
    for row in self.matrix:
      row.append(self.empty)
    self.matrix.append([self.empty] * len(self.vertices_))
  
  def insert_edge(self, vertex1, vertex2, edge = 1):
    self.insert_vertex(vertex1)
    self.insert_vertex(vertex2)
    i1 = self.vertices_.index(vertex1)
    i2 = self.vertices_.index(vertex2)
    
    self.matrix[i1][i2] = edge
    self.matrix[i2][i1] = edge
    
  def delete_vertex(self,vertex):
    index = self.vertices_.index(vertex)
    for row in self.matrix:
      row.pop(index)
    self.matrix.pop(index)
    self.vertices_.pop(index)
    
  def delete_edge(self,vertex1, vertex2):
    i1 = self.__getVertexID(vertex1)
    i2 = self.__getVertexID(vertex2)
    
    self.matrix[i1][i2] = self.empty
    self.matrix[i2][i1] = self.empty

  
  def neighbours(self, vertex):
    index = self.vertices_.index(vertex)
    return [(self.vertices_[i], val) for i, val in enumerate(self.matrix[index]) if val != self.empty]

  def vertices(self):
    return self.vertices_

  def get_vertex(self, vertexID):
    for node in self.vertices_:
      if node.id == str(vertexID):
        return node
  
  def __getVertexID(self, vertex):
    return self.vertices_.index(vertex)
  