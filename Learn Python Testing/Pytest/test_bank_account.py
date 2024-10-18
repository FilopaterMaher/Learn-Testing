from bank_account import BankAccount
import pytest

@pytest.fixture
def bank_account():
    balance = 100
    account = BankAccount(balance)
    return account

def test_initial_balance(bank_account):
    """Is the initial balance work correctly?"""
    assert bank_account.balance == 100
    
def test_deposit(bank_account):
    bank_account.deposit(50)
    assert bank_account.balance == 150

def test_withdraw(bank_account):
    bank_account.withdraw(30)
    assert bank_account.balance == 70

def test_deposit_transaction(bank_account):
    bank_account.deposit(50)
    assert "Deposited 50" in bank_account.transactions
    

def test_withdraw_transaction(bank_account):
    bank_account.withdraw(30)
    assert "Withdraw 30" in bank_account.transactions