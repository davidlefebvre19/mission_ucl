#mission 7

listening = True
line_list = []

def ReadFile(filename):
	filetoread = splited_command[1]
	try:
		file = open(filetoread, 'r')
		for line in file.readlines():
			line_list.append(line[:-2])
		print('file found.')	
	except:
		print('file NOT found !')

def ShowFile():
	print(line_list)

def Get_Words(command):
	line = command[1:]

	punctuation = '!"#$%&\'()*+,-./:;?@[]^_`{|}~ '
	listed_punctuation = list(punctuation)

	for z in range(len(line)):
		for x in listed_punctuation:
			line[z] = line[z].replace(x, '')

	for i in range(len(line)):
		if line[i] == '':
			del line[i]
	print(line)

def create_index(filename):
	index = {}
	for linenumber in range(len(line_list)): 
		listed_words = line_list[linenumber].split(' ')
		for word in listed_words:
			if word not in index:		
				index[word] = {}
				index[word][linenumber] = 1
			else: 
				index[(word)][linenumber] += 1
	print(index)

while listening:
	command = input('search@py: ')
	splited_command = command.split(' ')
	if splited_command[0] == 'readfile':
		ReadFile(splited_command)
	if splited_command[0] == 'showfile':
		ShowFile()
	if splited_command[0] == 'get_words':
		Get_Words(splited_command)
	if splited_command[0] == 'rm_punct':
		remove_punctuation(splited_command)
	if splited_command[0] == 'create_index':
		create_index(splited_command[1])

