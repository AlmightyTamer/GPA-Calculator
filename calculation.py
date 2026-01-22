# Simple GPA Calculator (based on your table)

# Quality points table
points = {
    "AP": {
        "A+": 5.7, "A": 5.3, "A-": 5.0,
        "B+": 4.7, "B": 4.3, "B-": 4.0,
        "C+": 3.7, "C": 3.3, "C-": 3.0,
        "D+": 2.7, "D": 2.3, "D-": 2.0,
        "F": 0
    },
    "HONORS": {
        "A+": 5.2, "A": 4.8, "A-": 4.5,
        "B+": 4.2, "B": 3.8, "B-": 3.5,
        "C+": 3.2, "C": 2.8, "C-": 2.5,
        "D+": 2.2, "D": 1.8, "D-": 1.5,
        "F": 0
    },
    "A LEVEL": {
        "A+": 4.7, "A": 4.3, "A-": 4.0,
        "B+": 3.7, "B": 3.3, "B-": 3.0,
        "C+": 2.7, "C": 2.3, "C-": 2.0,
        "D+": 1.7, "D": 1.3, "D-": 1.0,
        "F": 0
    }
}

total_points = 0
num_classes = int(input("How many classes? "))

for i in range(num_classes):
    print(f"\nClass {i + 1}")
    level = input("Enter level (AP / Honors / A Level): ").upper()
    grade = input("Enter grade (A+, A, A-, B+, etc): ").upper()

    class_points = points[level][grade]
    total_points += class_points

gpa = total_points / num_classes
print("\nYour GPA is:", round(gpa, 2))
