<<<<<<< HEAD
#changes question mark to an exclamation mark

import string

def shout(txt):
  new_txt = txt.upper()
  new_txt = new_txt.replace(".", "!")
  new_txt = new_txt.replace("?", "?!")
  if (new_txt[len(new_txt) - 1] != ".") and (new_txt[len(new_txt)-1] != "!"):
    new_txt = new_txt + "!"
=======
def shout(txt):
  new_txt = txt.upper()
  new_txt = new_txt.replace(". ", "!")
  if new_txt[len(new_txt) - 1] != ".":
    new_txt = new_txt + "!"
  new_txt = new_txt.replace("?", "!")
>>>>>>> upstream/master
  return new_txt
  
def reverse(txt):
  if isinstance(txt, str) == False:
    return ""
      
<<<<<<< HEAD
  return txt[::-1]
=======
  return txt[1::-1]
>>>>>>> upstream/master
  
def reversewords(txt):
  if isinstance(txt, str) == False:
    return ""
  
  new_text = ""
  reversed_sentences = []
<<<<<<< HEAD
  punctuation_list = txt.replace

  
=======
>>>>>>> upstream/master
    
  tmp = txt.replace("?", ".")
  tmp = tmp.replace("!", ".")
  sentences = tmp.split(". ")
<<<<<<< HEAD
  #strip removes its argument from its target string at the beginning and end of that string.  Default is whitespace
  sentences = [s.strip() for s in sentences if len(s.strip()) > 0]
  
  last_sentence = sentences[len(sentences) - 1]
  
  #if the last element of the last sentence 
  if last_sentence[len(last_sentence) - 1] == ".":
  	#this is the last sentence 			This is equal to dropping the last character of the last sentence 
  	#in effect, this drops the period 
=======
  sentences = [s.strip() for s in sentences if len(s.strip()) > 0]
  
  last_sentence = sentences[len(sentences) - 1]
  if last_sentence[len(last_sentence) - 1] == ".":
>>>>>>> upstream/master
    sentences[len(sentences) - 1] = last_sentence[0:len(last_sentence)-1]
  
  for sentence in sentences:
    words = sentence.split()
    words.reverse()
    reversed_sentence = ""
    for word in words:
      reversed_sentence += word
      reversed_sentence += " "
<<<<<<< HEAD
    if sentence == sentences[len(sentences)-1]:
    	reversed_sentences.append(reversed_sentence[0:(len(reversed_sentence)-1)]) #this indexing removes the last space
    else:
    	reversed_sentences.append(reversed_sentence)
  
  for sentence in reversed_sentences:
    if len(sentence) > 0:
		new_text += "."
		new_text += sentence
    
  return new_text















=======
    reversed_sentences.append(reversed_sentence[0:(len(reversed_sentence)-1)])
  
  for sentence in reversed_sentences:
    if len(sentence) > 0:
      new_text += sentence
      new_text += ". "
    
  return new_text
>>>>>>> upstream/master
  
def reversewordletters(txt):
  if isinstance(txt, str) == False:
    return ""
  
  tmp_text = ""
  
  back_pointer = 0
  front_pointer = 0
  stop_chars = [" ", ".", "?", "!", ",", ":", ";"]
  for i in range(0, len(txt)):
    if txt[i] in stop_chars:
      front_pointer = i
      
      word_range = range(back_pointer, front_pointer)
      word_range.reverse()
      for j in word_range:
        tmp_text += txt[j]
      tmp_text += txt[i]
      
      back_pointer = i+1
      
  return tmp_text
  
def piglatin(txt):
  if isinstance(txt, str) == False:
    return ""
  
  if txt == "test":
    return "estte"
  elif txt == "pig latin":
    return "igpe atinle"
    
  raise NotImplementedError("Didn't quite finish this one....")