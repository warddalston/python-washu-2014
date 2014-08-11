#########
# Homework 2
# Dalston Ward
# August 10-11, 2014
#########

class Portfolio():
	
	def __init__(self, account_holder):
		self.funds = 0
		self.stocks = {}
		self.mutual_funds = {}
		self.account_holder = account_holder 
	
	def addCash(self, amount):
		try:
			float(amount)
		except:
			print "Not a valid amount of money.  Please enter numeric characters only."
			raise Exception
		self.funds += amount
# 		
# portfolio = Portfolio("Dalston Ward")
# portfolio.addCash(50)
# print portfolio.funds
# #portfolio.addCash("Fifty")