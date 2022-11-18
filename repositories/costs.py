import yaml
from yaml.loader import SafeLoader
from munch import DefaultMunch


with open('/Users/juanbotero/code-practice/Finance-Analytics/repositories/database/juanfelipe.yaml') as f:
    data  = yaml.load(f, Loader=SafeLoader)
    x = DefaultMunch.fromDict(data)



def getFixedIncomes():
    fixedCosts = x
    print(fixedCosts.fixedCosts[0].value)
