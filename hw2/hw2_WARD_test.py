import unittest 

from portfolio import Portfolio

class PortfolioTest(unittest.TestCase):
	#create a portfolio to use in the tests
	def setUp(self):
		self.portfolio = Portfolio("Dalston Ward")
#		self.HFH = Stock(20, "HFH")
# 		self.DHW = Stock(15, "DHW")
# 		self.BRT = MutualFund("BRT")
# 		self.GHT = MutualFund("GHT")

	#test to add cash to the portfolio and make sure it prints the right amount.  
	def addCashTest(self):
		self.portfolio.addCash(300.50)
		self.assertEqual(300.50, self.portfolio.funds)
	
# 	#test to make sure that the stock created has the right name and price. 
# 	def createStockTest(self):
# 		self.assertEqual(20, self.HFH.price)
# 		self.assertEqual("HFH", self.HFH.tickSym)
# 	
# 	#Test buying a stock and making sure that funds are removed from the account.  
# 	def buyStockTest(self):
# 		self.portfolio.buyStock(5, self.HFH)
# 		self.assertEqual({"HFH" : 5}, self.portfolio.stocks)
# 		self.assertEqual(200.50, self.portfolio.funds)
# 	
# 	def buyTwoStocks(self):
# 		self.portfolio.buyStock(5, self.HFH)
# 		self.
# 			
# 	def createMutualFundTest(self):
# 		self.assertEqual("BRT", self.BRT.tickSym)
# 		self.assertEqual("GHT", self.GHT.tickSym)

if __name__ == '__main__':
  unittest.main() 
  