import csv
from ucsc_types import Student, Quarter, Course

subjects = [ 'CMPS', 'CMPE', 'MATH', 'AMS', 'CMPM' ]

def process_name( row ):
    lastName = row[ 0 ].split( ',' )[ 0 ].split( ':' )[ 1 ]
    fullNameList = row[ 0 ].split( ',' )[ 1 ].split() + [ lastName ]
    fullName = ' '.join( fullNameList )
    return Student( fullName )

def process_quarter( row ):
    quarterInfo = row[ 2 ].split()
    quarterName = quarterInfo[ 1 ] + ' ' + quarterInfo[ 0 ]
    return Quarter( quarterName )

def process_course( row ):
    if len( row[ 0 ].split() ) == 2:
        subject = row[ 0 ].split()[ 0 ]
        number = row[ 0 ].split()[ 1 ]
        name = row[ 1 ]
    else:
        subject = row[ 0 ]
        number = row[ 1 ].split()[ 0 ]
        name = ' '.join( row[ 1 ].split()[ 1: ] )
    gradeInfo = row[ 4 ].split()
    if len( gradeInfo ) != 2:
        grade = 'N/A'
    else:
        grade = gradeInfo[ 1 ]
    return Course( subject, number, name, [ '' ], grade )

def student_from_transcript( input ):
    student = None
    for row in csv.reader( input ):
        if not student:
            if len( row ) > 0 and 'Name:' in row[ 0 ]:
                student = process_name( row )
        else:
            if len( row ) >= 3 and 'Quarter' in row[ 2 ]:
                student.quarters.append( 
                    process_quarter( row ) )
            elif len( row ) > 0 and len( student.quarters ) > 0:
                subject = ''
                if len( row[ 0 ].split() ) == 2:
                    subject = row[ 0 ].split()[ 0 ]
                else:
                    subject = row[ 0 ]
                if subject in subjects:
                    student.quarters[ -1 ].courses.append(
                       process_course( row ) )
    return student
