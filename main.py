from entities.expense_income import *
from entities.transactions import *
from entities.balance import *
from entities.analytics import *
balance = Balance()

def floatToMoney(number:int):
    return '${:,.2f}'.format(number)



balance.addFixedCost(FixedCost(120000, "Pago gimnasio ohana","2022/07/01","2022/12/01"))
balance.addFixedCost(FixedCost(700000,"Pago arriendo Eliseos","2022/07/01","2022/12/01"))
balance.addFixedCost(FixedCost(125000,"Salud mama","2022/07/01","2022/12/01"))
balance.addFixedCost(FixedCost(1130000,"Deuda de 10 millones a mi hermano","2022/07/01","2022/12/01"))
balance.addFixedCost(FixedCost(167000,"Plan internet movistar","2022/07/01","2022/12/01"))
balance.addFixedCost(FixedCost(32000,"Plan celular movistar","2022/01/07","2022/12/01"))
balance.addFixedCost(FixedCost(1752000,"Pago cuota del carro a Sufi","2022/08/01","2022/12/01"))
balance.addCost(Cost(320000,"Pago soat carro","2022/08/15"))
balance.addCost(Cost(3980771,"Deuda tarjeta credito","2022/10/30"))

balance.addFixedIncome(FixedIncome(5500000,"Pago nomina Seeri","2022/07/01","2022/12/01"))
balance.addIncome(Income(1000000,"Anticipo 40% asesoria pulumi","2022/10/28"))
balance.addIncome(Income(3857779,"Saldo tarjeta debito","2022/10/30"))


print(balance.getMonthBalance(12))
