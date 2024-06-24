class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):

    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    grading_scale = {"O": (100, 90), "E": (89, 80), "A": (
        79, 70), "P": (69, 55), "D": (54, 40), "T": (39, 0)}

    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        sum_scores = sum(self.scores)
        grade_points = sum_scores // len(self.scores)

        for letter, (max_grade, min_grade) in self.grading_scale.items():
            if grade_points <= max_grade and grade_points >= min_grade:
                grade_letter = letter
                return grade_letter

        return ValueError("Grade must be between 100 and 0")


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
