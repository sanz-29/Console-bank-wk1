from dataclasses import dataclass
class AccountNotFoundError(Exception):
    pass
class InsufficientFundsError(Exception):
    pass
class Account:
    id:int
    coustmer:str
    bal:float
accounts={}
NextId=1


def CreateAccount():
    global NextId
    name=input("Enter your name: ")
    account=Account()