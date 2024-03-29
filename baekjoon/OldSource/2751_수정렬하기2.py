# heap 정렬
import sys
n =  int(input())

def heap_sort(unsorted):
    n = len(unsorted)
    for i in range(n//2 -1, -1, -1): #build heap
        heapify(unsorted, i, n)
    #print(unsorted)
    for i in range(n-1, 0, -1):
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
        heapify(unsorted, 0, i)
    return unsorted

def heapify(unsorted, index, heap_size):
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
        largest = left_index
    if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
        largest = right_index
    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        heapify(unsorted, largest, heap_size)

unsorted = []
for i in range(n):
    unsorted.append(int(sys.stdin.readline().strip()))

heap_sort(unsorted)
for i in unsorted:
    print(i)
#print(heap_sort(unsorted))
