import pandas as pd
import re

def printExcel():
    df = pd.read_excel(r'repositories/bank_informs/extracto_202209_cuenta_de_ahorros_5147.xlsx')
    df.rename(columns = {'Unnamed: 0':'date',"Unnamed: 1": "description","Unnamed: 2":"branch_office","Unnamed: 4":"value"},inplace= True)
    df = df[df['date'].notna()]
    result = df[df['date'].str.match('[0-9]{2}/[0-9]{2}')]
    result.dropna(how='all', axis=1, inplace=True)
    result.replace(float("NaN"), "", inplace=True)
    result.to_excel(r'repositories/bank_informs/new.xlsx')
    print(result)

