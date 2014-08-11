#########
# Homework 2
# Dalston Ward
# August 10-11, 2014
#########

from random import uniform

###########the main class for the homework
class Portfolio():
	
#########required arguments are account holder (a name) and the initial deposit.  
	def __init__(self, account_holder, initial_deposit = 0):
		self.funds = initial_deposit
		self.stocks = {} #store stocks purchased here
		self.mutual_funds = {} #store mutual funds purchased here 
		self.account_holder = account_holder 
		self.history = History() #store account history here!
	
############for making a deposit to the account
	def addCash(self, amount):
		#try/except makes sure that you're giving the right input.  
		try:
			float(amount)
			if amount <= 0:
				raise Exception 
		except:
			print "Not a valid amount of money.  Please enter numeric characters greater than zero only."
			raise Exception
		self.funds += amount
		self.history.log.append("$%.2f deposited.  Available funds now $%.2f." % (amount, self.funds))
		print "Congrats! $%.2f added to your account.  Total balance now $%.2f." % (amount, self.funds)

############# for withdrawing funds from the account 		
	def withdrawCash(self, amount):
		try: #try/except to make sure you're giving the right input
			float(amount)
		except:
			print "Not a valid amount of money.  Please enter numeric characters only."
			raise Exception
		if self.funds >= amount: # Can't take out more money than you're got! 
			self.funds -= amount
			self.history.log.append("$%.2f withdrawn.  Available funds now $%.2f." % (amount, self.funds))
			print "Congrats!  $%.2f withdrawn from your account.  Total balance now $%.2f." % (amount, self.funds)
		else:
			print "Withdraw amount exceeds account balance. Transaction not completed."	
			
######## function to buy some new stocks.  		
	def buyStock(self, n_shares, stock_name):
		try:
			int(n_shares) #can only buy integer numbers of stocks
			if n_shares <= 0:
				raise Exception
		except:
			print "Can only buy positive, whole number shares of stocks.  Please enter a valid number of shares"
			raise Exception
		if n_shares * stock_name.price > self.funds:
			print "Can't complete transaction.  Not enough funds!"
		else:
			self.funds -= n_shares*stock_name.price #update funds
			if stock_name.tick_sym not in self.stocks.keys(): #create a key if not pre-existing
				self.stocks[stock_name.tick_sym] = n_shares
			else:
				self.stocks[stock_name.tick_sym] += n_shares #else update key
			self.history.log.append("%d share(s) of %s purchased." % (n_shares, stock_name.tick_sym))
			self.history.log.append("$%.2f used to purchased stock.  Available funds now $%.2f." % (n_shares*stock_name.price, self.funds))
			print "Congrats!  You purchased %d share(s) of %s at a total cost of $%.2f." % (n_shares, stock_name.tick_sym, n_shares * stock_name.price)			
		
#########function to sell stocks back.  Takes as arguments the number of shares to sell and the stock to sell
	def sellStock(self, n_shares, stock_name):
		try: #make sure that its an integer number of shares and that you own that stock
			int(n_shares)
			if stock_name.tick_sym not in self.stocks.keys():
				raise Exception
		except:
			print "Can only sell whole shares of stocks in your portfolio.  Please enter a valid number of shares a stock you own."
			raise Exception		
		if self.stocks[stock_name.tick_sym] < n_shares: #make sure that you aren't selling more shares than you own!
			print "Cannot sell more shares than you own!  Transaction not completed."
		else:		
			if self.stocks[stock_name.tick_sym] == n_shares: #remove this stock from your portfolio entirely if selling all shares 
				self.stocks.pop(stock_name.tick_sym, None)				
			else: #just update your number of shares
				self.stocks[stock_name.tick_sym] -= n_shares			
			income = n_shares * uniform(.5 * stock_name.price, 1.5 * stock_name.price) #sale price
			self.funds += income #update funds
			self.history.log.append("%d share(s) of %s sold." % (n_shares, stock_name.tick_sym))
			self.history.log.append("$%.2f earned from sale.  Available funds now $%.2f." % (income, self.funds))
			print "Congrats!  You earned $%.2f from this sale" % income

########## function to buy mutual funds.  Takes as arguments how much to buy and which fund to purchase
	def buyMutualFund(self, shares, mf_name):
		try: #make sure that its an appropriate number of shares to purchase
			float(shares)
			if shares <= 0:
				raise Exception
		except:
			print "Can only buy positive shares of stocks.  Please enter a valid number of shares."
			raise Exception	
		if shares > self.funds: #make sure you can afford this transaction
			print "Can't complete transaction.  Not enough funds!"
		else:
			self.funds -= shares #update funds
			if mf_name.tick_sym not in self.mutual_funds.keys(): #create a key if not pre-existing
				self.mutual_funds[mf_name.tick_sym] = shares
			else:
				self.mutual_funds[mf_name.tick_sym] += shares #else update key
			self.history.log.append("%d share(s) of %s purchased." % (shares, mf_name.tick_sym)) #update history
			self.history.log.append("$%.2f used to purchased mutual funds.  Available funds now $%.2f." % (shares, self.funds)) #update history 
			print "Congrats!  You purchased %.f share(s) of %s at a total cost of $%.2f." % (shares, mf_name.tick_sym, shares)		

