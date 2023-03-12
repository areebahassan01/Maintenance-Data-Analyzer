import pandas as pd
import matplotlib.pyplot as plt

# Load maintenance data from a CSV file
df = pd.read_csv('maintenance_data.csv', parse_dates=['Request Date', 'Completion Date'])

# Calculate the 
df['Duration'] = (df['Completion Date'] - df['Request Date']).dt.days

# Visualize maintenance request counts over time with a histogram
plt.figure(figsize=(10,5))
plt.hist(df['Request Date'], bins=50, color='green')
plt.title('Maintenance Request Counts over Time')
plt.xlabel('Request Date')
plt.ylabel('Request Count')
plt.show()

# Visualize maintenance request durations over time with a boxplot
plt.figure(figsize=(50,20))
df.boxplot(column='Duration', by='Request Date', vert=False)
plt.title('Maintenance Request Durations over Time')
plt.xlabel('Duration (Days)')
plt.ylabel('Request Date')
plt.show()
