"""
Data Science Basics - A beginner project
------------------------------------------
This script demonstrates the core steps of a simple Data Science workflow:
1. Load data
2. Clean data (handle missing values)
3. Explore data (basic statistics)
4. Visualize data (simple charts)

Dataset: students_data.csv (sample student records)
"""

import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 1. Load Data
# -----------------------------
df = pd.read_csv("students_data.csv")

print("----- Raw Data -----")
print(df)

# -----------------------------
# 2. Data Cleaning
# -----------------------------
# Fill missing numeric values (age, study_hours) with column mean
df["age"] = df["age"].fillna(df["age"].mean())
df["study_hours"] = df["study_hours"].fillna(df["study_hours"].mean())

# Fill missing categorical values (city) with "Unknown"
df["city"] = df["city"].fillna("Unknown")

print("\n----- Cleaned Data -----")
print(df)

# -----------------------------
# 3. Exploratory Data Analysis (EDA)
# -----------------------------
print("\n----- Basic Statistics -----")
print(df.describe())

print("\n----- Average Score by City -----")
print(df.groupby("city")["score"].mean())

# -----------------------------
# 4. Data Visualization
# -----------------------------

# Bar chart: Study hours vs Score
plt.figure(figsize=(8, 5))
plt.bar(df["name"], df["score"], color="skyblue")
plt.xlabel("Student")
plt.ylabel("Score")
plt.title("Student Scores")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("scores_chart.png")
plt.close()

# Scatter plot: Study hours vs Score
plt.figure(figsize=(8, 5))
plt.scatter(df["study_hours"], df["score"], color="green")
plt.xlabel("Study Hours")
plt.ylabel("Score")
plt.title("Study Hours vs Score")
plt.tight_layout()
plt.savefig("study_vs_score.png")
plt.close()

print("\nCharts saved as 'scores_chart.png' and 'study_vs_score.png'")
