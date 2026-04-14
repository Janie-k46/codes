import pandas as pd

df = pd.DataFrame({
    'Month': ['Jan','Feb','Mar','Apr','May','Jun'],
    'PassengerCount': [112,118,132,129,121,135],
    'AvgTemp': [30,32,35,33,31,34],
    'Rainfall': [5,7,3,6,8,4]
})

# Rolling average (3-month)
df['RollingAvg'] = df['PassengerCount'].rolling(window=3).mean()

# Percentage change
df['PctChange'] = df['PassengerCount'].pct_change() * 100

print(df)
