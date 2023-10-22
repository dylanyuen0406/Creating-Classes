class BankAccount:
    def __init__(self, accNumber, name, registration, balance):
        self.accNumber = accNumber
        self.name = name
        self.registration = registration
        self.balance = balance

    def checkBalance(self):
        print(self.balance)

    def withdraw(self, money):
        self.balance -= money
        print("You have withdrawn $" + str(money))
        print("Balance left: $" + str(self.balance))

    def deposit(self, money):
        self.balance += money
        print("You have deposited $" + str(money))
        print("Balance: $" + str(self.balance))


    def transfer(self, payee, amount):
        self.balance -= amount
        payee.balance += amount
        print("$" + str(amount) + "has been transferred from " + self.name + "to " + payee.name)


var1 = BankAccount("1234", "me", "12345678", 100000000)
var2 = BankAccount("9999", "you", "69696969", 1)
var1.transfer(var2, 10000)
var1.checkBalance()
var2.checkBalance()






