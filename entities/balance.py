from .expense_income import Cost, Income
from .assets import Asset



class Balance:
    __incomes = []
    __expenses = []
    __assets = []

    def addIncome(self,income: Income):
        self.__incomes.append(income)
        pass

    def addExpense(self,cost: Cost):
        self.__expenses.append(cost)
        pass

    def addAsset(self,asset: Asset):
        self.__expenses.append(asset)
        pass

    def getIncomes(self):
        return self.__incomes

    def getExpenses(self):
        return self.__expenses

    def getAssets(self):
        return self.__assets

    def getTotalCostAmount(self):
        totalCost = 0
        for expense in self.__expenses:
            totalCost += expense.getTotalCost()

        return totalCost

    def getTotalIncomeAmount(self):
        totalIncome = 0
        for income in self.__incomes:
            totalIncome += income.getTotalIncome()

        return totalIncome

    def getBalance(self):
        totalBalance = 0
        for expense in self.__expenses:
            totalBalance -= expense.getTotalCost()
        
        for income in self.__incomes:
            totalBalance += income.getTotalIncome()

        return totalBalance