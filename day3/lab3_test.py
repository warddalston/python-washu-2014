import unittest
from lab3 import *

#shout tests
class Shout_test(unittest.TestCase):
	
	def test_a_single_word(self):
		self.assertEqual("HELLO!", shout("hello"))
		
	#problem: doesn't change period to exclamation
	def test_a_word_with_a_full_stop(self):
		self.assertEqual("HELLO!", shout("hello."))
	
	#problem 1: changes a question mark to an exclamation point 	
	def test_a_sentence(self):
		self.assertEqual("HI! HOW ARE YOU DOING?!", shout("Hi! How are you doing?"))
	
	def test_two_sentences(self):
		self.assertEqual("MY NAME IS DALSTON! I LIKE CHEESE!", shout("My name is Dalston. I like cheese."))
	
	#Can't handle abbreviations
	def test_three_question(self):
		self.assertEqual("WHO ARE YOU?! WHAT ARE YOU DOING HERE?! DO YOU LIKE CHEESE?!", shout("Who are you? What are you doing here? Do you like cheese?"))
		
	def test_reverse_a_word(self):
		self.assertEqual("olleh", reverse("hello"))
	
	def test_reverse_word_with_space(self):
		self.assertEqual(" ecaps", reverse("space "))
	
	def test_two_words(self):
		self.assertEqual("dlrow olleH", reverse("Hello world"))
		
	def test_world_hello(self):
		self.assertEqual(".world hello", reversewords("hello world."))

	def test_sentences_two(self):
		self.assertEqual(".world Hello .Dalston I'm", reversewords("Hello world. I'm Dalston."))
		
	def test_punctuation(self):
		self.assertEqual("?you are How", reversewords("How are you?"))
				
if __name__ == '__main__':
	unittest.main()