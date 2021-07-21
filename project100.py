class atm(object):
    def __init__(self,cashwithdrawl,balance, ):
        self.cashwithdrawl = cashwithdrawl
        self.balance = balance

    def theatmisworking(self):
        print("The Atm Is Working")
    
    def theatmisnotworking(self):
        print("The Atm Is Not Working")

bankaccount1 = atm(5000, 85000)
print(bankaccount1.balance)
bankaccount1.theatmisworking()