
#Read the names and marks of at least 3 students
#Rank the top three students with highest marks
#Give cash rewards. $500 for first rank, $300 for
#...second rank, $100 for third rank. Value cannot be
#...modified
#Appreciate students who secured 950 marks and above

import operator

def read_student_details():
    #Ex: 'Kai':500, 'Zen':600, 'Eric':800
    print("Enter the number of students:")
    number_of_students = int(input())
    student_record = {}
    for student in range(0, number_of_students):
        print("Enter the name of the student: ")
        name = input()
        print("Enter the grade of the student: ")
        grade = int(input())
        student_record[name] = grade
    return student_record

def rank_students(student_record):
    sorted_student_record = sorted(student_record.items(),
    key = operator.itemgetter(1))
    print(sorted_student_record)

def rewards_students():
    pass

def appreciate_students():
    pass

student_record = read_student_details()
rank_students(student_record)
