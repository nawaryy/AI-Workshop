class BankManagementSystem: 
    #constructor
    def __init__(self):
        self.acc_no = None
        self.holder_name = None
        self.__balance = None #private 

    def add_user(self,acc_no=None,holder_name=None,amount=None):
        # breakpoint() --> you can use this as a debug technique through the terminal
        if acc_no is not None:
            self.acc_no=acc_no
        if holder_name is not None:
            self.holder_name=holder_name
        if amount is not None:
            self.__balance=amount
        if self.acc_no and self.holder_name and self.__balance: 
            print(f"The account for {self.holder_name} has been created sucessfully!\n")
        else:
            print("Please provide all the credentials to join!\n")
    
    def creditAmount(self, acc_no=None, amount=None):
        if acc_no==self.acc_no:
            #credit the amount
            self.__balance+=amount
            print(f"The {amount} has been added sucessfully!\n")
        else:
            print("Please provide the vailed account\n")

    def checkBalance(self, acc_no = None):
        if acc_no==self.acc_no:
            if self.__balance: #the return item is not false> means it's not empty
                print(f"The balance for this account ({self.acc_no}) is {self.__balance} QR\n")
            else:
                print("Your balance is 0 QR\n")    
        else:
            print("Please provide the vailed account\n")

    def withdrawBalance(self,acc_no=None, amount=None):
        if acc_no==self.acc_no:
            if self.__balance>= amount:
                self.__balance-=amount
                print(f"{amount} QR has been withdrawn from you account\n")
            else:
                print("You don't have enough balance\n")
        else:
             print("Please provide the vailed account\n")

    def updateHolderName(self,acc_no=None,NewHolder_name=None):
        if acc_no==self.acc_no:
            self.holder_name=NewHolder_name
            print("Your name has been updated sucessfully!")
        else:
            print("Please provide a vailed account number!")




#user 1
c1=BankManagementSystem()
c1.add_user("QNB01","Ahmed", 1000)
c1.creditAmount("QNB01", 500)
c1.checkBalance("QNB01")
c1.withdrawBalance("QNB01",500)
c1.checkBalance("QNB01")

#user 2
c2=BankManagementSystem()
c2.add_user("QNB02","Naser", 5000)
c2.withdrawBalance("QNB02",2000)
c2.checkBalance("QNB02")
c2.updateHolderName("QNB02", "Khalil")
print(c2.holder_name)

