

class customer(object):
    ''' Class create customer related data and operations'''

    bank_name = "SBI Karve Nagar"

    def __init__(self, name, balance='0.00'):
        self.name= name
        self.balance=balance


    def __withdraw__(self, amount):
        ''' check if operation is feasible and them deduct amount from balance'''

        if amount > self.balance:
            raise  RuntimeError ('Entered amount is greater than available balance')
        self.balance -= amount
        return  self.balance


    def __deposite__(self, amount):
        self.balance += amount
        return  self.balance

    def __set_balance__(self, balance):
        self.balance = balance


''' Test customer class'''

cust1 = customer("shankar", 20000)
print 'Balance available for',cust1.name,"from",cust1.bank_name,"is",cust1.__deposite__(1000)


cust2= customer("Abhi", 15000)
print 'Balance available for',cust2.name,"from",cust2.bank_name,"is",cust2.__deposite__(1000)


