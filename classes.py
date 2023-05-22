
 
class Account:
    def __init__(self, account_number, account_name, balance):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance
        self.deposits = []
        self.withdrawals = []
        self.loan_balance = 0

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        self.deposits.append({"amount": amount, "narration": "deposit"})

    def withdrawal(self, amount):
        if self.balance < amount:
            return "Insufficient funds"
        else:
            self.balance -= amount
            self.withdrawals.append({"amount": amount, "narration": "withdrawal"})

    def print_statement(self):
        for transaction in self.deposits + self.withdrawals:
            narration = transaction["narration"]
            amount = transaction["amount"]
            print(f"{narration} - {amount}")

    def borrow_loan(self, amount):
        if self.loan_balance > 0:
            return "You have an outstanding loan"
        elif amount < 100:
            return "Loan amount must be at least 100"
        elif len(self.deposits) < 10:
            return "You must have at least 10 deposits to borrow"
        else:
            total_deposits = sum(transaction["amount"] for transaction in self.deposits)
            if amount > total_deposits / 3:
                return "Amount requested is more than 1/3 of your total deposits"
            else:
                self.loan_balance += amount
                self.balance += amount

    def repay_loan(self, amount):
        if amount < 0:
            return "Invalid amount"
        elif amount > self.loan_balance:
            self.balance += (amount - self.loan_balance)
            self.loan_balance = 0
        else:
            self.loan_balance -= amount

    def transfer(self, amount, account):
        if amount > self.balance:
            return "Insufficient funds"
        else:
            self.balance -= amount
            account.deposit(amount)