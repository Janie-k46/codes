import pandas as pd
import matplotlib.pyplot as plt

# Dataset
df = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Revenue': [120, 135, 150, 160, 155],
    'Expenses': [80, 85, 95, 100, 98],
    'ProfitMargin': [33, 37, 35, 38, 37],
    'CustomerGrowth': [5, 6, 8, 9, 7],
    'MarketingIndex': [1.2, 1.3, 1.5, 1.6, 1.4]
})

# Plot
df.plot(x='Month', y=['Revenue', 'Expenses', 'ProfitMargin'])
plt.title("Financial Performance Trends")
plt.ylabel("Values")
plt.show()

# Correlation
print(df.corr(numeric_only=True))
