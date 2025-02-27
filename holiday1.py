# dict1 = {
#     "timo":456,
#     "john":456,
#     "fire":789,
#     "lule":900
# }
# item1 = keys,values in values.dict1.items()
# print(item1)

# subject = ["Math","English","Science","SST"]
# subject_marks = {subject:[] for subject in subject}
# for key, values in values ["marks"]. item():

# for value in dict1.values():
    
class Bank_Account:
    def __init__(self,account_no,name,balance):
        self.account_no = account_no
        self.name = name
        self.balance = balance
    
    def withdraw (self,amount):
        if amount > self.balance:
            return ("----insuffincient------")
        else:
            self.balance-=amount
            return f"Withdraw successfull your new balance is :{self.balance}"
    def depost(self,amount,account_no):
        self.balance += amount
        return f" The new accout balance is:{self.balance}"

    def check_balance(self):
        return f"Account balance :{self.balance}"
    
class Saving_account(Bank_Account):
    def __init__(self,account_no,name,balance):
        super().__init__(account_no,name,balance)
    
    def add_intrest(self):
        if self.balance < 10000:
            intrest = self.balance*0.02
        elif 10000<= self.balance <=100000:
            intrest = self.balance*0.5
        else:
            intrest = self.balance*0.6
        self.balance += intrest
        return f"Intrest added! New balance:{self.balance}"



bank_account = Saving_account("2333","timoty",1000)
print(bank_account.add_intrest())

        
