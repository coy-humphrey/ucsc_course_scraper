from bs4 import BeautifulSoup
import urllib2

def parse_classes( html_contents ):
    soup = BeautifulSoup( html_contents, 'html.parser' )
    for course in courses( soup ):
        print course_name( course )
        for p in professors( course ):
            print p

def courses( soup ):
    return soup.find_all('td', class_="course-name")

def course_name( course ):
    return course.find_next('a').contents[0]

def professors( course ):
    return [ p.find_next('br').contents[0].strip() for
             p in course.find_next('tr').find_all('td')
             if p.find_next('br') ]

response = urllib2.urlopen('http://courses.soe.ucsc.edu/courses/cmps')
html = response.read()
htmlfile = open('ucsc.html')
html2 = htmlfile.read()

parse_classes( html )
