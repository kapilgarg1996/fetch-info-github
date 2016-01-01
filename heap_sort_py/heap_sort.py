import sys

class HeapSort:
	"""
		Class to sort a list in increasing order 
		How to use:
		#create object of this class using your unordered list
				obj = HeapSort(list)
		#get your sorted list
				list = obj.getFinal()
	"""

	def exchange(self, i, j):
		temp = self.array[i]
		self.array[i] = self.array[j]
		self.array[j] = temp

	def left(self, i):
		return 2*i+1

	def right(self, i):
		return 2*i+2

	def max_heapify(self, i):
		leftChild = self.left(i)
		rightChild = self.right(i)
		if leftChild < self.size and self.array[i]<self.array[leftChild]:
			largest=leftChild
		else:
			largest=i
		if rightChild < self.size and self.array[rightChild]>self.array[largest]:
			largest = rightChild

		if largest != i:
			self.exchange(i, largest)
			self.max_heapify(largest)

	def build_max_heap(self):
		self.size = self.length
		tar = self.length/2
		for x in range(tar-1, -1, -1):
			self.max_heapify(x)

	def sort_func(self):
		self.build_max_heap()
		tar = self.length
		for x in range(tar-1, 0, -1):
			self.exchange(0, x)
			self.size-=1
			self.max_heapify(0)

	def __init__(self, listg):
		self.array = listg
		self.size = len(listg)
		self.length = len(listg)
		self.sort_func()

	def getFinal(self):
		return self.array

if __name__ == '__main__':
	x = map(int, sys.argv[1:])
	goal = HeapSort(x)
	x = goal.getFinal()
	print x