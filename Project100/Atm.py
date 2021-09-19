class Atm():
    
    def __init__(self,cashWithdrawl,balanceEnquiry,):
        self.cashWithdrawl=cashWithdrawl
        self.balanceEnquiry=balanceEnquiry
        

    def start(self):
        print("started")

    def stop(self):
        print("stopped")


Bank=Atm("$1000","-500")

print(Bank.balanceEnquiry)
print(Bank.cashWithdrawl)
