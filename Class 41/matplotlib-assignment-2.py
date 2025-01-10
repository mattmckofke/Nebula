import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_json("student_data.json")
print(df.head())

# The students sleep for a high number of hours
# The students study for a medium number of hours
# The students play sports for a low number of hours
# The students have a medium amount of leisure time

# Create a histogram of the students' study hours
plt.hist(df['Study'], bins=len(df), color='blue', edgecolor='black')
plt.xlabel('Study Hours')
plt.ylabel('Number of Students')
plt.title('Histogram of Study Hours')
plt.show()

# The most amount of students study for over 35 hours
# The same amount of studtent study for 15-20 hours, 20-25 hours, and 25-30 hours

# Create a histogram of the students' sports hours
plt.hist(df['Sports'], bins=len(df), color='red', edgecolor='black')
plt.xlabel('Sports Hours')
plt.ylabel('Number of Students')
plt.title('Histogram of Sports Hours')
plt.show()

# Students play sports for a low number of hours compared to study hours
# The most amount of students play sports for 0-5 hours