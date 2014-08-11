import unittest 

from portfolio import *

class PortfolioTest(unittest.TestCase):

	#create a portfolio to use in the tests
	def setUp(self):
		self.portfolio = Portfolio(account_holder = "Dalston Ward", initial_deposit = 0)
		self.HFH = Stock(20, "HFH")
 		self.DHW = Stock(15, "DHW")
		self.BRT = MutualFund("BRT")
		self.GHT = MutualFund("GHT")

	#test to make sure the object is created correctly
	def test_createPortfolio(self):
		self.assertEqual(0, self.portfolio.funds)
		self.assertEqual("Dalston Ward", self.portfolio.account_holder)

	#test to add cash to the portfolio and make sure it prints the right amount.  
	def test_addCash(self):
		self.portfolio.addCash(300.50)
		self.assertEqual(300.50, self.portfolio.funds)
		
		#test to remove cash to the portfolio and make sure it prints the right amount.  
	def test_withdrawCash(self):
		self.portfolio.addCash(300.50)
		self.portfolio.withdrawCash(50)
		self.assertEqual(250.50, self.portfolio.funds)
	
	#test to make sure that the stock created has the right name and price. 
	def test_createStock(self):
		self.assertEqual(20, self.HFH.price)
		self.assertEqual("HFH", self.HFH.tick_sym)
# 	
	#Test buying a stock and making sure that funds are removed from the account.  
	def test_buyStock(self):
		self.portfolio.addCash(300.50) 
		self.portfolio.buyStock(5, self.HFH)
		self.assertEqual({"HFH" : 5}, self.portfolio.stocks)
		self.assertEqual(200.50, self.portfolio.funds)
	
	#test buying two different stocks at once 	 	
	def test_buyTwoStocks(self):
		self.portfolio.addCash(300.50) 
		self.portfolio.buyStock(5, self.HFH)
		self.portfolio.buyStock(2, self.DHW)
		self.assertEqual({"HFH" : 5, "DHW" : 2}, self.portfolio.stocks)
		self.assertEqual(170.50, self.portfolio.funds)
	
	#test buying something you can't afford
	def test_cantAffordThis(self):
		self.portfolio.addCash(300.50) 
		self.portfolio.buyStock(25, self.HFH)
		self.assertEqual({}, self.portfolio.stocks)
				
	#test selling a stock.  Does portfolio change? 
	def test_sellStocks(self):
		self.portfolio.addCash(300.50) 
		self.portfolio.buyStock(5, self.HFH)
		self.portfolio.sellStock(3, self.HFH)
		self.assertEqual({"HFH" : 2}, self.portfolio.stocks)
	
	#test selling all of your stock.  
	def test_sellallStocks(self):
		self.portfolio.addCash(300.50) 
		self.portfolio.buyStock(5, self.HFH)
		self.portfolio.sellStock(5, self.HFH)
		self.assertEqual({}, self.portfolio.stocks)
					
	def test_createMutualFund(self):
		self.assertEqual("BRT", self.BRT.tick_sym)
		self.assertEqual("GHT", self.GHT.tick_sym)

	def test_buyMutualFunds(self):
		self.portfolio.addCash(300.50) 
		self.portfolio.buyMutualFund(3, self.BRT)
		self.assertEqual({"BRT" : 3}, self.portfolio.mutual_funds)
		self.assertEqual(297.50, self.portfolio.funds) 
		
	def test_sellMutualFunds(self):
		self.portfolio.addCash(300.50) 
		self.portfolio.buyMutualFund(3, self.BRT)
		self.portfolio.sellMutualFund(1.5, self.BRT)
		self.assertEqual({"BRT" : 1.5}, self.portfolio.mutual_funds)
	
	def test_printPortfolio(self):
		self.portfolio.addCash(300.50) 
		self.portfolio.buyMutualFund(3, self.BRT)		
		self.portfolio.buyStock(5, self.HFH)
		self.assertEqual("Account holder: Dalston Ward\nAvailable Funds: $197.50 \nStocks: \n\t5  HFH\nMutual Funds: \n\t3  BRT\n", self.portfolio.__str__())

if __name__ == '__main__':
  unittest.main() 
  