import matplotlib.pyplot as plt

plt.plot(df['Month'], df['PassengerCount'], marker='o')
plt.title("Passenger Trend Over Time")
plt.xlabel("Month")
plt.ylabel("Passengers")
plt.show()
