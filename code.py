import heapq

def maxProbability(n, edges, succProb, start, end):
    adj = [[] for _ in range(n)]
    for i in range(len(edges)):
        a, b = edges[i]
        p = succProb[i]
        adj[a].append((b, p))
        adj[b].append((a, p))
    
    max_prob = [0.0] * n
    max_prob[start] = 1.0
    heap = [(-1.0, start)]  # Using min-heap to simulate max-heap
    
    while heap:
        current_neg_prob, node = heapq.heappop(heap)
        current_prob = -current_neg_prob
        
        if node