from .expense_income import Income,FixedCost,Cost,FixedIncome,formatDate
import datetime


class Balance:
    __incomes = []
    __costs = []
    __fixedIncomes = []
    __fixedCosts = []

    def addIncome(self,income: FixedIncome):
        self.__incomes.append(income)
        pass
    
    def addFixedIncome(self,income: Income):
        self.__fixedIncomes.append(income)
        pass

    def addFixedCost(self,cost: FixedCost):
        self.__fixedCosts.append(cost)
        pass
    
    def addCost(self,cost: Cost):
        self.__costs.append(cost)
        pass

    def getMonthBalance(self,month: int):
        totalBalance = 0
        for fixedCost in self.__fixedCosts:
            if formatDate(fixedCost.getInitialDate()).month <= month <= formatDate(fixedCost.getEndDate()).month:
                totalBalance -= fixedCost.getAmount()

        for fixedIncome in self.__fixedIncomes:
            if formatDate(fixedIncome.getInitialDate()).month <= month <= formatDate(fixedIncome.getEndDate()).month:
                totalBalance += fixedIncome.getAmount()

        for income in self.__incomes:
            if formatDate(income.getDate()).month == month:
                totalBalance += income.getAmount()

        for cost in self.__costs:
            if formatDate(cost.getDate()).month == month:
                totalBalance -= income.getAmount()

        return totalBalance