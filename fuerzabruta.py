<<<<<<< HEAD
maxl=400
maxa=30

def Area(A,H):
   
  
  
  
   arreglo=[]
   for i in range (len(A)):
         par = (A[i],H[i])
         arreglo.append(par)
        
   return arreglo

A=[2,4,6,6,15]
H=[2,5,3,1,7]

def suma(A):       
  suma=0
  maximol=0
  maximoa=0
  print(maxa)
  for i in range (len(A)):
    suma+=A[i]
    maximoa+=A[i]
    if maximoa>maxa:
      
    
      maximoa-=A[i]
  return maximoa



print (A[1]+H[2])
print(Area(A,H))
print (suma(A))

=======
class Bin:
	def __init__(self):
		self.list = []

	def addItem(self, item):
		self.list.append(item)

	def removeItem(self, item):
		self.list.remove(item)

	def sum(self):
		total = 0
		for elem in self.list:
			total += elem
		return total

	def show(self):
		return self.list


def first_fit(list_items, max_size):
	""" Returns list of bins with input items inside. """
	list_bins = []
	list_bins.append(Bin()) # Add first empty bin to list

	for item in list_items:
		# Go through bins and try to allocate
		alloc_flag = False

		for bin in list_bins:
			if bin.sum() + item <= max_size:
				bin.addItem(item)
				alloc_flag = True
				break
		
		# If item not allocated in bins in list, create new bin
		# and allocate it to it.
		if alloc_flag == False:
			newBin = Bin()
			newBin.addItem(item)
			list_bins.append(newBin)

	# Turn bins into list of items and return
	list_items = []
	for bin in list_bins:
		list_items.append(bin.show())

	return(list_items)

items = [8, 16, 12, 8, 45, 18, 30, 7, 10, 14, 9, 9, 52, 88]
bin_height = 60

# First-fit Algorithm
print(first_fit(items, bin_height))
>>>>>>> 6da0cdc1e5edc053582043cad9eedb04502f518c
