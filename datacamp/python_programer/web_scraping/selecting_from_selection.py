from scrapy.http.response.text import TextResponse
import html_secret_v2


html = html_secret_v2.html

response = TextResponse(url='https://www.datacamp.com/courses/all',
                        status=200,
                        encoding='utf-8',
                        body=html)

# Select all desired div elements
divs = response.css('div.course-block')

# Take the first div element
first_div = divs[0]

# Extract the text from the (only) h4 element in first_div
h4_text = first_div.css('h4::text').extract_first()

# Print out the text
print("The text from the h4 element is:", h4_text)
