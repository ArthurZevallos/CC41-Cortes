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

