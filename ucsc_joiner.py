def student_combined( student, course_dict ):
    for quarter in student.quarters:
        year = int( quarter.name.split()[ 1 ] )
        quarterName = quarter.name.split()[ 0 ].lower()
        if quarterName == 'fall':
            year += 1
        for course in quarter.courses:
            courseName = course.subject + course.number
            '''
            if str( year ) not in course_dict:
                print str( year ) + " not in dict"
            elif courseName not in course_dict[ str( year ) ]:
                print courseName + " not in dict"
            elif quarterName not in course_dict[ str( year ) ][ courseName ]:
                print quarterName + " not in dict"
                '''
            try:
                course.instructors = \
                    course_dict[ str( year ) ][ courseName ][ quarterName ].values()
            except:
                pass
    return student
