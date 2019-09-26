
placa=[40,40,1600]


def Area(A,H):
   arreglo=[]
   for i in range (len(A)):
         par = (A[i],H[i],A[i]*H[i])
         arreglo.append(par)
        
   return arreglo


A=[4,3,6,6,5]
H=[3,4,3,1,7]

def suma(A,placa):       
  suma=0
  maximol=0
  maximoa=0
  print(placa[0]) 
  for i in range (len(A)):
    suma+=A[i]
    maximoa+=A[i]
    if maximoa>placa[0]:
      maximoa-=A[i]
  return maximoa

def ordenar(arreglo):
  for i in range (len(arreglo)):
    arreglo[i][2].sort(reverse=True)
  return arreglo

def burbuja(arr):
    n = len(arr)
 
    
    for i in range(n):
 
        
        for j in range(0, n-i-1):
 
            
            if arr[j][2] < arr[j+1][2] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
""" def Area(A,H):
   arreglo=[]
   for i in range (len(A)):
         par = (A[i],H[i])
         arreglo.append(par) 
        
   return arreglo """

def llenar(arr,placa):
  posiciones=[]
  posicionesY=[]
  xp = placa[0]
  xy = placa[1]

  x=0
  y=0

  for i in range (len(arr)):
    print(arr[i][0])
    if  (x + arr[i][0]) > xp:
      posiciones.append((x,y,i))
      x+=arr[i][0]
      arr.pop(i)
  return posiciones
print (A[1]+H[2])
print (burbuja(Area(A,H)))
print(Area(A,H))
print (suma(A,placa))
print(llenar(A,placa))
