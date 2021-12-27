from scrapy.http.response.text import TextResponse
import html_secret_v2


html = html_secret_v2.html

response = TextResponse(url='https://www.datacamp.com/courses/all',
                        status=200,
                        encoding='utf-8',
                        body=html)

mystery = response.xpath('//body')

# Calculate the number of children of the mystery element
how_many_kids = len(mystery.xpath('./*'))

# Print out the number
print("The number of elements you selected was:", how_many_kids)
