class Bank_Account:
    interest_rate = 4.9
    def __init__(self, account_holder):
        self.account_holder = account_holder

    def display_interest_rate(self):
        print(f"Regular interest rate: {self.interest_rate}%")


class Senior_Citizen(Bank_Account):
    interest_rate = 5.9

    def __init__(self, account_holder, age):
        super().__init__(account_holder)
        self.age = age

    def display_interest_rate(self):
        print(f"Senior citizen interest rate: {self.interest_rate}%")

    def get_customer_details(self):
        print(f"Account Holder: {self.account_holder}, Age: {self.age}")



if __name__ == "__main__":



    senior_account = Senior_Citizen("Sham", 70)
    senior_account.display_interest_rate()


    senior_account.super_interest_rate = super(Senior_Citizen, senior_account).display_interest_rate()


    senior_account.get_customer_details()
