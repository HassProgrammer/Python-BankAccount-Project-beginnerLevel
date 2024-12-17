from bank_account import *
ahshan = BankAccount(1000, "Ahshan")
sadman = BankAccount(2000, "Sadman")

ahshan.getBalance()
sadman.getBalance()

sadman.deposit(500)

ahshan.withdraw(2000)

sadman.transfer(2000000, ahshan)
sadman.transfer(200, ahshan)

Jim = InterestRewardsAcct(1000, "Jim")
Jim.getBalance()
Jim.deposit(100)
Jim.transfer(100, ahshan)

Rock = SavingAcct(1000, "Rock")

Rock.getBalance()
Rock.deposit(20)
Rock.transfer(1000000, Jim)
Rock.transfer(10, Jim)