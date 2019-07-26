def main():

    class Account:

        def __init__(self, filepath):
            self.filepath=filepath
            with open(filepath,'r') as file:
                self.balance=int(file.read())

        def withdraw(self, amount):
            self.balance=self.balance - amount

        def deposit(self, amount):
            self.balance=self.balance + amount

        def commit(self):
            with open(self.filepath,'w') as file:
                file.write(str(self.balance))
                
    path="balance.txt"

    print("\nWelcome to IDFC Bank\nPlease select your task:\n1. Check current balance\n2. Deposit or Withdraw")
    x=input()
    if int(x)==1:
        account=Account(path)
        print("Your current balance is "+str(account.balance))
        account.commit()
        r=input("\nDo you want to perform another task?\tY or N : ")
        if r=="Y":
            main()
        else:
            exit()


    elif int(x)==2:
        print("\nPlease select your task:\n1. Withdraw\n2. Deposit")
        y=input()
        if int(y)==1:
            w=input("\nEnter the value of money to be withdraw:")
            account=Account(path)
            account.withdraw(int(w))
            print("Your current balance is "+str(account.balance))
            account.commit()
            r=input("\nDo you want to perform another task?\tY or N : ")
            if r=="Y":
                main()
            else:   
                exit()

        elif int(y)==2:
            d=input("\nEnter the value of money to be deposited:")
            account=Account(path)
            account.deposit(int(d))
            print("Your current balance is "+str(account.balance))
            account.commit()
            r=input("\nDo you want to perform another task?\tY or N : ")
            if r=="Y":
                main()
            else:
                exit()

        else:
            print("\nInvalid Input. Please try again ") 
    else:
        print("\nInvalid Input. Please try again ")

main()

