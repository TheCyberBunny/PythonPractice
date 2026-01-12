#matplotlib is a comprehensive library for creating static, animated, and interactive visualizations
# It provides an object-oriented API for embedding plots into applications using 
# general-purpose GUI toolkits like Tkinter, wxPython, Qt, or GTK.
import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create a simple line plot
plt.plot(x, y, marker='o', linestyle='-', color='b', label='Line 1')
plt.title('Simple Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.show()

# Create a bar chart
categories = ['A', 'B', 'C', 'D']
values = [5, 7, 3, 8]
plt.bar(categories, values, color='g')
plt.title('Simple Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()

# Create a scatter plot
x_scatter = [1, 2, 3, 4, 5]
y_scatter = [5, 4, 3, 2, 1]
plt.scatter(x_scatter, y_scatter, color='r')
plt.title('Simple Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

