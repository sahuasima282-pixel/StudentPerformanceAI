import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read CSV dataset
df = pd.read_csv("student.csv")

# Display student data
print("STUDENT DATASET")
print(df)

# Calculate average marks
average = np.mean(df["Marks"])
print("\nAverage Marks:", average)

# Find students who scored above 75
print("\nHigh Performing Students:")
print(df[df["Marks"] > 75])

# Create graph
plt.bar(df["Name"], df["Marks"])
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.title("Student Performance Analysis")

plt.savefig("performance.png")
plt.show()


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


# Function 1: Load student data
def load_data():
    try:
        file_path = Path("student.csv")

        if not file_path.exists():
            raise FileNotFoundError("student.csv not found")

        df = pd.read_csv(file_path)

        required_columns = [
            "Name", "Marks", "Attendance", "StudyHours"
        ]

        if not all(col in df.columns for col in required_columns):
            raise ValueError("Required columns are missing")

        if df.empty:
            raise ValueError("Student dataset is empty")

        return df

    except (FileNotFoundError, ValueError) as error:
        print("Error:", error)
        return None


# Function 2: Analyse student data
def analyse_data(df):
    average = np.mean(df["Marks"])

    print("\nSTUDENT PERFORMANCE REPORT")
    print(df)

    print("\nAverage Marks:", average)

    print("\nStudents scoring above 75:")
    print(df[df["Marks"] > 75])


# Function 3: Create performance graph
def create_graph(df):
    plt.bar(df["Name"], df["Marks"])

    plt.xlabel("Student Name")
    plt.ylabel("Marks")
    plt.title("Student Performance Analysis")

    plt.savefig("performance.png")
    plt.show()


# Main function
def main():
    df = load_data()

    if df is not None:
        analyse_data(df)
        create_graph(df)


if __name__ == "__main__":
    main()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


# Function 1: Load student data
def load_data():
    try:
        file_path = Path("student.csv")

        if not file_path.exists():
            raise FileNotFoundError("student.csv not found")

        df = pd.read_csv(file_path)

        required_columns = [
            "Name", "Marks", "Attendance", "StudyHours"
        ]

        if not all(col in df.columns for col in required_columns):
            raise ValueError("Required columns are missing")

        if df.empty:
            raise ValueError("Student dataset is empty")

        return df

    except (FileNotFoundError, ValueError) as error:
        print("Error:", error)
        return None


# Function 2: Analyse student data
def analyse_data(df):
    average = np.mean(df["Marks"])

    print("\nSTUDENT PERFORMANCE REPORT")
    print(df)

    print("\nAverage Marks:", average)

    print("\nStudents scoring above 75:")
    print(df[df["Marks"] > 75])


# Function 3: Create performance graph
def create_graph(df):
    plt.bar(df["Name"], df["Marks"])

    plt.xlabel("Student Name")
    plt.ylabel("Marks")
    plt.title("Student Performance Analysis")

    plt.savefig("performance.png")
    plt.show()


# Main function
def main():
    df = load_data()

    if df is not None:
        analyse_data(df)
        create_graph(df)


if __name__ == "__main__":
    main()

