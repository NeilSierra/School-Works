# Request name 
name = input('\nEnter student name: ')
section = input('Enter student section: ')
# Get grades and round it off to the hundreths
prelim = round(float(input('\nEnter PRELIM grade: ')), 2)
midterm = round(float(input('Enter MIDTERM grade: ')), 2)
final = round(float(input('Enter FINAL grade: ')), 2)
if (prelim >= 40 and prelim <= 100) and (midterm >= 40 and midterm <= 100) and (final >= 40 and final <= 100):
    # Compute for the percentage of GPA
    prelim = (33.33 * prelim) / 100
    midterm = (33.33 * midterm) / 100
    final = (33.33 * final) / 100
    # Sume of all terms = gpa
    gpa = round((prelim + midterm + final))
    # Compute for the transmutation of gpa
    if gpa >= 99:
        grade_points = "1.00"
        general_description = "Excellent"
    elif gpa >= 96:
        grade_points = "1.25"
        general_description = "Outstanding"
    elif gpa >= 93:
        grade_points = "1.50"
        general_description = "Superior"
    elif gpa >= 90:
        grade_points = "1.75"
        general_description = "Very Good"
    elif gpa >= 87:
        grade_points = "2.00"
        general_description = "Good"
    elif gpa >= 84:
        grade_points = "2.25"
        general_description = "Satisfactory"
    elif gpa >= 81:
        grade_points = "2.50"
        general_description = "Fair Satisfactory"
    elif gpa >= 78:
        grade_points = "2.75"
        general_description = "Fair"
    elif gpa >= 75:
        grade_points = "3.00"
        general_description = "Passed"
    else:
        grade_points = "5.00"
        general_description = "Failed"
    # Display the final output
    print(f'\n\n===== GRADE SUMMARY =====' +
          f'\nName: {name}' +
          f'\nSection: {section}' +
          f'\nPrelim Grade: {prelim:.2f}%' +
          f'\nMidterm Grade: {midterm:.2f}%' +
          f'\nFinal Grade: {final:.2f}%' +
          f'\n\nGPA: {gpa}%' +
          f'\nGrade Points: {grade_points}' +
          f'\nGeneral Description: {general_description}')
else:
    print('\n\nThe program did not work due to the following erros: ')
    # Check if prelim is invalid
    if (prelim < 40 or prelim > 100):
        print('- Prelim grade is INVALID')
    # Check if midterm is invalid
    if (midterm < 40 or midterm > 100):
        print('- Midterm grade is INVALID')
    # Check if final is invalid
    if (final < 40 or final > 100):
        print('- Final grade is INVALID')