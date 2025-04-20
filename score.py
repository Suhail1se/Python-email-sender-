import numpy as np

# Scores of 5 students in 3 subjects: [Math, Science, English]
scores = np.array([
    [78, 85, 90],
    [88, 79, 92],
    [90, 91, 85],
    [70, 68, 72],
    [95, 89, 94]
])

# 1. Average score of each student
student_avg = np.mean(scores, axis=1)
print("Average score per student:", student_avg)

# 2. Average score per subject
subject_avg = np.mean(scores, axis=0)
print("Average score per subject:", subject_avg)

# 3. Highest score and the student who got it
highest_score = np.max(scores)
student_index, subject_index = np.unravel_index(np.argmax(scores), scores.shape)
print(f"Highest score is {highest_score} by student {student_index + 1} in subject {subject_index + 1}")
