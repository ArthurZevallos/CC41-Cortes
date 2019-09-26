def MostrarAreas(G):
	n=len(G)
	resultado=[]
	for i in range(n):
		producto=G[i][0]*G[i][1]
		resultado.append((producto,G[i][0],G[i][1]))
	return resultado

def Ordenar(resultado):

	n=len(resultado)-1

	for i in range(n):
		for j in range(n-i):
			if resultado[j]<resultado[j+1]:
				resultado[j],resultado[j+1]=resultado[j+1],resultado[j]
	return resultado
    
def AreaTotal(resultado):
    n=len(resultado)
    sumaa=0
    for i in range(n):
        sumaa+=resultado[i]
    return sumaa



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
	list_bins.append(Bin())

	for item in list_items:
		alloc_flag = False

		for bin in list_bins:
			if bin.sum() + item <= max_size:
				bin.addItem(item)
				alloc_flag = True
				break
		
		if alloc_flag == False:
			newBin = Bin()
			newBin.addItem(item)
			list_bins.append(newBin)

	list_items = []
	for bin in list_bins:
		list_items.append(bin.show())

	return(list_items)

def Desperdicio():
    resultado=100-((AreaTotal(MostrarAreas(G))/planchaArea)*100)
    return resultado

def Planchas(G, AreaPlancha):
    n = len(G) 
    list_planchas1 = []
    list_planchas2 = []
    list_planchas_final = []
    for i in range(n):
        nuevoVolumen = AreaPlancha 
        nuevoVolumen -= G[i][0]
        if AreaPlancha >= nuevoVolumen:
            list_planchas1.append(G[i])
        if AreaPlancha <= nuevoVolumen:
            list_planchas2.append(G[i])
      
    '''print("hola",list_planchas1)
    print(list_planchas_final)
        
    for i in range(n):
        nuevoVolumen = AreaPlancha 
        nuevoVolumen -= G[i][0]
        if AreaPlancha >= nuevoVolumen:
            list_planchas2.append(G[i])'''
       
    list_planchas_final.append(list_planchas1)
    list_planchas_final.append(list_planchas2)
    return list_planchas_final

G=[(15,16),(11,13),(8,9),(5,6),(8,20)]
planchaAncho = 300
planchaAlto = 200
planchaArea = planchaAncho*planchaAlto
print("----- Cortes------")
print("X - Y",G)
print("------Cortes con su respectivo area y dimensiones------")
print("(Area - X - Y)",MostrarAreas(G))
print("------Cortes ordenamos-------")
print("(Area - X - Y)",Ordenar(MostrarAreas(G)))
print("------Cortes en su respectiva plancha------")
print(Planchas(Ordenar(MostrarAreas(G)),planchaArea))
print(Desperdicio)