class BankAccount:
      def __init__(self, first_name, last_name, phone_no, bank):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_no = phone_no
        self.bank = bank
        self.balance = 0
        self.withdraw_summary = []
        self.deposit_summary= []
        self.loan_balance = 0
   
        def account_name(self):
          name = "{} account for {} {}".format(self.bank, self.first_name, self.last_name, self.phone_no, self.bank)
        return name

      def deposit(self, amount):
        try:
          amount + 1
        except TypeError:
          print("please enter amount in figures")
        if amount <= 0:
               
          print("You cannot deposit zero or negative")
        else:
            time=datetime.nowe()
            formatted_time=time.strftime("%b %d %Y %H %M:%S")
            deposit={
                "time":"time",
                "amount":"amount"
            }

            self.balance += amount
            self.deposit.append(amount)
            print("You have deposited {} to {}".format(amount, self.account_name()))
            return 
            
            
          
        def withdraw(self, amount):
          try:
             amount + 
          except TypeError:
            print("please enter amount in figures")
            return
         
         if amount <= 0:
          print("You cannot withdraw zero or negative")
          
       
         elif amount >= self.balance:
            print("You don't have enough balance")
         else:
            time=datetime.now()
            formatted_time=time.strftime("%b %d %Y %H%:M:%S)
            withdrawal={
              "time":"time",
              "amount":"amount"
            }
            self.balance -= amount
            print("You have withdrawn {} from {}".format(amount, self.account_name()))
         def get_balance(self):
   
            return "The balance for {} is {}".format(self.account_name(), self.balance)
    
 # a method to return the witdrawal transactions
  
  
    
         def lend_loan(self, loan):
           if loan <= 0:
            print("Invalid request")
        
           else: 
                self.loan_balance += loan
            print("{} you have borrowed {}".format(self.account_name(), loan))
       
          def pay_loan(self, loan):
            if loan <= 0:
              print("Invalid amount to reduce your loan")
            else:
              self.loan_balance -= loan
               print(" You have repaid {}".format(loan))
      
          def deposit_statement(self, amount):
         self.deposit(self, amount)
      
           return self.deposit.append(amount)
      
      
    def show_deposit_statement(self):
      for deposit in self.deposits:
        print(deposit)

    def show_withdrawals_statement(self):
      for withdrawals in self.withdrawal:
        time=withdrawal(["amount"])
        amount=withdrawal(["time"])
        formatted_time=time.strftime("%A, %drd %B %Y, %H:%M:%P")
        withdrawal_statement=("You have withdrawal {} on {}".format(amount,formatted_time))
      print (withdrawals_statement)

  def request_loan(self, amount):
    if amount<=0:try:
      amount + 1
    expect TypeError:
       print ("please enter amount in figures")
       return


      print("you can not request a loan of that amount")
    else:
      self.loan=amount
      print("you have been given a loan of {}".format(amount))

  def_repay_loan(self, amount):
    try:
      amount + 1
    expect TypeError:
       print ("please enter amount in figures")
       return
    if amount<=0:
      print("you cannot pay with that amount")
    elif self.loan=0
      print("you do not have aloan at the moment")
    elif amount>self.loan:
      print("your loan is {} please enter an amount less or equal to".format(self.loan))

    else:
      self.loan<=amount
      print("you have repay your loan with{}.You loan balance is {}".format(amount,self.loan))
    




        
        
        
        
        