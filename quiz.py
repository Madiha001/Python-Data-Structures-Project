import random

#this function will return the key-value pair where key is the word and defination is the value
def get_def_and_pop(word_list, word_dict):
	random_index = random.randrange(len(word_list))
	word = word_list.pop(random_index)
	definition = word_dict.get(word)
	return word,definition #return word and definition as a tuple

#split the string into word and definition
def get_word_definition(rawstring):
    word, definition = rawstring.split(',', 1)
    return word, definition

#read file of words and definition
fh = open("Vocabulary_list.csv", "r")
wd_list = fh.readlines()

#create file of words and definition without duplicate entries
#wd_list.pop(0)
wd_set = set(wd_list)
fh = open("Vocabulary_set.csv", "w")
fh.writelines(wd_set)

#creating dictionary
word_dict = dict()
for rawstring in wd_set:
    word, definition = get_word_definition(rawstring)
    word_dict[word] = definition

#loop for creating quiz question with multiple choices
while True:
	wd_list = list(word_dict) #list of words
	choice_list = []#choicelist of definitions
	for x in range(4):#max 4 choices
		word, definition = get_def_and_pop(wd_list, word_dict)
		choice_list.append(definition)
	#shuffle the choices
	random.shuffle(choice_list)
	#printing a word as a quiz question
	print(word)
	print("-------------")
	#printing the choices using for each loop
	for idx, choice in enumerate(choice_list):
		#printing index
		print(idx+1, choice)
	#getting input from the user
	choice = int(input("Enter 1,2,3,4; 0 to exit: "))
	#if user selects the correct choice
	if choice_list[choice-1] == definition:
		print("Correct!\n")
	#if user wants to exit
	elif choice == 0:
		exit(0)
	#if user selects the wrong choice
	else:
		print("Incorrect You lose this\n")
