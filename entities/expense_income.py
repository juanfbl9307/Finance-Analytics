from array import array


class Cash:
    description = ""

    def __init__(self, amount: float, description: str):
        self.description = description
        self.__amount = amount

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, amount):
        self.__amount = amount


class Cost(Cash):
    def __init__(self, amount: float, description: str):
        super().__init__(amount, description)
        self.amount = amount * (-1)


class FixedCost(Cost):
    def __init__(self, amount: float, description: str, months: list):
        super().__init__(amount, description)
        self.__months = months

    def getTotalCost(self):
        return (self.amount * len(self.__months))


class VariableCost(Cost):
    def __init__(self, amount: float, description: str, month: str):
        super().__init__(amount, description)
        self.month = month


class Income(Cash):
    def __init__(self, amount: float, description: str):
        super().__init__(amount, description)


class FixedIncome(Income):
    def __init__(self, amount: float, description: str, months: list):
        super().__init__(amount, description)
        self.months = months

    def getTotalIncome(self):
        return (self.amount * len(self.months))


class VariableIncome(Income):
    def __init__(self, amount: float, description: str, month: str):
        super().__init__(amount, description)
        self.month = month
