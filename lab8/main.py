import polska
# from Graph import Graph, Vertex
from Graph_dependency import Graph as Gd, Vertex
from Graph_matrix import Graph as Gm
from typing import Union

def test(graphClass : Union[Gd, Gm]):
  data = polska.graf
  g = graphClass()
  
  for tup in data:
    v1 = Vertex(tup[0])
    v2 = Vertex(tup[1])
    g.insert_edge(v1,v2)

  g.delete_vertex(g.get_vertex('K')) 
  g.delete_edge(g.get_vertex('W'), g.get_vertex('E'))
  polska.draw_map(g)

def main():
  test(Gd)
  # test(Gm)

if __name__ == "__main__":
  main()