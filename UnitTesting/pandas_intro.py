#pandas is a python library used for data manipulation and analysis
# It provides data structures like DataFrames and Series to work with structured data
# It offers functionalities for data cleaning, transformation, aggregation, and visualization

import pandas as pd

#pandas works great with matplotlib!
import matplotlib.pyplot as plt

# Create a simple DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 30, 22, 35],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

df = pd.DataFrame(data)
print("DataFrame:\n", df)

# Accessing columns
print("\nNames Column:\n", df['Name'])

# Accessing rows by index location
print("\nFirst Row:\n", df.iloc[0])

# Filtering data
adults = df[df['Age'] >= 25]
print("\nAdults (Age >= 25):\n", adults)

# Adding a new column
df['Salary'] = [70000, 80000, 60000, 90000]
print("\nDataFrame with Salary Column:\n", df)

# Basic statistics
print("\nAverage Age:", df['Age'].mean())
print("Maximum Salary:", df['Salary'].max())
print("Summary Statistics:\n", df.describe())

# Sorting data
sorted_df = df.sort_values(by='Age')
print("\nDataFrame sorted by Age:\n", sorted_df)

vehicle_df = pd.read_csv("./data/Electric_Vehicle_Population_Data.csv")
print("\nvehicle DataFrame:\n", vehicle_df.head())
print("\nvehicle DataFrame Info:", vehicle_df.info())

#basic selection and filtering of vehicle data
#select each unique vehicle make
vehicle_makes = vehicle_df['Make'].unique()
print("\nUnique Vehicle Makes:\n", vehicle_makes)

#filter vehicles made by Tesla
tesla_vehicles = vehicle_df[vehicle_df['Make'] == 'TESLA']
print("\nTesla Vehicles:\n", tesla_vehicles)

#filter using NOT using the ~ operator aka NOT operator in pandas
non_tesla_vehicles = vehicle_df[~(vehicle_df['Make'] == 'TESLA')]
#we can also decide to only return the first 5 rows of the non-tesla vehicles
print("\nNon-Tesla Vehicles:\n", non_tesla_vehicles.head(5))

#we can also aggregate data
#this will give us the average electric range by vehicle make
#and filter out those with values of 0
avg_range_by_make = vehicle_df[vehicle_df['Electric Range'] > 0].groupby('Make')['Electric Range'].mean()
print("\nAverage Electric Range by Make:\n", avg_range_by_make)

#finally, let's visualize our data using matplotlib
#we can create a Figure - a matplotlib object that represents the entire figure or plot area
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

#plot the average electric range by vehicle make as a bar chart
avg_range_by_make.plot(kind='bar', ax=axes[0, 0], title='Average Electric Range by Vehicle Make')
plt.xlabel('Vehicle Make')
plt.ylabel('Average Electric Range (miles)')

#plot the count of non tesla vehicles by model year
non_tesla_vehicles['Model Year'].value_counts().sort_index().plot(kind='bar', ax=axes[0, 1], title='Count of Non-Tesla Vehicles by Model Year')
plt.xlabel('Model Year')
plt.ylabel('Number of Vehicles')
plt.show()

#Finally, we can export our modified DataFrame to a new CSV file
non_tesla_vehicles.to_csv('./data/modified_vehicle_data.csv', index=False)