from scrapy.http.response.text import TextResponse
import html_secret_v2


html = html_secret_v2.html

response = TextResponse(url='https://www.datacamp.com/courses/all',
                        status=200,
                        encoding='utf-8',
                        body=html)

# Create a SelectorList of the course titles
crs_title_els = response.css('div.course-block__body')

# Extract the course titles
crs_titles = crs_title_els.css('h4::text').extract()

# Print out the course titles
for el in crs_titles:
    print(">>", el)
