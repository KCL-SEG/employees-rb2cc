from abc import ABC, abstractmethod
"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""


class Employee():
    def __init__(self, name, Contract, Commission):
        self.name = name
        self.Contract = Contract
        self.Commission = Commission

    def get_pay(self):
        totalPay = 0
        totalPay = self.Contract.getPay()

        if self.Commission:
            totalPay += self.Commission.getCommission()
        return totalPay

    def __str__(self):
        return f'{self.name} works on a {self.Contract}{self.Commission if self.Commission else "."} Their total pay is {self.get_pay()}.'


class Contract(ABC):
    @abstractmethod
    def getPay(self):
        pass


class HourlyContract(Contract):
    def __init__(self, hourlyPay, hours):
        self.hourlyPay = hourlyPay
        self.hours = hours

    def getPay(self):
        pay = self.hourlyPay * self.hours
        return pay

    def __str__(self):
        return f'contract of {self.hours} hours at {self.hourlyPay}/hour'


class MonthlyContract(Contract):
    def __init__(self, salary):
        self.salary = salary

    def getPay(self):
        return (self.salary)

    def __str__(self):
        return f'monthly salary of {self.getPay()}'


class Commission(ABC):
    def getCommission(self):
        pass


class BonusCommission(Commission):
    def __init__(self, amount):
        self.amount = amount

    def getCommission(self):
        return self.amount

    def __str__(self):
        return f' and receives a bonus commission of {self.getCommission()}.'


class ContractCommission(Commission):
    def __init__(self, rate, noOfContracts):
        self.rate = rate
        self.noOfContracts = noOfContracts

    def getCommission(self):
        totalCommission = self.rate * self.noOfContracts
        return totalCommission

    def __str__(self):
        return f' and receives a commission for {self.noOfContracts} contract(s) at {self.rate}/contract.'


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', MonthlyContract(4000), None)
print(str(billie))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', HourlyContract(25, 100), None)
print(str(charlie))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', MonthlyContract(3000), ContractCommission(200, 4))
print(str(renee))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', HourlyContract(25, 150), ContractCommission(220, 3))
print(str(jan))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', MonthlyContract(2000), BonusCommission(1500))
print(str(robbie))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', HourlyContract(30, 120), BonusCommission(600))
print(str(ariel))
