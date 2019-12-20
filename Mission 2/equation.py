#David Lefebvre: solveur d'équation diophantienne

print("Pour x^a + y^b = z^c")

#Valeurs a entrer par l'utiulisateur
a = int(input("Veuillez entrer une valeur de a: "))
b = int(input("Veuillez entrer une valeur de b: "))
c = int(input("Veuillez entrer une valeur de c: "))
max = int(input("Veuillez entrer une valeur max pour x, y et z: "))
print("Initialisation du calcul:")

#Compteur de solutions
Valid_answer = 0
Invalid_answer = 0
DivCommun = []
DivA = []
DivB = []

def IsValid(a, b, c): #Verifie si c est un multiple du pgcd de a et b
	for i in range (1,a+1):
		if a % i == 0:
			DivA.append(i)
		else:
			continue
	for i in range (1,b+1):
		if b % i == 0:
			DivB.append(i)
		else:
			continue
	a_set = set(DivA)
	b_set = set(DivB)
	DivCommun = a_set & b_set
	DivCommun_f = list(DivCommun)
	if c % DivCommun_f[-1] == 0:
		return True
	else:
		return False


"""	r = a % b
	if c % r == 0:
		return False
	else:
		return True
"""

def FinalResult():
	if Valid_answer == 0:
		if Invalid_answer == 0:
			print("Aucune reponse n'a ete trouvee")
		else:
			print("Aucune reponse n'a ete trouvee mais ", Invalid_answer, " solutions on ete rejetees")
	else:
		if Invalid_answer == 0:
			print(Valid_answer, " solutions ont ete calculee")
		else:
			print(Valid_answer, "solutions ont ete calculee mais ", Invalid_answer, " ont ete rejetees")


for x in range(1, max):
	for y in range(1, max):
		for z in range(1, max):
			if x**a + y**b == z**c:
				if IsValid(x, y, z) == True:
					print("x:",x,"\t","y:",y,"\t","z:",z)
					Valid_answer += 1 
				else:
					print("x:",x,"\t","y:",y,"\t","z:",z, " ATTENTION: cette solution est rejetee")
FinalResult()