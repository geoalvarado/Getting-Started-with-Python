import matplotlib.pyplot as plt
import pandas as pd
import datetime

# Define course schedule

# Extend course list with all 12 AI Engineer courses (I should make a list out of this)
ai_engineer_courses = [f"AI Engineer Course {i+1}" for i in range(12)]

# Calculate start and end dates for each AI course (1 per week)
ai_start_dates = pd.date_range(start="2025-03-17", periods=12, freq="W-MON")
ai_end_dates = ai_start_dates + pd.Timedelta(days=6)

# Update course schedule
courses = [
    ("Data Manipulation with Pandas", "2025-02-26", "2025-03-02"),
    ("Introduction to Statistics with Python", "2025-03-03", "2025-03-09"),
    ("Supervised Learning with Scikit-Learn", "2025-03-10", "2025-03-16"),
]

# Append AI Engineer courses
for course, start, end in zip(ai_engineer_courses, ai_start_dates, ai_end_dates):
    courses.append((course, start.strftime("%Y-%m-%d"), end.strftime("%Y-%m-%d")))

# Convert to DataFrame
df = pd.DataFrame(courses, columns=["Course", "Start", "End"])
df["Start"] = pd.to_datetime(df["Start"])
df["End"] = pd.to_datetime(df["End"])

# Plot updated Gantt chart with start dates labeled
fig, ax = plt.subplots(figsize=(10, 6))

for i, (course, start, end) in enumerate(zip(df["Course"], df["Start"], df["End"])):
    ax.barh(course, (end - start).days, left=start, color="skyblue")
    ax.text(start, i, start.strftime("%Y-%m-%d"), va="center", ha="right", fontsize=8, color="black")

# Define start of the year:
dates = df["Start"]
min_date = min(dates)  # Get the earliest date in your data
start_of_year = datetime.datetime(min_date.year, 2, 1)  # Set to January 1st of that year

# Format plot
ax.set_xlabel("Date")
ax.set_ylabel("Course")
ax.set_title("AI & ML Learning Plan Gantt Chart (With Start Dates)")
ax.xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter("%b %Y"))
ax.set_xlim(start_of_year, max(dates))  # Extend to the max date
plt.xticks(rotation=45)

# Show plot
plt.show()