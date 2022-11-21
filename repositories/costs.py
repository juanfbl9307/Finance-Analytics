import yaml
from yaml.loader import SafeLoader
from munch import DefaultMunch
import os, sys


def getFixedIncomes():
    with open(os.getcwd() + '/repositories/database/juanfelipe.yaml') as f:
        data = yaml.load(f, Loader=SafeLoader)
    x = DefaultMunch.fromDict(data)
    fixedCosts = x
    print(fixedCosts.fixedCosts[0].value)
