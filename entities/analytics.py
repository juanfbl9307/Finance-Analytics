from .balance import Balance
from .expense_income import Cost,Income

class Analyzer:
    def __init__(self,balance: Balance):
        self.__balance = balance

    def monthlyRemain(self,months: list):
        balance = 0
        expenses: list(Cost) = self.__balance.getExpenses()
        incomes: list(Income) = self.__balance.getIncomes()

        for expense in expenses:
            for month in months:
                balance -= expense.getMonthCost(month)

        for income in incomes:
            for month in months:
                balance += income.getMonthIncome(month)
        
        
        return {
            "total": balance,
            "perMonth": (balance/len(months))
        }
            


