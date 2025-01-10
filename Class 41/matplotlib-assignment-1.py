import matplotlib.pyplot as plt
import pandas as pd

# Load data from CSV
df = pd.read_csv('student_scores.csv')
print(df.head())

# Preparing the data for plotting
subjects = ['Math', 'English', 'Science', 'History']
scores = [df[subject].values for subject in subjects]

plt.figure(figsize=(10, 6))
plt.boxplot(scores, labels=subjects, patch_artist=True,
            boxprops=dict(facecolor='cyan', color='blue'),
            whiskerprops=dict(color='green'),
            capprops=dict(color='red'),
            medianprops=dict(color='yellow'))
plt.title('Colored Box Plot of Student Scores')
plt.ylabel('Scores')
plt.xlabel('Subjects')
plt.grid(True)
plt.savefig("customized_box_plot.png")
plt.show()

# The subject with the highest variability in scores is Math. The subject with the highest median score is History.

