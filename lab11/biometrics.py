import numpy as np
from collections import deque
import matplotlib.pyplot as plt

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
  

class BiometricGraph:
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
      if node.id == vertexID:
        return node
    return None
  
  def getVertexID(self, vertex):
    return self.vertices_.index(vertex)
  
  def getVertexByRow(self, row):
    return self.vertices_[row]
  
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
  
  def plot_graph(self, v_color, e_color):  
    for v in self.vertices():
      y, x = v.id
      plt.scatter(x, y, c=v_color)
      for neighbour, _ in self.neighbours(v):
        yn, xn = neighbour.id
        plt.plot([x, xn], [y, yn], color=e_color)
    plt.show()
  
def fill_biometric_graph_from_image(img, graph : BiometricGraph):
  Y, X = img.shape
  for y in range(Y):
    for x in range(X):
      if img[y, x] == 255:
        v = Vertex((Y-y, x))
        graph.insert_vertex(v)
        if y > 0:
          for i in range(x-1, x+2):
            if i > 0 and i < X and img[y-1, i] == 255:
              graph.insert_edge(graph.get_vertex((Y-(y -1), i)), v)
        if x > 0 and img[y, x-1] == 255:
          graph.insert_edge(graph.get_vertex((Y-y, x-1)), v)


def unclutter_biometric_graph(graph : "BiometricGraph"):
  vertices = graph.vertices()
  trash = set()
  insertion = set()
  for v in vertices:
    neighbours = graph.neighbours(v)
    if len(neighbours) == 2:
      continue
  
    for n, _ in neighbours:
      prev = v
      node = n
      while len(graph.neighbours(node)) == 2:
        nodes = graph.neighbours(node)
        trash.add(node)
        if nodes[0][0] == prev:
          node, prev = nodes[1][0], node
        else:
          node, prev = nodes[0][0], node
      insertion.add((v, node))

  for node in trash:
    graph.delete_vertex(node)

  for v1, v2 in insertion:
    graph.insert_edge(v1,v2)

    
def merge_near_vertices(graph : "BiometricGraph", thr=10):
  vertices = graph.vertices()
  Y = len(vertices)
  merge = []
  visited = {x : False for x in vertices}
  for i in range(Y-1):
    v1 = vertices[i]
    if visited[v1]:
      continue
    visited[v1] = True
    merge.append([v1])
    for j in range(i+1, Y):
      v2 = vertices[j]
      if visited[v2]:
        continue
      dist = np.sqrt((v1.id[0]- v2.id[0])** 2 + (v1.id[1] - v2.id[1])**2)
      if dist < thr:
        merge[-1].append(v2)
        visited[v2] = True
        
  for i, m in enumerate(merge):
    if len(m) == 1:
      continue
    meanX = np.mean(list(map(lambda x : x.id[1], m)))
    meanY = np.mean(list(map(lambda x : x.id[0], m)))
    neighbors = []
    for v in m:
      neighbors.extend([x for x, _ in graph.neighbours(v) if x not in m])
    for v in m:
      graph.delete_vertex(v)  
    newV = Vertex((meanY, meanX))
    graph.insert_vertex(newV)
    for v2 in neighbors:
      graph.insert_edge(newV, v2)
    

def rotateGraph(graph : "BiometricGraph", tx, ty, theta):
  for v in graph.vertices():
    y, x = v.id
    newX = (x+tx)*np.cos(theta) + (y + ty)*np.sin(theta)
    newY = -(x+tx)*np.sin(theta) + (y + ty)*np.cos(theta)
    v.id = (newY, newX)

def dist(v1 :Vertex, v2 : Vertex):
  return np.sqrt((v1.id[0] - v2.id[0]) ** 2 + (v1.id[1] - v2.id[1]) ** 2)

def angle(v1 : Vertex, v2 : Vertex):
  return np.arctan((v1.id[0] - v2.id[0]) / (v1.id[1] - v2.id[1]))

def biometric_graph_registration(graph1, graph2, Ni=50, eps=10):
  edges = set()
  for v1, v2 in graph1:
    l1 = dist(v1, v2)
    theta1 = angle(v1, v2)
    for n1, n2 in graph2:
      l2 = dist(n1, n2)
      theta2 = angle(n1, n2)
      sab = 2 * np.sqrt((l1 - l2) ** 2 + (theta1 - theta2) ** 2) / (l1 + l2)
      edges.add((sab, (v1,v2), (n1, n2)))