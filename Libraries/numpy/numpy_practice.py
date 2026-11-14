# NumPy is a Python library that provides powerful tools for working with numerical data, especially arrays and mathematical calculations.
#  Data Science
#  AI & Machine Learning
#  Data Analysis
#  Scientific Computing

import numpy as np

marks = []
n = int(input("Enter number of students: "))
for i in range(n):
    mark = float(input(f"Enter marks {i + 1}: "))
    marks.append(mark)

data = np.array(marks)

print("\n--- Performance Report ---")
print("Marks:", data)
print("Average:", np.mean(data))
print("Highest:", np.max(data))
print("Lowest:", np.min(data))

passed = data[data >= 50]
failed = data[data < 50]

print("Passed:", len(passed))
print("Failed:", len(failed))

percentage = (len(passed) / len(data)) * 100

print("Pass Percentage:", percentage)






