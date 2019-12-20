#Mission 6 

listening = True
file = ''
word2frequence = {}

def File(command):
	#file <name>: spécifie le nom d'un fichier sur lequel l'outil doit travailler
	global file
	filetoread = splitedcommand[1]
	file = filetoread
	try:
		file = open(filetoread, "r")
		return True
	except:
		return False

def Info():
	#info: montre le nombre de lignes et de caractères du fichier
	lines = 0
	chars = 0
	info = []
	for line in file.readlines():
		lines += 1
		char_line = line.split()
		for i in str(char_line):
			chars += 1
	info.append(lines)
	info.append(chars)
	print(info)


def Dictionnary():
    #dictionary: utilise le fichier comme dictionnaire à partir de maintenant
    for line in file.readlines():
        wordandfrequence = line.split(',')
        word2frequence[wordandfrequence[0]] = wordandfrequence[1]
    """
    for keys,values in word2frequence.items():
        print(keys)
        print(values)
	"""

def Search(word):
	searchedword = splitedcommand[1]
	wordtofound = list(searchedword)
	wordtofoundlen =  len(wordtofound)
	word_found = False
	founded_word = []
	wordlist = []
	for line in file:
		fileline = line.split(',')
		wordlist.append(list(fileline[0]))

	while word_found == False:
		erreurs = 0
		for word in wordlist:
			check = wordtofoundlen - erreurs
			checked_letters = 0
			for i in range(len(wordtofound)):
				if wordtofound[i] in word:
					checked_letters += 1
			if checked_letters == check:
			#if len(word) == wordtofoundlen:
				founded_word.append(word)
				word_found = True
			else:
				erreurs += 1

	print(founded_word)

def Sum():
	total_sum = 0
	lensplitcom = len(splitedcommand)
	for i in range(1, lensplitcom):
		total_sum += int(splitedcommand[i])
	print(total_sum)

def Avg():
	total_sum = 0
	avg = 0
	lensplitcom = len(splitedcommand)
	for i in range(1, lensplitcom):
		total_sum += int(splitedcommand[i])
	avg = (total_sum/(lensplitcom-1))
	print(avg)

def Exit():
	print('The client has closed the script')
	global listening
	listening = False


while listening:
	command = input( "root@root >>> " )
	splitedcommand = command.split(' ')
	
	if splitedcommand[0] == "file":
		if File(splitedcommand[1]):
			print('File found.')
		else: 
			print('file not found')
	if splitedcommand[0] == "info":
		Info()
	if splitedcommand[0] == "dictionnary":
		Dictionnary()
	if splitedcommand[0] == "search":
		Search(splitedcommand[1])
	if splitedcommand[0] == "sum":
		Sum()
	if splitedcommand[0] == "avg":
		Avg()
	if splitedcommand[0] == "exit":
		Exit()
