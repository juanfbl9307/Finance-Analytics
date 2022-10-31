from .expense_income import Cost, Income


class Balance:
    income = 0
    expense = 0

    def addExpense(self, cost: Cost):
        self.expense += cost.amount
        pass

    def addIncome(self, income: Income):
        self.income += income.amount
        pass

    def getBalance(self):
        return self.expense + self.income
