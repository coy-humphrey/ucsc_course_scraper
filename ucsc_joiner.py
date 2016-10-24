def student_combined( student, course_dict ):
    for quarter in student.quarters:
        yearName = quarter.name.split()[ 1 ]
        quarterName = quarter.name.split()[ 0 ].lower()
        for course in quarter.courses:
            courseName = course.subject + course.number
            try:
                course.instructors = \
                    course_dict[ yearName ][ courseName ][ quarterName ]
            except:
                pass
    return student
