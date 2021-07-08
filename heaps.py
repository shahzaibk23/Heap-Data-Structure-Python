# DAA ASSIGNMET 03
# SHAZAIB(18B-050-SE)

class Heaps:
    def __init__(self):
        self.heap = []  # initiate heap with list

    # Max Heapify Q1
    def maxHeapify(self,n,i):
        largest,left,right = i, i*2, i*2+1                                      # initialized largest,left and right by algo
        if left < n and self.heap[largest] < self.heap[left]:
            largest = left                                                      # if left 
        elif right < n and self.heap[largest] < self.heap[right]:
            largest = right                                                     # else if right

        if largest != i:
            self.heap[i],self.heap[largest] = self.heap[largest],self.heap[i]   # if largest != i
            self.maxHeapify(n,largest)                                          # recursing maxHeapify func

    # Build Max Heap Q2
    def buildMaxHeap(self):
        self.heap.remove(self.heap[0])                                          # removing root
        self.heapSorter()                                                       # sorting the rest

    # Heap Extract Max Q3
    def heapExtractMax(self,item):
        if item not in self.heap:
            return False                                                        # if item not in heap, return False
        elif self.heap.index(item) == 0:
            return 0                                                            # else if item is root, return 0
        else:
            self.heap.remove(item)                                              # otherwise, remove/extract the item
            self.heapSorter()                                                   # sort the rest

    # Heap Increase Key Node Q4
    def heapIncreaseKeyNode(self,lastItem,nextItem):    
        if lastItem not in self.heap or nextItem not in self.heap:
            return False                                                        # if any last or next are not in heap already, return False
        elif self.heap.index(lastItem) == 0:
            return 0                                                            # else if lastItem (to remove) is root, return 0
        else:
            index = self.heap.index(lastItem)                                   # otherwise; saving the index of lastItem (to remove)
            self.heap.remove(lastItem)                                          # removed lastItem from the heaps
            self.heap.insert(index,nextItem)                                    # insert nextItem at lastItem saved index
            self.heapSorter()                                                   # sorting at the end

    # Sorter to execute Max Heapify
    def heapSorter(self):
        length = len(self.heap)                                                 # saving length of heap
        for i in range(length//2 -1, -1, -1):                                   
            self.maxHeapify(length,i)                                           # loop for nodes which are leaves
        for i in range(length-1,0,-1):
            self.heap[i],self.heap[0] = self.heap[0],self.heap[i]               # swapping
            self.maxHeapify(i,0)                                                # extracting item one by one

    # Insert Max Heap Q5
    def insertMaxHeap(self,value):
        self.heap.append(value)                                                 # append new value in heap
        indexOfValue = self.heap.index(self.heap[-1])                           # index of newly added value saved
        parentOfValue = ((self.heap.index(self.heap[-1]) -1 )//2)               # parent of newly added value saved
        while parentOfValue >= 0:                                               # loop to sort the array a/c to newly added value
            if self.heap[parentOfValue] < self.heap[indexOfValue]:              # if parent is smaller than newly added value, both nodes are swapped
                self.heap[parentOfValue],self.heap[indexOfValue] = self.heap[indexOfValue],self.heap[parentOfValue]
                indexOfValue = parentOfValue                                    # then, current index changes to of parent
                parentOfValue = ((parentOfValue -1) //2)                        # parent is updated with position of newly added value
            else:
                parentOfValue = ((parentOfValue -1) //2)                        # else, updating the parent value directly


# --- DRIVER CODE ---
HEAP = Heaps()                                                                  # Heap class object instantiated

HEAP.insertMaxHeap(7)                                                           # insert 7 in heap
HEAP.insertMaxHeap(3)                                                           # insert 3 in heap
HEAP.insertMaxHeap(2)                                                           # insert 2 in heap
HEAP.insertMaxHeap(9)                                                           # insert 9 in heap
HEAP.insertMaxHeap(8)                                                           # insert 8 in heap
print(f"After Insertion: {HEAP.heap}")                                          # print heap after insertion

HEAP.heapSorter()                                                               # sorting heap with heapSorter method
print(f"After Sorting: {HEAP.heap}")                                            # print heap after sorting

HEAP.buildMaxHeap()                                                             # build max heap with buildMaxHeap mehod
print(f"After Build Max Heap: {HEAP.heap}")                                     # print heap after buildMaxHeap

HEAP.heapExtractMax(7)                                                          # extracting heap max with heapExtractMax method
print(f"After Heap Extract Max: {HEAP.heap}")                                   # print heap after heapExtractMax

HEAP.heapIncreaseKeyNode(8,9)                                                   # increasing heap key node with heapIncreaseKeyNode method
print(f"After Heap Increase Key Node: {HEAP.heap}")                             # print heap after heapIncreaseKeyNode
