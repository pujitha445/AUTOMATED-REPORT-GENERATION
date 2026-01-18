# ============================================
# TASK 2: ADVANCED DATA ANALYSIS & VISUALIZATION
# Sales Performance Analysis
# ============================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ============================================
# STEP 1: CREATE DATASET
# ============================================

data = {
    "Month": ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],
    "Electronics": [12000,15000,18000,17000,20000,22000,24000,23000,21000,25000,27000,30000],
    "Clothing": [8000,9000,9500,10000,11000,13000,14000,13500,12000,15000,16000,18000],
    "Grocery": [15000,16000,17000,18000,19000,20000,21000,22000,23000,24000,25000,26000]
}

df = pd.DataFrame(data)

print("📊 Sales Dataset Preview")
display(df)

# ============================================
# STEP 2: DATA ANALYSIS
# ============================================

df["Total_Sales"] = df["Electronics"] + df["Clothing"] + df["Grocery"]

print("\n📈 Monthly Total Sales:")
display(df[["Month", "Total_Sales"]])

print("\n📊 Category-wise Average Sales:")
print(df[["Electronics","Clothing","Grocery"]].mean())

# ============================================
# STEP 3: VISUALIZATION 1 – LINE CHART
# ============================================

plt.figure()
plt.plot(df["Month"], df["Electronics"], label="Electronics")
plt.plot(df["Month"], df["Clothing"], label="Clothing")
plt.plot(df["Month"], df["Grocery"], label="Grocery")
plt.title("Monthly Sales Trend by Category")
plt.xlabel("Month")
plt.ylabel("Sales Amount")
plt.legend()
plt.xticks(rotation=45)
plt.show()

# ============================================
# STEP 4: VISUALIZATION 2 – BAR CHART
# ============================================

plt.figure()
plt.bar(df["Month"], df["Total_Sales"])
plt.title("Total Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.show()

# ============================================
# STEP 5: VISUALIZATION 3 – PIE CHART
# ============================================

category_totals = [
    df["Electronics"].sum(),
    df["Clothing"].sum(),
    df["Grocery"].sum()
]

plt.figure()
plt.pie(category_totals, labels=["Electronics","Clothing","Grocery"], autopct="%1.1f%%")
plt.title("Sales Contribution by Category")
plt.show()

# ============================================
# STEP 6: BUSINESS INSIGHTS
# ============================================

best_month = df.loc[df["Total_Sales"].idxmax(), "Month"]
best_sales = df["Total_Sales"].max()

print("\n📌 Key Insights:")
print(f"✔ Highest sales occurred in {best_month}")
print(f"✔ Maximum total sales: {best_sales}")
print("✔ Grocery shows consistent growth throughout the year")
print("✔ Electronics contributes the highest revenue overall")
