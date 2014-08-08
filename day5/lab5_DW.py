"""Data Structures
Working with Graphs/Networks"""

"""
Teammate: Betul
"""

from math import sqrt
from copy import deepcopy 

def makeLink(G, node1, node2):
  if node1 not in G:
    G[node1] = {}
  (G[node1])[node2] = 1
  if node2 not in G:
    G[node2] = {}
  (G[node2])[node1] = 1
  return G 

# Ring Network
ring = {} # empty graph 

n = 5 # number of nodes 

# Add in edges
for i in range(n):
  ring = makeLink(ring, i, (i+1)%n)

# How many nodes?
print len(ring)

# How many edges?
print sum([len(ring[node]) for node in ring.keys()])/2 

# Grid Network
# TODO: create a square graph with 256 nodes and count the edges 
# TODO: define a function countEdges

def sqr_graph(T):
	t=int(sqrt(T))
	mysquare={}
	for n in range(1,T+1):
		if n > t:
			makeLink(mysquare, n, n-t)
		if n + t <= T:
			makeLink(mysquare, n, n+t)
		if n % t != 1:
			makeLink(mysquare, n, n-1)
		if n % t !=	0:
			makeLink(mysquare, n, n+1)
	return mysquare	

def countEdges(graph):
	return sum([len(graph[node]) for node in graph.keys()])/2 				
				
my256graph = sqr_graph(256)				
print my256graph[18]					

# How many edges?
print countEdges(my256graph)


# Social Network
class Actor(object):
  def __init__(self, name):
    self.name = name 

  def __repr__(self):
    return self.name 

ss = Actor("Susan Sarandon")
jr = Actor("Julia Roberts")
kb = Actor("Kevin Bacon")
ah = Actor("Anne Hathaway")
rd = Actor("Robert DiNero")
ms = Actor("Meryl Streep")
dh = Actor("Dustin Hoffman")

movies = {}

makeLink(movies, dh, rd) # Wag the Dog
makeLink(movies, rd, ms) # Marvin's Room
makeLink(movies, dh, ss) # Midnight Mile
makeLink(movies, dh, jr) # Hook
makeLink(movies, dh, kb) # Sleepers
makeLink(movies, ss, jr) # Stepmom
makeLink(movies, kb, jr) # Flatliners
makeLink(movies, kb, ms) # The River Wild
makeLink(movies, ah, ms) # Devil Wears Prada
makeLink(movies, ah, jr) # Valentine's Day

# # How many nodes in movies?
def countNodes(graph):
	return len(graph)

print countNodes(movies)

# # How many edges in movies?

print countEdges(movies)

#this function takes you from one node to the next if possible. if not it gets upset
def tour(graph, nodes): #the input nodes should be a list of the nodes you want to visit. 
  for i in range(len(nodes)):
    node = nodes[i] 
    if node in graph.keys():
      print node 
    else:
      print "Node not found!"
      break 
    if i+1 < len(nodes):
      next_node = nodes[i+1]
      if next_node in graph.keys():
        if next_node in graph[node].keys():
          pass 
        else:
          print "Can't get there from here!"
          break 

# TODO: find an Eulerian tour of the movie network and check it 
# movie_tour = [kb, ms, rd, dh, kb, jr, dh, ss, jr, ah, ms] 
# tour(movies, movie_tour)

#this function takes you from one node to the next if possible. if not it gets upset
def Eularian_tour(graph, nodes, visited = None): #the input nodes should be a list of the nodes you want to visit. 
  if visited == None:
    visited = []
  for i in range(len(nodes)):
    node = nodes[i] 
    if node in graph.keys():
      print node 
    else:
      print "Node not found!"
      break 
    if i+1 < len(nodes):
      next_node = nodes[i+1]
      if next_node in graph.keys():
        if next_node in graph[node].keys():
          graph[node].pop(next_node)
          graph[next_node].pop(node) 
          visited.append((node, next_node))
          visited.append((next_node , node))
          pass 
        elif (node, next_node) in visited:
        	print "Oops!  Already walked down that road."
        	break
        else:
          print "Can't get there from here!"
          break 

Eularian_movie_tour = [kb, ms, rd, dh, kb, jr, dh, ss, jr, ah, ms] 
#NOT_eularian_tour = [kb, ms, rd, dh, kb, jr, dh, ss, jr, ah, ms, kb] 
Eularian_tour(movies, Eularian_movie_tour)
#Eularian_tour(movies, NOT_eularian_tour)


# def findPath(graph, start, end, path=[]):
#         path = path + [start]
#         if start == end:
#             return path
#         if not graph.has_key(start):
#             return None
#         for node in graph[start]:
#             if node not in path:
#                 newpath = findPath(graph, node, end, path)
#                 if newpath: return newpath
#         return None
# 
# print findPath(movies, jr, ms)
# 
# 
# # TODO: implement findShortestPath()
# # print findShortestPath(movies, ms, ss)
# 
# # TODO: implement findAllPaths() to find all paths between two nodes
# # allPaths = findAllPaths(movies, jr, ms)
# # for path in allPaths:
# #   print path