# Assuming you have access to Python and pandas library
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset and select the 'Temp' variable
data = pd.read_csv("Algerian_forest_Modm.csv")
temperature = data['Temp']

# Construct histogram
plt.hist(temperature, bins=10, color='skyblue', edgecolor='black')
plt.title('Temperature Distribution')
plt.xlabel('Temperature (°C)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

