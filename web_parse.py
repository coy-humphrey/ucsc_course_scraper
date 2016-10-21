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

def course_name( course ):
    return course.find_next('a').contents[0]

def professors( course ):
    result = {}
    quarters = ['fall', 'winter', 'spring', 'summer']
    for quarter, listing in zip(quarters, course.find_next('tr').find_all('td')):
        result[quarter] = { a.contents[0]: a.next_sibling.next_sibling.strip()
                            for a in listing.find_all('a')
                            if listing.get('class') and len(listing.get('class') ) == 1 }
    return result
    # return { a.contents[0]:  a.next_sibling.next_sibling.strip() 
    #          for td in course.find_next('tr').find_all('td')
    #          for a in td.find_all('a')
    #          if td.get('class') and len( td.get('class') ) == 1 }

# For now we just download a single course page,
# rename it to ucsc.html, and test with it
# Future plan is to take a list of filenames in
# argv, parse each file and dump into same csv
parse_classes( open('cmps') )
