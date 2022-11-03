import datetime

def formatDate(strDate:str):
        ## year/month/day format
        return datetime.datetime.strptime(strDate, '%Y/%m/%d')


class Cash:
    def __init__(self, amount: float, description: str):
        self.__amount = amount
        self.__description = description

    def getAmount(self):
        return self.__amount
    
    def getDescription(self):
        return self.__description

class __FixedCash(Cash):
    def __init__(self, amount: float, description: str, initialDate: str,endDate: str):
        self.__endDate = endDate
        self.__initialDate = initialDate
        super().__init__(amount,description)

    
    def getEndDate(self):
        return self.__endDate

    def getMonthCost(self,month: int):
        month = datetime.date(1900, month, 1).strftime('%B')
        amount = 0
        if self.formatDate(self.__initialDate) <= month <= self.formatDate(self.__endDate):
            amount += self.getAmount()
            
        return amount

    def getInitialDate(self):
        return self.__initialDate

    def getDurationInDays(self):
        diff = self.formatDate(self.__initialDate) - self.formatDate(self.__endDate)
        return diff.date

    def getDurationInMonths(self):
        diff = self.formatDate(self.__initialDate) - self.formatDate(self.__endDate)
        return diff.months
    
    def getTotalAmount(self):
        diff = self.formatDate(self.__initialDate) - self.formatDate(self.__endDate)
        return (diff.months * self.getAmount())
         
    

class Cost(Cash):
    def __init__(self, amount: float, description: str, date: str):
        self.__date = date
        super().__init__(amount, description)
    
    def getDate(self):
        return self.__date


class FixedCost(__FixedCash):
    def __init__(self, amount: float, description: str, initialDate: str,endDate: str):
        super().__init__(amount, description,initialDate,endDate)


class Income(Cash):
    def __init__(self, amount: float, description: str, date: str):
        self.__date = date
        super().__init__(amount, description)
    
    def getDate(self):
        return self.__date

class FixedIncome(__FixedCash):
    def __init__(self, amount: float, description: str, initialDate: str,endDate:str ):
        super().__init__(amount, description,initialDate,endDate)



