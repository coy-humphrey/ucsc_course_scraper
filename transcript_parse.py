import csv
from ucsc_types import Student, Quarter, Course

subjects = [ 'CMPS', 'CMPE', 'EE', 'MATH', 'AMS', 'CMPM' ]

def process_name( row ):
    lastName = row[ 0 ].split( ',' )[ 0 ].split( ':' )[ 1 ]
    fullNameList = row[ 0 ].split( ',' )[ 1 ].split() + [ lastName ]
    fullName = ' '.join( fullNameList )
    return Student( fullName )

def process_gpa( row, student ):
    longRow = ' '.join( row )
    student.gpa = longRow.split()[ 3 ]

def process_quarter( row ):
    quarterInfo = ' '.join( row ).split()
    quarterName = quarterInfo[ 1 ] + ' ' + quarterInfo[ 0 ]
    return Quarter( quarterName )

def process_course( row ):
    courseInfo = ' '.join( row ).split()
    subject = courseInfo[ 0 ]
    number = courseInfo[ 1 ]
    grade = 'N/A'
    units = courseInfo[ -3 ]
    name = ' '.join( courseInfo[ 2:-3 ] )
    try:
        float( courseInfo[ -2 ] )
    except ValueError:
        grade = courseInfo[ -2 ]
        units = courseInfo[ -4 ]
        name = ' '.join( courseInfo[ 2:-4 ] )
    return Course( subject, number, name, [ '' ], grade, units )

def student_from_transcript( input ):
    student = None
    for row in csv.reader( input ):
        if not student:
            if len( row ) > 0 and 'Name:' in row[ 0 ]:
                student = process_name( row )
        elif len( row ) > 0:
            if len( row ) >= 3 and 'Quarter' in ' '.join( row ):
                student.quarters.append( 
                    process_quarter( row ) )
            elif 'Combined Cum GPA' in row[ 0 ]:
                process_gpa( row, student );
            elif len( student.quarters ) > 0:
                subject = ''
                if len( row[ 0 ].split() ) == 2:
                    subject = row[ 0 ].split()[ 0 ]
                else:
                    subject = row[ 0 ]
                if subject in subjects:
                    student.quarters[ -1 ].courses.append(
                       process_course( row ) )
    return student
