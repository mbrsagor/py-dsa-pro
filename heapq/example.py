import heapq


class PQNode(object):

    def __init__(self, key, value):
        self.key = key
        self.value = value

    # compares the second value
    def __lt__(self, other):
        return self.value < other.value

    def __str__(self):
        return f"{self.key}, {self.value}"


_input = [PQNode(1, 4), PQNode(7, 4), PQNode(6, 9), PQNode(2, 5)]
hin_put = []
for item in _input:
    heapq.heappush(hin_put, item)

while hin_put:
    print(heapq.heappop(hin_put))
