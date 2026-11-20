import numpy as np
import pandas as pd

# Student data
data = {
    "Name": ["Asima", "Rahul", "Priya", "Amit", "Sneha"],
    "Marks": [85, 65, 92, 45, 78],
    "Attendance": [90, 75, 95, 60, 85]
}

df = pd.DataFrame(data)

print("STUDENT PERFORMANCE REPORT")
print(df)

print("\nAverage Marks:", np.mean(df["Marks"]))

print("\nStudents scoring above 75:")
print(df[df["Marks"] > 75])

