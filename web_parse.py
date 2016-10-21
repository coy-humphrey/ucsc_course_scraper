from bs4 import BeautifulSoup
import urllib2

def parse_classes( html_contents ):
    soup = BeautifulSoup( html_contents, 'html.parser' )
    for course in courses( soup ):
        print course_name( course )
        for section, profs in professors( course ).items():
            print section, profs

def courses( soup ):
    return soup.find_all('td', class_="course-name")

# Given a course, the first a element will be a link to the course
# web page, with the link title being the full name of the course
# Format is: COURSENUMBER: Full Course Name
def course_name( course ):
    return course.find_next('a').contents[0]

# Given a course, a 'tr' will contain 4 'td's, each 'td' representing a quarter.
# If a 'td's class name is just 'class', then it will contain valid classes.
# Otherwise, if it is 'class inactive', it will have no classes.
# Grabbing the class name gives us either ['class'] or ['class', 'invalid'],
# so we can just check to see if the length is 1 to know if it's valid.
# The contents of each 'a' within a 'td' will be "Section X".
# After each 'a', there will be a 'br' followed by the professor's name.
def professors( course ):
    result = {}
    quarters = ['fall', 'winter', 'spring', 'summer']
    for quarter, listing in zip(quarters, course.find_next('tr').find_all('td')):
        result[quarter] = { a.contents[0]: a.next_sibling.next_sibling.strip()
                            for a in listing.find_all('a')
                            if listing.get('class') and len(listing.get('class') ) == 1 }
    return result

# For now we just manually download a single course page,
# rename it to ucsc.html, and test with it
# Future plan is to take a list of filenames in
# argv, parse each file and dump into same csv
parse_classes( open('cmps') )
