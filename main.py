from entities.expense_income import *
from entities.transactions import *
from entities.balance import *
from entities.analytics import *
balance = Balance()

def floatToMoney(number:int):
    return '${:,.2f}'.format(number)



balance.addExpense(FixedCost(120000, "Pago gimnasio ohana", ["agosto", "septiembre","noviembre","diciembre"]))
balance.addExpense(FixedCost(700000,"Pago arriendo Eliseos",["julio","agosto","septiembre","octubre","noviembre","diciembre"]))
balance.addExpense(FixedCost(125000,"Salud mama",["julio","agosto","octubre","noviembre","diciembre"]))
balance.addExpense(FixedCost(1130000,"Deuda de 10 millones a mi hermano",["julio","agosto","septiembre","octubre","noviembre","diciembre"]))
balance.addExpense(FixedCost(167000,"Plan internet movistar",["julio","agosto","septiembre","octubre","noviembre","diciembre"]))
balance.addExpense(FixedCost(32000,"Plan celular movistar",["julio","agosto","septiembre","octubre","noviembre","diciembre"]))
balance.addExpense(FixedCost(1752000,"Pago cuota del carro a Sufi",["agosto","septiembre","octubre","noviembre","diciembre"]))
balance.addExpense(VariableCost(320000,"Pago soat carro","agosto"))
balance.addExpense(VariableCost(3980771,"Deuda tarjeta credito","octubre"))

balance.addIncome(FixedIncome(5500000,"Pago nomina Seeri",["julio","agosto","septiembre","octubre","noviembre","diciembre"]))
balance.addIncome(VariableIncome(1000000,"Anticipo 40% asesoria pulumi","octubre"))
balance.addIncome(VariableIncome(3857779,"Saldo tarjet debito","octubre"))


print('Total balance = {0}'.format(floatToMoney(balance.getBalance())))
print('Total costs = {0}'.format(floatToMoney(balance.getTotalCostAmount())))
print('Total incomes = {0}'.format(floatToMoney(balance.getTotalIncomeAmount())))

analyzer = Analyzer(balance)
print(analyzer.monthlyRemain(["noviembre","diciembre"]))