#########function to sell mutual funds shares back.  Takes as arguments the number of shares to sell and the mutual fund to sell
	def sellMutualFund(self, shares, mf_name):
		try: #make sure that its a positive number and that you own that stock
			float(shares)
			if mf_name.tick_sym not in self.mutual_funds.keys():
				raise Exception
			if shares <= 0:
				raise Exception
		except:
			print "Can only sell positive shares of mutual funds in your portfolio.  Please enter a valid number of shares a mutual fund you own."
			raise Exception		
		if self.mutual_funds[mf_name.tick_sym] < shares: #make sure that you aren't selling more shares than you own!
			print "Cannot sell more shares than you own!  Transaction not completed."
		else:	
			if self.mutual_funds[mf_name.tick_sym] == shares: #remove this mutual fund from your portfolio entirely if selling all shares 
				self.mutual_funds.pop(mf_name.tick_sym, None)				
			else: #just update your number of shares
				self.mutual_funds[mf_name.tick_sym] -= shares			
			income = shares * uniform(0.9, 1.2) #sale price
			self.funds += income #update funds
			self.history.log.append("%d share(s) of %s sold." % (shares, mf_name.tick_sym)) #update history
			self.history.log.append("$%.2f earned from sale of mutual funds.  Available funds now $%.2f." % (income, self.funds)) #update history. 
			print "Congrats!  You earned $%.2f from this sale" % income	
	
######### function to print the portfolio
	def __str__(self):
		owner_print = "Account holder: %s\n" % self.account_holder #Who's account?
		funds_print = "Available Funds: $%.2f \n" % self.funds #current balance
		stocks_print = "Stocks: \n" #next two lines create owned stocks string
		for stock in self.stocks:
		 		stocks_print += ("\t" +  str(self.stocks[stock]) + "  " + stock + "\n")
		mutual_funds_print = "Mutual Funds: \n" #next two lines create owned MF's string
		for mutual_fund in self.mutual_funds:
			mutual_funds_print += ("\t" +  str(self.mutual_funds[mutual_fund]) + "  " + mutual_fund + "\n")
		return owner_print + funds_print + stocks_print + mutual_funds_print #put it all together and return. 		

		
class Stock():
	def __init__(self, price, tick_sym):
		try:
			if not isinstance(tick_sym, str): #Make sure the input is appropriate
				raise Exception
		except:
			print "Not a valid ticker symbol.  Please enter a string."
			raise Exception
		try:
			float(price)
		except: 
			print "Not a valid stock price.  Please enter numeric characters only" 
			raise Exception
		self.tick_sym = tick_sym
		self.price = price
		
	def __str__(self):
		return "Stock name: %s; Price per share: $%d" % (self.tick_sym, self.price)
	
class MutualFund():
	def __init__(self, tick_sym):
		try:
			if not isinstance(tick_sym, str): #Make sure the input is appropriate
				raise Exception
		except:
			print "Not a valid ticker symbol.  Please enter a string."
			raise Exception
		self.tick_sym = tick_sym
	
	def __str__(self):
		return "Mutual Fund name is %s." % self.tick_sym

# I created the history class so that I could specify a specific way to print the history.  
class History():
	def __init__(self):
		self.log = []
	
	def __str__(self):
		return "Transaction history: \n" + '\n'.join(self.log)				
#		
# portfolio = Portfolio("Dalston Ward")
# portfolio.addCash(50)
# print portfolio.funds
# #portfolio.addCash("Fifty")
# #portfolio.addCash(-5)
# stock = Stock(22, "woo")
# stock2 = Stock(5, "DGW")
# portfolio.buyStock(1, stock)
# print portfolio.stocks
# print portfolio
# portfolio.addCash(50)
# print portfolio.funds
# portfolio.buyStock(1, stock)
# print portfolio.stocks
# portfolio.buyStock(3, stock2)
# print portfolio.stocks
# portfolio.sellStock(3, stock2)
# print portfolio.stocks
# portfolio.withdrawCash(2)
# mf1 = MutualFund("HEY")
# mf2 = MutualFund("HO")
# portfolio.buyMutualFund(1.7,mf1)
# print portfolio.mutual_funds
# portfolio.sellMutualFund(.5, mf1)
# portfolio.buyMutualFund(.9, mf2)
# print portfolio.mutual_funds
# print portfolio
# portfolio.sellMutualFund(.5, mf1)
# print portfolio
# print portfolio.history
# portfolio = Portfolio("Dalston Ward")
# portfolio.addCash(50)
# print portfolio.history
# 
# 
