import math
class fibonacci_tree:
	def __init__(self,key):
		self.key = key
		self.order = 0
		self.children = []
	def add_at_the_end(self,t):
		self.children.append(t)
		self.order += 1
class fibonacci_heap:
	def __init__(self):
		self.trees = []
		self.count = 0
		self.least = None
	def insert(self,key):
		fb_tree = fibonacci_tree(key)
		self.trees.append(fb_tree)
		if self.least is None or key < self.least.key:
			self.least = fb_tree
		self.count += 1
	def get_min(self):
		if self.least == None:
			return None
		else:
			return self.least.key
	def extract_min(self):
		minimum = self.least
		if minimum is not None:
			for child in minimum.children:
				self.trees.append(child)
			self.trees.remove(minimum)
		if self.trees==[]:
			self.least=None
		else:
			self.least=self.trees[0]
			self.consolidate()
		self.count-=1
		return minimum.key
	def consolidate(self):
		aux = (floor_log2(self.count)+1)*[None]
		while self.trees!=[]:
			x = self.trees[0]
			order = x.order
			self.trees.remove(x)
			while aux[order] is not None:
				y=aux[order]
				if x.key > y.key:
					x,y=y,x
				x.add_at_the_end(y)
				aux[order]=None
				order+=1
			aux[order]=x
		self.least=None
		for k in aux:
			if k is not None:
				self.trees.append(k)
				if (self.least is None or k.key < self.least.key):
					self.least = k
def floor_log2(x):
	return math.frexp(x)[1]-1
heap = fibonacci_heap()
heap.insert(20)
heap.insert(30)
heap.insert(-50)
heap.insert(-10)
print(heap.extract_min())
