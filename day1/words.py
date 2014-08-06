<<<<<<< HEAD
# file = open('words.txt')
# 
# for line in file:
#   word = line.strip()
#   print word
#   
#   

#does this word have an e?
# def has_no_e(word):
# 	return not("e" in word)
# 
# print has_no_e("cheese")

#is a word made of only some letters 
# def uses_only(word, available):
# 	available = available.lower()
# 	word = word.lower()
# 	for letter in word:
# 		if not(letter in available):
#  			return False
# 	return True 
# 
# print uses_only("dad", "da")

# Uses ALL letters
# def uses_only(word, letters):
# 	letters = letters.lower()
# 	word = word.lower()
# 	for i in range(0,len(letters)):
# 		if letters[i] in word:
# 			continue
# 		else:
# 			return False
# 	return True 
# 	
# print uses_only("Bagelelelelelele", "agleb")

#in alphabetical order
def is_abecedarian(word):
	return "".join(sorted(word))==word
	
	
print is_abecedarian("bagel")
=======
file = open('words.txt')

for line in file:
  word = line.strip()
  print word
>>>>>>> upstream/master
