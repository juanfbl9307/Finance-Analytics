from entities.expense_income import *
from entities.transactions import *
from entities.balance import *
from entities.analytics import *
from repositories.costs import getFixedIncomes
def floatToMoney(number:int):
    return '${:,.2f}'.format(number)




getFixedIncomes()
