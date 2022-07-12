
from mimetypes import init


class Bank :
    bankID = -1
    allBanks = set([])
    def __init__(self,bankFullName,bankAbbrivation):
        self.bankFullName = bankFullName
        self.bankAbbrivation = bankAbbrivation
        bankID+=1
        self.bankID = bankID

    @staticmethod
    def findBank(bankAbbrivation):
        for i in Bank.allBanks:
            if i.bankAbbrivation == bankAbbrivation:
                return True,i
        return False

    @staticmethod
    def createNewBank(bankName,bankAbbrivation):
        newBank = Bank(bankName,bankAbbrivation)
        if(Bank.allBanks.add(newBank)==False):
            print("Bank already exits!!")
            return False
        return True

class Account:
    accountNumber = 0
    def __init__(self,bank):
        self.accountNumber = Account.accountNumber
        self.bank = bank
        self.balance = 1000
    def isAccountExists(self,bankAbbrivation):
        return self.bank.bankAbbrivation == bankAbbrivation

    def displayAccountBalance(self):
        print("Account Balance is "+self.balance)

    def isSufficientBalace(self,amount):
        return self.balance>=amount

    def updateAccountBalance(self,amount,operation):
        if operation=="Add":
            self.balance+=amount
        else:
            self.balance-=amount
        return

    @staticmethod
    def createNewAccount(bankAbbrivation):
       isBankExits,bankObj =  Bank.findBank(bankAbbrivation)
       if not isBankExits:
         print("The given bank name doest not exits!!")
         return False
       newAccount = Account(bankObj)
       return newAccount


class Customer:
    customerID = -1
    allCustomers = []
    def __init__(self,firstName,lastName,totalBalance,userName):
        customerID+=1
        self.customerID = Customer.customerID
        self.firstName = firstName
        self.lastName = lastName
        self.totalBalance = totalBalance
        self.accounts = []
        self.userName = userName
    
    @staticmethod
    def findCustomer(self,userName):
        for customer in Customer.allCustomers:
            if customer.userName == userName:
                return True,customer
        
        return False
        


    def findAccount(self,bankAbbrivation):
        for account in self.accounts:
            if account.bank.bankAbbrivation == bankAbbrivation:
                return True,account
            return False
            
    def createNewAccount(self,bankAbbrivation):
        isAccountExists,_ = self.findAccount(bankAbbrivation)
        if isAccountExists:
           print("account already exits in this bank!! ")
           return 
        isBankExists,bankObj = Bank.findBank(bankAbbrivation)
        if isBankExists :
           return 
        newAccount = Account.createNewAccount(bankAbbrivation)
        self.accounts.append(newAccount)
        return True,newAccount

    def deposit(self,bankAbbrivation,amount):
        isBankExists,bankObj = Bank.findBank(bankAbbrivation)
        if not isBankExists:
            print("Amount cannot be deposited as the bank does not exits")
            return 
        isAccountExits,account = self.findAccount(bankAbbrivation)
        if isAccountExits:
            account.updateAccountBalance(amount,"Add")
            print("Amount has been deposited in your accout successfully")
            self.__updateTotalBalace()
            return True
        print("cannot deposit the amount as the account does not exits")
        return False

    def Withdraw(self,amount,bankAbbrivation):
        isBankExists,bankObj = Bank.findBank(bankAbbrivation)
        if not isBankExists:
            print("Amount cannot be withdraw as the bank does not exits")
            return 
        isAccountExits,account = self.findAccount(bankAbbrivation)
        if isAccountExits:
            if account.isSufficientBalace(amount):
                 account.updateAccountBalance(amount,"subtract")
                 print("Amount has been withdrawn from your account successfully!!")
                 self.__updateTotalBalace()
                 return True

            print("Insufficient account balance!")
            return 
        print("cannot withdraw the amount as the account does not exits")
        return False
    
    def transferAmount(self,creditCustomerUserName,creditCustomerBankName,debitCustomerBankName,amount):
        if Customer.findCustomer(creditCustomerUserName) and Customer.findCustomer(debitCustomerBankName):
            customerObj = Customer.findCustomer(creditCustomerBankName)
            self.Withdraw(debitCustomerBankName,amount)
            customerObj.deposit(creditCustomerUserName,amount)
            return True
        print("cannot transfer the amount")
        return False

    def selfTransfer(self,creditBankName,debitBankName,amount):
        if Bank.findBank(creditBankName) and Bank.findBank(debitBankName):
           self.Withdraw(debitBankName,amount)
           self.deposit(creditBankName,amount)
           return True
        print("cannot transfer the amount!")
        return False

    def __updateTotalBalace(self):
        self.totalBalance = 0
        for account in self.accounts:
            self.totalBalance+=account.balance
        return self.totalBalance
        

    def displayBalance(self):
        print(self.firstName+" your account balance is "+self.totalBalance)
        for account in self.accounts:
            account.displayBalance()
 

