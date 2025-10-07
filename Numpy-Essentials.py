import numpy as np

# Create the grades array
grades = np.array([85, 90, 88, 92, 95, 80, 75, 98, 89, 83])

# 1. Calculate mean, median, and standard deviation
mean_grade = np.mean(grades)
median_grade = np.median(grades)
std_dev = np.std(grades)

# 2. Find maximum and minimum grades
max_grade = np.max(grades)
min_grade = np.min(grades)

# 3. Sort grades in ascending order
sorted_grades = np.sort(grades)

# 4. Find the index of the highest grade
index_highest = np.argmax(grades)

# 5. Count the number of students scoring above 90
count_above_90 = np.sum(grades > 90)

# 6. Calculate percentages
percent_above_90 = np.mean(grades > 90) * 100
percent_below_75 = np.mean(grades < 75) * 100

# 7. Extract subsets
high_performers = grades[grades > 90]
passing_grades = grades[grades > 75]

# Print all results neatly
print("📊 Student Grades Analysis 📊\n")
print(f"Grades: {grades}")
print(f"\nMean Grade: {mean_grade:.2f}")
print(f"Median Grade: {median_grade:.2f}")
print(f"Standard Deviation: {std_dev:.2f}")
print(f"Highest Grade: {max_grade}")
print(f"Lowest Grade: {min_grade}")
print(f"\nSorted Grades: {sorted_grades}")
print(f"Index of Highest Grade: {index_highest}")
print(f"\nNumber of Students Scoring Above 90: {count_above_90}")
print(f"Percentage Above 90: {percent_above_90:.2f}%")
print(f"Percentage Below 75: {percent_below_75:.2f}%")
print(f"\nHigh Performers (Grades > 90): {high_performers}")
print(f"Passing Grades (Grades > 75): {passing_grades}")
