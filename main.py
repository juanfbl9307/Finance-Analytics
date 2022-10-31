from entities.expense_income import *
from entities.transactions import *
from entities.balance import *

cost1 = VariableCost(200, "new", "ene")
cost2 = FixedCost(200, "new", ["ene", "feb"])
income1 = FixedIncome(400, "income", ["ene", "feb"])

balance = Balance()
balance.addExpense(cost1)
balance.addExpense(cost2)
balance.addIncome(income1)

print(balance.getBalance())
