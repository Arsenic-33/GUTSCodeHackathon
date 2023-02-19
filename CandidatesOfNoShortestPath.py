# You are given an undirected connected weighted graph with N vertices and M edges that contains
#  neither self-loops nor double edges. The th  edge connects vertex ai and vertex bi with a distance of ci. 
# Here, a self-loop is an edge where ai = bi , and double edges are two edges where (ai ,bi)=(aj ,bj) or (ai ,bi)=(bj ,aj)1≤i

# Input Format

# Given standard input string as follows:

# N M
# "a1   b1   c1"
# "a2   b2  ​ c2"
# ... ,
# "aM   bM   cM"

# Constraints

# 1≤ai,bi≤N
# 1≤ci≤1000
# ci is an integer.
# The given graph contains neither self-loops nor double edges.
# The given graph is connected.
# Output Format

# Print the number of the edges in the graph that are not contained in any shortest path between any pair of different vertices as an integer.

#50/50, this imports a prewritted dijkstra but the logic is the main part of the solution and this is a common algorithm so this is seen as okay
#Code might not be optimal I'll be honest, this was done in like 10-15 minutes includng learning dijkstra to the point of using it


# Enter your code here. Read input from STDIN. Print output to STDOUT
import heapq

n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    adj[a-1].append((b-1, c))
    adj[b-1].append((a-1, c))

def dijkstra(s):
    #inf weight on all, I learnt dijkstra today in a yt vid, I dont fully understand
    dist = [float('inf') for _ in range(n)]
    dist[s] = 0
    heap = [(0, s)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))
    return dist

# Find shortest paths between all pairs of vertices
shortest_paths = []
for i in range(n):
    shortest_paths.append(dijkstra(i))

# Count edges that are not in any shortest path
count = 0
for a in range(n):
    for b in range(a+1, n):
        for v, w in adj[a]:
            if v == b:
                if w == shortest_paths[a][b]:
                    break
                else:
                    count += 1
                    break
print(count)