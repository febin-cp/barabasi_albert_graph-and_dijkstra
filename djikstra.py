from collections import defaultdict
from heapq import *
def djikstra(start,end,edges):
	g = defaultdict(list)

	for l,r,c in edges:
		g[l].append((c,r))
	q,seen = [(0,start,())],set()
	while q:
		(cost,v1,path) = heappop(q)
		if v1 not in seen:
			seen.add(v1)
			path = (v1,path)
			if(v1==end):
				return(cost,path)
			for c, v2 in g.get(v1,path):
				if(v2 not in seen):
					heappush(q,cost+c,v2,path)
	return float("inf")
if __name__=="__main__":
	edges = [("A","B",1),("B","D",4),("D","C",2),("C","A",3),("B","E",5),("E","D",0)]
	print("B to E")
	print(djikstra(edges,"B","E"))













