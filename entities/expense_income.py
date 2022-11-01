
class Cash:
    description: str
    def __init__(self,amount:float, description: str):
        self.description = description
        self.__amount = amount

    def getAmount(self):
        return self.__amount

    def setAmount(self,amount):
        self.__amount = amount
        pass


class Cost(Cash):
    def __init__(self, amount: float, description: str, months: list):
        super().__init__(amount, description)
        self.__periodCost = self.getAmount()
        self.__months = months
        self.__numPeriods = len(months)
        self.__totalCost = (self.__numPeriods * self.__periodCost)
    
    def getPeriodCost(self):
        return self.__periodCost

    def getMonths(self):
        return self.__months

    def getTotalCost(self):
        return self.__totalCost
    
    def getMonthCost(self,month: str):
        cost = 0
        if (month in self.__months):
            cost += self.__periodCost
        return cost


class FixedCost(Cost):
    def __init__(self, amount: float, description: str, months: list):
        super().__init__(amount, description,months)


class VariableCost(Cost):
    def __init__(self, amount: float, description: str, month: str):
        super().__init__(amount, description,[month])


class Income(Cash):
    def __init__(self, amount: float, description: str, months: list):
        super().__init__(amount, description)
        self.__periodIncome = self.getAmount()
        self.__months = months
        self.__numPeriods = len(months)
        self.__totalCost = (self.__numPeriods * self.__periodIncome)

    def getPeriodIncome(self):
        return self.__periodIncome
    
    def getMonths(self):
        return self.__months

    def getTotalIncome(self):
        return self.__totalCost
    
    def getMonthIncome(self,month: str):
        income = 0
        if (month in self.__months):
            income += self.__periodIncome
        return income

class FixedIncome(Income):
    def __init__(self, amount: float, description: str, months: list):
        super().__init__(amount, description,months)


class VariableIncome(Income):
    def __init__(self, amount: float, description: str, month: str):
        super().__init__(amount, description,[month])


