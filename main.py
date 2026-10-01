# Program Name: Assignment2.py
# Course: IT3883/Section 85540
# # Student Name: Harash Banga
# Assignment Number: Lab2
# Due Date: 10/02/2026
# Purpose: Reads a file that contains student names and grades, the program
#          calculates each student's final average, and prints the results
#          in descending order by average.

#Initializing the txt file in the program
INPUT_FILE = "input.txt"

# Method that reads the file and calculates the average of student
def calcAvg(filename):
    student_averages = []

    with open(filename, "r") as file:
        for line in file:
            fields = line.split()
            # Skip blank lines
            if not fields:
                continue
            name = fields[0]
            scores = [float(score) for score in fields[1:len(fields)]]

            # Calculate the average of the scores
            average = sum(scores) / len(scores)
            student_averages.append((name, average))
    return student_averages

def main():
    averages = calcAvg(INPUT_FILE)
    # Sorting method by average with the highest average being first
    averages.sort(key=lambda student: student[1], reverse=True)

    # Print each student's name and average to two decimal places
    for name, average in averages:
        print(f"{name} {average:.2f}")
        print("------------")

if __name__ == "__main__":
    main()