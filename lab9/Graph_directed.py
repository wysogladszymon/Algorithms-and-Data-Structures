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
  def __init__(self):
    self.dependency = {}
    
  def is_empty(self):
    return len(self.dependency) == 0
  
  def insert_vertex(self, vertex : "Vertex"):
    if vertex in self.dependency:
      return 
    self.dependency[vertex] = {}
  
  def insert_edge(self, vertex1, vertex2, edge = None):
    self.insert_vertex(vertex1)
    self.insert_vertex(vertex2)
    self.dependency[vertex1][vertex2] = edge
    # self.dependency[vertex2][vertex1] = edge
  
  def delete_vertex(self,vertex):
    for node in self.dependency:
      self.delete_edge(node, vertex)
    self.dependency.pop(vertex, None)
  
  
  def delete_edge(self,vertex1, vertex2):
    self.dependency[vertex1].pop(vertex2, None)
    
  def neighbours(self, vertexID):
    return list(self.dependency[vertexID].items())
  
  def vertices(self):
    return list(self.dependency.keys())
  
  def get_vertex(self, vertexID):
    for node in self.dependency:
      if node.id == str(vertexID):
        return node
      
  def edges(self):
    edges = set()
    for node in self.dependency:
      for neighbour, edge in self.dependency[node].items():
        edges.add((node, neighbour, edge))
    return edges
    
  def getEdge(self, v1, v2):
    return self.dependency[v1][v2]
  
  def __iter__(self):
    return iter(self.edges())


class Edge:
  def __init__(self, volume, isResidual = False):
    self.volume = volume
    self.isResidual = isResidual
    self.flow = 0
    self.residualFlow = 0 if isResidual else volume
  
  def __str__(self):
      return f'{self.volume} {self.flow} {self.residualFlow} {self.isResidual}'
      
  def __repr__(self):
    return self.__str__()  