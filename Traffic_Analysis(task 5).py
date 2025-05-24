import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
df = pd.read_csv('https://docs.google.com/spreadsheets/d/18Cu1pwloSlHJwpVeladWGDZviwjvZXcBNevlILGXbe4/export?format=csv')
print(df.head)

# Convert Start_Time column to datetime format
df['Time'] = pd.to_datetime(df['Time'], errors='coerce')
df = df.dropna(subset=['Time'])

# Extract day of the week and hour from Start_Time
df['Day_Of_week'] = df['Time'].dt.day_name()
df['Hour'] = df['Time'].dt.hour

# Categorize time of day
def get_time_of_day(hour):
if 5 <= hour < 12:
return 'Morning'
elif 12 <= hour < 17:
return 'Afternoon'
elif 17 <= hour < 21:
return 'Evening'
else:
return 'Night'

df['Time'] = df['Hour'].apply(get_time_of_day)

# --- Plot 1: Accidents by Day of the Week ---
plt.figure(figsize=(8,6))
order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
sns.countplot(data=df, x='Day_Of_week', order=order)
plt.title('Accidents by Day of the Week')
plt.xlabel('Day')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --- Plot 2: Accidents by Time of Day ---
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='Time', order=['Morning', 'Afternoon', 'Evening', 'Night'])
plt.title('Accidents by Time of Day')
plt.xlabel('Time of Day')
plt.ylabel('Number of Accidents')
plt.tight_layout()
plt.show()

import seaborn as sns

# Replace with correct column names if different
light_severity = df.groupby(['Light_conditions', 'Casualty_severity']).size().unstack().fillna(0)

# Plot
light_severity.plot(kind='barh', stacked=False, figsize=(10,6))
plt.title('Accident Severity under Different Light Conditions')
plt.xlabel('Number of Accidents')
plt.ylabel('Light Conditions')
plt.legend(title='Severity')
plt.tight_layout()
plt.show()

road_weather = df.groupby(['Road_surface_conditions', 'Weather_conditions']).size().unstack().fillna(0)

# Plot
road_weather.plot(kind='bar', figsize=(14,7))
plt.title('Accident Counts by Road Condition and Weather')
plt.xlabel('Road surface condition')
plt.ylabel('Number of Accidents')
plt.legend(title='Weather conditions', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


