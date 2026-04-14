# Variance
variance = df['PassengerCount'].var()

# Standard deviation
std_dev = df['PassengerCount'].std()

# Correlation matrix
correlation = df[['PassengerCount','AvgTemp','Rainfall']].corr()

print("Variance:", variance)
print("Standard Deviation:", std_dev)
print("Correlation:\n", correlation)
