import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sales_data.csv")

# Show summary
print("----- Sales Summary -----")
print(df.describe())

# Total sales by product
product_sales = df.groupby("Product")["Sales"].sum()

# Line chart - Sales trend
plt.figure(figsize=(8,5))
plt.plot(df["Date"], df["Sales"], marker="o")
plt.title("Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Sales ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Bar chart - Total sales by product
product_sales.plot(kind="bar", title="Total Sales by Product", ylabel="Sales ($)")
plt.tight_layout()
plt.show()

# Pie chart - Sales distribution
product_sales.plot(kind="pie", autopct="%1.1f%%", title="Sales Distribution")
plt.ylabel("")
plt.show()