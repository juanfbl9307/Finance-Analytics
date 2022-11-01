class _Transaction:
    def __init__(self, desc: str, date, amount: float):
        self.__desc = desc
        self.__date = date
        self.__amount = amount

    def getDesc(self):
        return self.__desc

    def getDate(self):
        return self.__date


class CreditTransaction(_Transaction):
    def __init__(self, desc, data, amount, interestRate, dues):
        super().__init__(desc, data, amount)
        self.__interestRate = interestRate
        self.__dues = dues

    @property
    def getDues(self):
        return self.__dues

    @property
    def getInterestRate(self):
        return self.__interestRate

    @property
    def setInterestRate(self, interestRate):
        self.__interestRate = interestRate

    @property
    def setDues(self, dues):
        self.__dues = dues


class DebitTransaction(_Transaction):
    def __init__(self, desc, data, amount):
        super().__init__(desc, data, amount)
