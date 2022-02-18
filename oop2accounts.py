 
import datetime
import pytz


class Accounts:

    @staticmethod
    def _current_time():
        utc_time=datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self,name,balance):
        self._name=name
        self.__balance=balance
        self._transactionsLst=[(Accounts._current_time(),balance)]
        print("account created for {}".format(self._name))

    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            self._transactionsLst.append((Accounts._current_time(),amount))
            self.showBalance()

    def withdraw(self,amount):
        if 0<amount<=self.__balance:
            self.__balance-=amount
            self._transactionsLst.append((Accounts._current_time(),-amount))
        else:
            print("anount must be greater than zero and less than {}".format(self.__balance))
        
        self.showBalance()


    def showBalance(self):
        print("balance of {} is {}".format(self._name,self.__balance))
    
    def showTransactions(self):
        for date, amount in self._transactionsLst:
            if amount>0:
                trans_Type="deposited"
            else:
                trans_Type="Withdrawn"
                amount *= -1
            #print("{:6} {} on {} (local time was {})".format(amount, trans_Type, date, date.astimezone()))
            print("{} {} on {} (local time was {})".format(amount, trans_Type, date, date.astimezone()))

if __name__== "__main__":
    Gus=Accounts("costas",0)
    Gus.showBalance()
    Gus.deposit(1000)
    Gus.showBalance()
    Gus.withdraw(500)
    Gus.showBalance()
    Gus.showTransactions()
    
    steph=Accounts("Steph",800)
    steph.__balance=200
    steph.deposit(100)
    steph._Accounts__balance=100
    steph.showBalance()
    #steph.withdraw(200)
    steph.showTransactions()
    #print(steph.__dict__)
