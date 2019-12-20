
solutions = 0
solutionsNonAutorises= 0

def DiviseursCommun(nombres): #nombres : [a,b,c]
  diviseurs = []
  response = 0
  for i in range(len(nombres)):
    nombre = nombres[i]
    for d in range(2,nombre+1):
      if nombre % d == 0:
        diviseurs.append(d)
  for diviseur in diviseurs:
    if(diviseurs.count(diviseur)>= len(nombres)):
      response = diviseur
      break
  return(response)

def FinalResult():
  if solutions == 0:
      print("Aucune solution trouvee")
  else:
      print(solutions, "solutions trouvees")
  if(solutionsNonAutorises==0):
    print("Aucune solution a diviseurs communs n a ete trouvees")
  else:
    print(solutionsNonAutorises,"solutions non autorises (diviseurs communs)")

print("pour x^a + y^b = z^c ")
a = int(input("Entrez la valeur du coefficient a : "))
b = int(input("Entrez la valeur du coefficient b : "))
c = int(input("Entrez la valeur du coefficient c : "))
max = int(input("Entrez la valeur maximale pour x et y : "))
print("Calcule 'brute-force' pour x^",a," + y^",b," = z^",c)

for x in range(1,max):
    for y in range(1,max):
      for z in range(1,max):
        if x**a + y**b == z**c:
          diviseurCommun = DiviseursCommun([x,y,z])
          if(diviseurCommun>0):
            # print("Attention diviseurs communs [",diviseurCommun,"] : \n ","x =", x, " y =", y,"z = ",z)
            solutionsNonAutorises += 1
          else:
            print("x =", x, " y =", y,"z =",z)
            solutions += 1
FinalResult()


