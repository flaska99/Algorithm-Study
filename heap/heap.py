#힙 자료구조를 구현합니다

class MinHeap() :
    def __init__(self):
        self.heap = []
    
    def push(self, val) :
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)
        
    def pop(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root
    
    def build_heap(self, arr) :
        self.heap = arr[:]
        for i in range(len(self.heap) // 2 - 1, -1, -1) :
            self._heapify_down(i)
    
    def _heapify_up(self, index) :
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def _heapify_down(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        elif right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        
        if smallest != index :
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)
    
    def __str__(self) :
        return str(self.heap)
