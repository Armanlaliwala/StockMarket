class StockMarketApp:
    def __init__(self):
        self.balance = 1000  # Initial balance
        self.stocks = {}  # Dictionary to store stock name and quantity

    def add_amount(self, amount):
        self.balance += amount
        print(f"\nAmount added successfully! New balance: ${self.balance}")

    def withdraw_amount(self, amount):
        if amount > self.balance:
            print("\nInsufficient balance to withdraw.")
        else:
            self.balance -= amount
            print(f"\nAmount withdrawn successfully! Remaining balance: ${self.balance}")

    def buy_stock(self, stock_name, stock_price, quantity):
        total_cost = stock_price * quantity
        if total_cost > self.balance:
            print("\nInsufficient balance to buy the stocks.")
        else:
            self.balance -= total_cost
            self.stocks[stock_name] = self.stocks.get(stock_name, 0) + quantity
            print(f"\nYou successfully bought {quantity} shares of {stock_name}. Remaining balance: ${self.balance}")

    def sell_stock(self, stock_name, stock_price, quantity):
        if stock_name not in self.stocks or self.stocks[stock_name] < quantity:
            print("\nYou do not have enough shares to sell.")
        else:
            self.stocks[stock_name] -= quantity
            self.balance += stock_price * quantity
            if self.stocks[stock_name] == 0:
                del self.stocks[stock_name]
            print(f"\nYou successfully sold {quantity} shares of {stock_name}. New balance: ${self.balance}")

    def view_details(self):
        print("\n--- Account Details ---")
        print(f"Balance: ${self.balance}")
        if self.stocks:
            print("Stocks owned:")
            for stock, quantity in self.stocks.items():
                print(f"  - {stock}: {quantity} shares")
        else:
            print("No stocks owned.")

# Main App
app = StockMarketApp()

while True:
    print("\n--- Stock Market App ---")
    print("1. View Account Details")
    print("2. Add Amount")
    print("3. Withdraw Amount")
    print("4. Buy Stock")
    print("5. Sell Stock")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        app.view_details()
    elif choice == "2":
        amount = float(input("Enter amount to add: "))
        app.add_amount(amount)
    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        app.withdraw_amount(amount)
    elif choice == "4":
        stock_name = input("Enter stock name: ")
        stock_price = float(input("Enter stock price: "))
        quantity = int(input("Enter quantity to buy: "))
        app.buy_stock(stock_name, stock_price, quantity)
    elif choice == "5":
        stock_name = input("Enter stock name: ")
        stock_price = float(input("Enter stock price: "))
        quantity = int(input("Enter quantity to sell: "))
        app.sell_stock(stock_name, stock_price, quantity)
    elif choice == "6":
        print("\nThank you for using the Stock Market App. Goodbye!")
        break
    else:
        print("\nInvalid choice. Please try again.")
