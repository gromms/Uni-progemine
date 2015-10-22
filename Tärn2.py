#1. leia sona pikkus
#2. loe listist õige pikkusega sõnad
#3. vota taht ja kontrolli selle esinevust kõigis alles jäänud sõnades
#4. leia täht, mis eemaldab võimalikult palju sõnu
#4.1 filtreeri sõnad vastavalt antud tähe asukohale sõnas
#5. eemalda need sõnad
#6. korda 3-5 kuni jääb alles 1 sõna
#7. paku sõna

#Esiteks leian võimalikult kiiresti ühe sisalduva tähe

from math import *
import string

def findOccurance(wordList, letter, occurance): #Leiab tähtede sisalduvuse antud listi sõnades
	for i in range(0, len(wordList)):
		if(wordList[i].find(letter) >= 0):
			occurance += 1
	#print(letter, 'Occurance =', occurance)
	#print(letter, 'Occurance ratio =', occurance / len(wordList))
	return occurance / len(wordList)

def bestLetter(wordList, letterList):
	currentBest = ['', 0]
	occurance = 0
	#print(len(letterList))
	#print(len(wordList))
	#print('letter list:', letterList)
	#print('letter list len:', len(letterList))
	for letter in range(0, len(letterList)):
		for word in wordList:
			if word.find(letterList[letter]) != -1:
				occurance += 1
		contains = occurance / len(wordList)
		occurance = 0
		#print(letterList[letter], contains)
		if contains > currentBest[1]:
			currentBest[0] = letterList[letter]
			currentBest[1] = contains
			#print(currentBest)

	return currentBest[0]

def filterList(wordList, letter, letterPos): #letterPos - list, mis sisaldab tähtede asukohta antud sõnas
	newList = []
	if len(letterPos) > 0:
		for word in wordList:
			sobib = True
			for pos in letterPos:
				if word[pos] != letter:
					sobib = False
			if sobib:
				newList.append(word)
	else:
		for word in wordList:
			if word.find(letter) == -1:
				newList.append(word) 
	return newList

def scanWord(newWord, guessedLetter): #Kontrollib, kas uues vihjes on pakutud täht
	letterPos = []
	for i in range(0, len(newWord)):
		if newWord[i] == guessedLetter:
			letterPos.append(i)
	return letterPos

def findLetter(wordList, letterList): #Leiab parima tähe, mida pakkuda
	#letterList = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','V','W','Õ','Ä','Ö','Ü','X','Y']
	#letterList = ['a', 'b', 'c']
	#print('Letters in list:', len(letterList))
	bestGuess = ['', 1]

	for i in range(0, len(letterList)):
		oc = findOccurance(wordList, letterList[i], 0)
		if oc > 0:
			x = abs(0.5 - oc)
			if x <= bestGuess[1]:
				bestGuess[0] = letterList[i]
				bestGuess[1] = x
	return bestGuess		

with open('sonad.txt', encoding = 'utf-8') as f:
	word = input()
	wordLen = len(word)
	#count = 1
	wordList = []

	letterList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','v','w','õ','ä','ö','ü','x','y']

	while 1: #Loeb alles jäänud sõnad vastavalt ette antud sõna pikkusele failist listi
		line = f.readline().strip()
		if not line:
			break
		elif len(line) == wordLen:
			wordList.append(line)
	#print(len(wordList))
	#loop = True
	if wordLen != 2 and wordLen != 7 and wordLen != 6:
		while len(wordList) > 1:
			result = bestLetter(wordList, letterList)
			#print(result)
			letter = result
			#print(letter)
			letterList.remove(letter)
			print(letter.upper())
			word = input().lower()
			#print(word.find(letter))
			if word.find(letter) != -1:
				#print(letter)
				letterPos = scanWord(word, letter)
				wordList = filterList(wordList, letter, letterPos)
				#print('edasi')
				#loop = False


	else:
		while len(wordList) > 1: #Leiab parima tähe ja pakub neid seni, kuni jääb alles üks sõna
			guess = findLetter(wordList, letterList)
			letterList.remove(guess[0])
			#count += 1
			#print('List len:', len(wordList))
			#print('Guessed letter:', guess[0], '|| Occurance:', guess[1])
			print(guess[0].upper())
			#print(wordList)
			#print(letterList)
			word = input().lower()
			letterPos = scanWord(word, guess[0])
			wordList = filterList(wordList, guess[0], letterPos)
	print(wordList[0].upper())
	#print(count)