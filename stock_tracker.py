
# Hardcoded stock prices
stock_prices = {
    "tcs": 3600,
    "infosys": 1500,
    "reliance": 2800,
    "hdfc": 1700,
    "wipro": 430
}

# Dictionary to store your portfolio
portfolio = {}


while True:
    stock = input("Enter stock name (or type 'done' to finish): ").lower()

    if stock == "done":
        break

    if stock not in stock_prices:
        print("❌ Stock not found! Try one of:", ", ".join(stock_prices.keys()))
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        if quantity <= 0:
            print("❗ Quantity must be greater than 0.")
            continue
    except ValueError:
        print("⚠️ Please enter a valid number.")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + quantity

# Calculate total investment
total_investment = 0
print("\n📊 Your Stock Portfolio:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_investment += value
    print(f"- {stock.title()}: {qty} × ₹{price} = ₹{value}")

print(f"\n💰 Total Investment: ₹{total_investment}")

# Save to file
save = input("Do you want to save this summary to 'portfolio.txt'? (yes/no): ").lower()
if save == "yes":
    try:
        file_path = r"C:\Users\Ekata\Documents\task\portfolio.txt"
        with open(file_path, "w", encoding="utf-8") as file:  
            file.write("📊 Your Stock Portfolio:\n")
            for stock, qty in portfolio.items():
                price = stock_prices[stock]
                value = qty * price
                file.write(f"- {stock.title()}: {qty} × ₹{price} = ₹{value}\n")
            file.write(f"\n💰 Total Investment: ₹{total_investment}\n")
        print(f"✅ Portfolio saved successfully at:\n{file_path}")
    except Exception as e:
        print("⚠️ Error saving file:", e)
else:
    print("📄 Save skipped.")


