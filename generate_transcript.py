import sys
import json
from transcript_parse import student_from_transcript
from ucsc_joiner import student_combined

csv_transcript_input = []
for line in sys.stdin:
    csv_transcript_input.append( line )

student = student_from_transcript( csv_transcript_input )

course_dict_filename = 'courses.json'

with open( course_dict_filename ) as data_file:    
    course_dict = json.load( data_file )

student = student_combined( student, course_dict )

print 'Name: ' + student.name
print 'GPA: ' + student.gpa
for quarter in student.quarters:
    print '\n----- ' + quarter.name + ' -----\n'
    for course in quarter.courses:
        print '  %s%s%s%s%s%s' % \
            ( course.subject.ljust( 6 ), course.number.ljust( 7 ), course.units.ljust( 8 ), 
              course.grade.ljust( 7 ), course.name.ljust( 25 ), ' | '.join( course.instructors ) )
print '\n'
