# Learn Unit Test using pytest library 
#####################################################
# 1-Unit testing for function

# from name_function import get_formatted_name

# print("Enter 'q' any time to quit.")

# while True:
#     first = input("Please give me a first name: ")
#     if first == 'q':
#         break
#     last = input("Please give me a last name: ")
#     if last == 'q':
#         break
    
#     formatted_name = get_formatted_name(first, last)
#     print(f"\tFormatted name: {formatted_name}")

#####################################################
# 2- Unit testing for class
from bank_account import BankAccount

balance = 100
account = BankAccount(balance)

print(f"Intitial balance: {account.balance}")
print(f"Depositing 50: {account.deposit(50)}")
print(f"Withdrawing 30: {account.withdraw(30)}")