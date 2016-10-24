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
for quarter in student.quarters:
    print '\n----- ' + quarter.name + ' -----\n'
    for course in quarter.courses:
        print '  %s\t%s\t%s\t%s\t%s' % \
            ( course.subject, course.number, course.grade, 
              course.name, ' | '.join( course.instructors ) )
print '\n'
