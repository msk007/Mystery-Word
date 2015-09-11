cohort1 = {
'Avery': [63, 62, 41, 66, 84, 82, 73, 89, 69, 75],
'Blake': [79, 97, 78, 78, 74, 69, 80, 100, 74, 70],
'Casey': [93, 97, 99, 95, 98, 91, 96, 99, 100, 88],
'Dakota': [71, 65, 72, 65, 24, 100, 84, 71, 59, 50],
'Elliot': [84, 73, 90, 72, 69, 93, 61, 65, 81, 98],
'Fox': [80, 91, 90, 80, 83, 73, 84, 89, 84, 84],
'Gale': [41, 7, 64, 60, 78, 48, 73, 50, 69, 89]
}

def student_names(drop_lowest=False, dictionary):
    student_means = {}
    for student, grades in dictionary.items():
        if drop_lowest=True:
            del min(grades)
        length = len(grades)
        this_student = (sum(grades)/length)
        student_means.update({student: this_student})
    print(student_means)
student_names(cohort1)
