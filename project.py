import pandas as pd

print("================================")
print("STUDENT MARKS ANALYSER")
print("================================")

print("--- PART 1: PANDAS SERIES ---")
marks = [88, 76, 92, 67, 85]
student_marks = pd.Series(
    marks,
    index=["Aarav", "Meera", "Kabir", "Anaya", "Rohan"]
)
print(student_marks)

print("--- PART 2: PANDAS DATAFRAME ---")
data = {
    "Student": ["Aarav", "Meera", "Kabir", "Anaya", "Rohan"],
    "Math": [88, 76, 92, 67, 85],
    "Science": [91, 80, 89, 72, 87],
    "English": [84, 78, 95, 70, 82],
    "Attendance": [96, 90, 98, 85, 92]
}
df = pd.DataFrame(data)
print(df)

print("--- PART 3: CREATING & READING CSV FILE ---")
df.to_csv("student_marks.csv")
student_data = pd.read_csv("student_marks.csv")
print("CSV file read successfully!")
print(student_data)

print("--- PART 4: VIEWING DATA ---")
print("First 3 rows:")
print(student_data.head(3))
print("Last 2 rows:")
print(student_data.tail(2))
print("Dataset Info:")
print(student_data.info())

print("--- PART 5: CLEANING DATA ---")
messy_data = {
    "Student": ["Aarav", "Meera", "Kabir", "Anaya", "Rohan"],
    "Math": [88, None, 92, 67, 85],
    "Science": [91, 80, None, 72, 87],
    "English": [84, 78, 95, None, 82]
}
messy_df = pd.DataFrame(messy_data)
print("Data with Missing Values:")
print(messy_df)

cleaned_df = messy_df.fillna(0)
print("Missing Values Filled with 0:")
print(cleaned_df)

print("--- PART 6: SIMPLE ANALYSIS ---")
cleaned_df["Total"] = cleaned_df["Math"] + cleaned_df["Science"] + cleaned_df["English"]
cleaned_df["Average"] = cleaned_df["Total"] / 3
print(cleaned_df)

print("================================")
print("STUDENT MARKS ANALYSER SUMMARY")
print("================================")
print("Pandas was imported using import pandas as pd.")
print("A Series was used to store one column of marks.")
print("A DataFrame was used to store marks in table form.")
print("CSV data was created, read, and viewed.")
print("Missing values were cleaned using fillna().")
print("Total and average marks were calculated.")
print("================================")