class QuickSort(object):
	"""
	A class to sort an array using quicksort technique.
	How-to-use:
	x = new QuickSort(array)
	x.sort() #to sort in increasing order
	x.revSort() #to sort in decreasing order
	x.sort(compare) #to sort according to your compare function
	print array #to print sorted array
	"""
	def __init__(self, arr):
		self.__arr = arr

	def sort(self, comp=None):
		if comp:
			self.comp = comp
		else:
			self.comp = self.__lt__
		self.__qSort(0, len(self.__arr))
	
	def __qSort(self, l, r):
		if(l<r):
			x = self.__partition(l, r)
			self.__qSort(l, x)
			self.__qSort(x+1, r)

	def __partition(self, l, r):
		x = self.__arr[r-1]
		i = l-1
		for j in range(l, r):
			if(self.comp(j, r-1)):
				i = i+1
				self.__swap(i, j)
		self.__swap(i+1, r-1)
		return i+1

	def __swap(self, i, j):
		temp = self.__arr[i]
		self.__arr[i] = self.__arr[j]
		self.__arr[j] = temp

	def __lt__(self, i, j):
		return self.__arr[i]<self.__arr[j]

	def __gt__(self, i, j):
		return self.__arr[i]>self.__arr[j]

	def revSort(self):
		self.sort(self.__gt__)