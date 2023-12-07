import heapq
heap = []
N = int(input()) # 가로 세로의 크기

for _ in range(N):
    nums = map(int,input().split())
    for n in nums:
        if len(heap) < N:
            heapq.heappush(heap, n)
        else:
            if heap[0] < n:
                heapq.heappop(heap)
                heapq.heappush(heap,n)

print(heap[0])
