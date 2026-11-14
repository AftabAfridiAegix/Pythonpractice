# Pandas is a Python library used for working with, cleaning, analyzing, and manipulating structured data.

# pd → Pandas
# DataFrame() → Pandas ka table banane wala function
# data → hamara dictionary
# df → DataFrame ko store karne wala variable
import pandas as pd
data = {
    "Name" : ["Ali", "Ahmed", "Sara", "Usman", "Ayesha"],
    "Age" : [23, 35, 28, 42, 31],
    "Disease" : ["Flu", "Diabetes", "Fever", "Flu", "Fever"],
    "Temperature" : [38.5, 37.2, 39.1, 38.0, 36.8]
}

df = pd.DataFrame(data)

print("\n --- Analysis ---")

print("Average Age:", df["Age"].mean())
print("Highest Temperature:", df["Temperature"].max())

high_temperature = df[df["Temperature"] > 38]

print("\n--- Temperature Above 38 ---")
print(high_temperature)

flu_patients = df[df["Disease"] == "Flu"]

print("\n--- Flu Patients ---")
print(flu_patients)

print("\n--- Disease Count ---")
print(df["Disease"].value_counts())

print("\n--- Patients Sorted by Age ---")
print(df.sort_values("Age"))