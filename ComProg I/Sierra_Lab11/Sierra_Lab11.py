print('\n\n\nEnter the grade of the Students (Should only be 40-100 | Enter "DONE" to end)\n')

grades = []
studentNum = 1
systemLoop = True
totalGrade = 0
passedStudentNum = 0

while systemLoop == True:
    studentGrade = input(f'Student #{studentNum}: ')
    if studentGrade.replace(".", "", 1).isdigit() and studentGrade.count(".") <= 1:
        studentGrade = float(studentGrade)
        if studentGrade >= 40 and studentGrade <= 100:
            grades.append(studentGrade)
            studentNum += 1
            continue
        else:
            print('[Invalid Input] Please enter a number between 40 and 100.')
            continue
    elif studentGrade.lower() == 'done':
        systemLoop = False
    else:
        print('[Invalid Input] Please enter a number.')
        continue
else:
    if grades != []:
        for grade in grades:
            totalGrade += grade
            averageGrade = totalGrade / len(grades)
        else:
            print(f'\n\n\nAverage Grade: {averageGrade:.2f}')
        for grade in grades:
            if grade >= 75:
                passedStudentNum += 1
        else:
            print(f'Number of Passed Students: {passedStudentNum}')
            passPercentage = (passedStudentNum / len(grades)) * 100
            print(f'Pass Percentage: {passPercentage:.2f}%')
    else:
        print('No grade have been entered.')
