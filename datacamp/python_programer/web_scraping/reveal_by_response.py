from scrapy.http.response.text import TextResponse
import html_secret_v2


html = html_secret_v2.html

response = TextResponse(url='https://www.datacamp.com/courses/all',
                        status=200,
                        encoding='utf-8',
                        body=html)


def print_url_title(url, title):
    print("Here is what you found:")
    print("\t-URL: %s" % url)
    print("\t-Title: %s" % title)


# Get the URL to the website loaded in response
this_url = response.url

# Get the title of the website loaded in response
this_title = response.xpath('//title/text()').extract_first()

# Print out our findings
print_url_title(this_url, this_title)
