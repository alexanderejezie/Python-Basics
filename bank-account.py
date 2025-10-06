# bank_account.py

class Account:
    def __init__(self, account_number, account_holder, account_balance=0.0):
        """Initialize account attributes."""
        self.account_number = account_number
        self.account_holder = account_holder
        self.account_balance = account_balance

    def deposit(self, amount):
        """Add funds to the account."""
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited ${amount:.2f} successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw funds from the account if sufficient balance exists."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.account_balance:
            print("Insufficient funds for this withdrawal.")
        else:
            self.account_balance -= amount
            print(f"Withdrew ${amount:.2f} successfully.")

    def check_balance(self):
        """Return the current balance."""
        print(f"Current balance: ${self.account_balance:.2f}")
        return self.account_balance


# Example usage and testing
if __name__ == "__main__":
    # Create account instances
    my_account = Account("12345", "Alice Johnson", 500.00)
    another_account = Account("67890", "Bob Smith", 1000.00)

    # Test operations on my_account
    print("\n--- Transactions for Alice ---")
    my_account.deposit(200)
    my_account.withdraw(150)
    my_account.check_balance()

    # Test operations on another_account
    print("\n--- Transactions for Bob ---")
    another_account.deposit(500)
    another_account.withdraw(1200)  # Should show insufficient funds
    another_account.check_balance()
