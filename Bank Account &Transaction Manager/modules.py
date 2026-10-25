
class account :
    def __init__(self,owner:str, balance :float=0.0):
         """ class rep for main bank account"""
         self.owner=owner
         self._balance = 0.0
         self.balance = balance
         self.transactions = []

    @property
    def balance(self) -> float:
        return self._balance

    @balance.setter
    def balance(self, value: float):
        if value<0:
            raise ValueError("balance cannot be negative")
        self._balance = float(value)

    
    def deposit (self , amount:float):
        if amount<=0:
            raise ValueError(" depoist connat exxept negative value")
        self.balance+=amount
        print(f"sucess depoist a{amount:.2f}")

    def withdraw(self, amount:float):
        if amount<=0:
            raise ValueError("it should be greater than zero")
        if amount>self.balance:
            raise ValueError("balance is not enough to make this process")
        self.balance -= amount
        print (f"{amount:.2f} was withrdraw")

    def __str__(self):
        return f"owner :{self.owner} | balance : {self.balance:.2f} dollar"
    def __repr__(self):
        return f"Account(owner='{self.owner}', balance={self._balance})"
    def __add__(self, other):
        if isinstance(other, account):
            marged = f"{self.owner} + {other.owner}"
            return account(owner= marged, balance=self.balance + other.balance)
        raise TypeError ("process takes two vaild accounts")
    def to_dict(self) -> dict:
        return {
            "owner": self.owner,
            "balance": self.balance,
            "type": "Standard",
            "transactions": self.transactions
        }
class SavingsAccount(account): 
    def __init__(self, owner: str, balance: float = 0.0, interest_rate: float = 0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest) 
        print (f"{interest:.2f} was added")
        
    def to_dict(self) -> dict:
        data = super().to_dict()
        data["type"] = "Savings"
        data["interest_rate"] = self.interest_rate
        return data
# acc1=account("eilomilo", 1000)
# acc2=account("alaa", 1000)
# acc_tot =acc1 + acc2
# print (acc_tot)

