import cv2
from graph import Graph
from djikstraPrim import prim
from collections import deque
import numpy as np

def getID(XX, j, i):
  return XX * j + i

def getCoords(XX, ID):
  return ID // XX, ID % XX

def graphTraversal(g : "Graph", start, color, img):
  q = deque()
  q.append(start)
  visited = set()
  visited.add(start)
  Y, X = img.shape
  while q:
    node = q.popleft()
    y, x = getCoords(X, node)
    img[y, x] = color
    for neighbor, edge in g.neighbours(node):
      if neighbor not in visited:
        q.append(neighbor)
        visited.add(neighbor)
  return img        
  
def main():
  I = cv2.imread('sample.png', cv2.IMREAD_GRAYSCALE).astype(int)
  Y, X = I.shape
  g = Graph()
  for y in range(Y):
    for x in range(X):
      xID = getID(X, y, x)
      if x > 0:
        weight = abs(I[y, x] - I[y, x-1])
        g.insert_edge(xID, xID - 1, weight)
      if x > 0 and y > 0:
        weight = abs(I[y, x] - I[y-1, x-1])
        g.insert_edge(xID, xID - X - 1, weight)
      if x < X - 1 and y > 0:
        weight = abs(I[y, x] - I[y-1, x+1])
        g.insert_edge(xID, xID - X + 1,weight)
      if x < X - 1:
        weight = abs(I[y, x] - I[y, x+1])
        g.insert_edge(xID, xID + 1,weight)
      if y > 0:
        weight = abs(I[y, x] - I[y-1, x])
        g.insert_edge(xID, xID - X, weight)
      if x > 0 and y < Y - 1:
        weight = abs(I[y, x] - I[y+1, x-1])
        g.insert_edge(xID, xID + X - 1, weight)  
      if x < X - 1 and y < Y - 1:
        weight = abs(I[y, x] - I[y+1, x+1])
        g.insert_edge(xID, xID + X + 1,weight)
      if y < Y - 1:
        weight = abs(I[y, x] - I[y+1, x])
        g.insert_edge(xID, xID + X, weight)
  g, s = prim(g, 0)
  
  maxEdge = (0,0,0)
  # szukaj maksimum
  for edge in g.edges():
    if edge[2] > maxEdge[2]:
      maxEdge = edge
  g.delete_edge(maxEdge[0], maxEdge[1])
  
  img = np.zeros((Y, X), dtype='uint8')
  newImg = graphTraversal(g, maxEdge[0], 100, img)
  newImg = graphTraversal(g, maxEdge[1], 200, newImg)
  cv2.imshow("Wynik",newImg)
  cv2.waitKey() 
  
if __name__ == '__main__':
  main()