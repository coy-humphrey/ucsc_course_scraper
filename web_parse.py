from bs4 import BeautifulSoup
from collections import OrderedDict
import json

def parse_classes( html_contents, results ):
    soup = BeautifulSoup( html_contents, 'html.parser' )
    year = page_year( soup )
    results[year] = results.get( year, OrderedDict() )
    for course in courses( soup ):
        results[ year ][ course_name( course ) ] = professors( course )

def courses( soup ):
    return soup.find_all( 'td', class_="course-name" )

# Given a course, the first a element will be a link to the course
# web page, with the link title being the full name of the course
# Format is: COURSENUMBER: Full Course Name
# Therefore, if we grab everything before the :, we will have the course number
def course_name( course ):
    name = str( course.find_next( 'a' ).contents[ 0 ] )
    return name[ : name.find( ':' ) ].upper()

# Given a course, a 'tr' will contain 4 'td's, each 'td' representing a quarter.
def professors( course ):
    result = OrderedDict()
    quarters = [ 'fall', 'winter', 'spring', 'summer' ]
    for quarter, listing in zip( quarters, course_listings( course ) ):
        result[quarter] = { section_name( section ): section_professor_name( section )
                            for section in listing.find_all( 'a' )
                            if listing_has_classes( listing ) }
    return result

def course_listings( course ):
    return course.find_next( 'tr' ).find_all( 'td' )

# The contents of each 'a' within a 'td' will be "Section X".
def section_name( section ):
    return section.contents[ 0 ]

# After each 'a', there will be a 'br' followed by the professor's name.
def section_professor_name( section ):
    return section.next_sibling.next_sibling.strip()

# If a 'td's class name is just 'class', then it will contain valid classes.
# Otherwise, if it is 'class inactive', it will have no classes.
# Grabbing the class name gives us either ['class'] or ['class', 'invalid'],
# so we can just check to see if the length is 1 to know if it's valid.
def listing_has_classes( listing ):
    return listing.get( 'class' ) and len( listing.get( 'class' ) ) == 1

def page_year( soup ):
    title = str(soup.title)
    end_i = title.find('|') - 1
    return int(title[end_i-4:end_i])

# For now we just manually download a single course page,
# rename it to ucsc.html, and test with it
# Future plan is to take a list of filenames in
# argv, parse each file and dump into same csv
results = OrderedDict()
parse_classes( open( 'cmpe' ), results )

print json.dumps( results, indent=4 )
