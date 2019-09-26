
maxl=400
maxa=30
def Area(A,H):
   arreglo=[]
   for i in range (len(A)):
         par = (A[i],H[i],A[i]*H[i])
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



print (A[1]+H[2])
print (burbuja(Area(A,H)))
print(Area(A,H))
print (suma(A))


