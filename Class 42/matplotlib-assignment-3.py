import matplotlib.pyplot as plt
import pandas as pd

# Load the data
df = pd.read_csv("sales_data.csv")

print(df.head())

# The data shows that North had the lowest sales and South had the highest sales.

# Extract data
regions = df["Region"]
sales = df["Sales"]

# Create a pie chart
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']  # Custom colors

# Dynamic Explosion of biggest slice
explode = []
max_val = df['Sales'].max()
for val in df['Sales']:
    if val == max_val: explode.append(0.1)
    else: explode.append(0)

plt.figure(figsize=(8, 8))
plt.pie(sales, labels=regions, autopct='%1.1f%%', startangle=90, colors=colors, explode=explode, shadow=True)
plt.title("Enhanced Sales Distribution by Region")
plt.savefig("customized_sales_pie_chart.png")
plt.show()

# This chart shows by percent the sales distribution of each region.
# The South region had the highest sales with 28.6%
# The North region had the lowest sales with 21.4%.