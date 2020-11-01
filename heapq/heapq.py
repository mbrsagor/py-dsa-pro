import heapq

li = [10, 1, 5, 2, 11, 7, 21, 0]
heapq.heapify(li)
print(li)

heapq.heappop(li)  # heappop remove 1st item
print(li)
heapq.heappush(li, 12)  # heappush add last item
print(li)
