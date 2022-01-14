from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()
    # print(content)

    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())

    # finding teh first occurance of the tag
    # tags = soup.find('h5')

    # finding all occurance of the tag
    # course_html_tags = soup.find_all('h5')

    # printing txt fron the html grabbed
    # for course in course_html_tags:
        # print(course.text)

    # getting the prices for the courses 
    course_cards = soup.find_all('div', class_='card')
    for course in course_cards:
        coursenm = course.h5.text 
        coursepr = course.a.text.split()[-1]

        print(f'{coursenm} price is {coursepr}')