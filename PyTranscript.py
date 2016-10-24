import sys

# list of tuples with the following format:
# ( quarter, subject, course number, grade )
# ex. ( 'Fall 2014', 'CMPS', '5J', 'A+' )
# we only care about CMPS and CMPE
# ( quarter, subject, course number ) will be used
# to index into the DB to find the teacher and the
# final tuple will be the following:
# ( quarter, subject, course number, professor, grade )
# ex. ( 'Fall 2014', 'CMPS', '5J', 'Patrick Tantalo', 'A+' )
# file output format will look like the following:
#
# Name: John Doe
#    Fall 2014
#       CMPS 5J Patrick Tantalo A+
#       CMPS 12A Wesley Mackey C+
#    Winter 2015
#       CMPE 13 ... A-

name = ''
quarters = []
courses = []

subjects = [ 'CMPS', 'CMPE', 'MATH', 'AMS', 'CMPM' ]

for line in sys.stdin:
    columns = line.split( ',' )
    if len( columns ) >= 2:
        # parse the name
        if 'Name:' in columns[ 0 ] and name == '':
            nameInfo = line.split( '\"' )[ 1 ].split( ' ' )[ 1: ]
            lastName = columns[ 0 ].split( ':' )[ 1 ]
            nameInfo.append( lastName )
            name = ' '.join( nameInfo )
            continue
    if len( columns ) >= 3:
        # set the current quarter
        if 'Quarter' in columns[ 2 ]:
            quarterInfo = columns[ 2 ].split()
            quarters.append( quarterInfo[ 1 ] + ' ' + quarterInfo[ 0 ] )
            continue
    if len( columns ) > 0:
        columns = line.replace( '\"', '' ).split( ',' )
        courseInfo = columns[ 0 ].split()
        subject = ''
        if len( courseInfo ) > 0:
            subject = courseInfo[ 0 ]
        # add the course to the courses list
        if subject in subjects:
            print line.replace( '\"', '' )
            if len( courseInfo ) == 2:
                courseId = courseInfo[ 1 ]
            elif len( courseInfo ) == 1:
                courseId = columns[ 1 ].split()[ 0 ]
            gradeInfo = columns[ 4 ].split()
            if len( gradeInfo ) == 2:
                grade = gradeInfo[ 1 ]
            else:
                grade = 'N/A'
            courses.append( ( quarters[ -1 ], subject, courseId, grade ) )
            continue

print "Name: " + name
if len( quarters ) > 0:
    currentQuarter = quarters[ 0 ]
else:
    exit( 0 )
print "\n--- " + currentQuarter + ' ---\n'
for course in courses:
    if course[ 0 ] != currentQuarter:
        print "\n--- " + course[ 0 ] + ' ---\n'
        currentQuarter = course[ 0 ]
    print "      %s\t%s\t%s" % ( course[ 1 ], course[ 2 ], course[ 3 ] )
