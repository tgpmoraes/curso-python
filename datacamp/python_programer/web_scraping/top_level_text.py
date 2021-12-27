from scrapy.http.response.text import TextResponse


html = ('\n<html>\n<body>\n<div id="this-div">\n<p id="p1" class="class-1">'
        'This is not the element you are looking for</p>\n<p id="p2" '
        'class="class-12">\n<a href="https://www.google.com">Google</a> is '
        'linked to here, but this isn\'t the link you are looking for. '
        '\n</p>\n<p id="p3" class="class-1 class-12">\nHere is the '
        '<a href="https://www.datacamp.com" id="a-exercise">DataCamp</a> '
        'link you want!\n</p>\n</div>\n</body>\n</html>\n')


res = TextResponse(url='http://www.datacamp.com',
                   status=200,
                   encoding='utf-8',
                   body=html)


def our_xpath(xpath):
    xextr = res.xpath(xpath).extract()
    return xextr


def our_css(css):
    cextr = res.css(css).extract()
    return cextr


def print_results(xpath, css_locator):
    print("Your XPath extracts to following:")
    print(our_xpath(xpath))
    print("_________________\n")
    print("Your CSS Locator extracts the following:")
    print(our_css(css_locator))
    return None


# Create an XPath string to the desired text.
xpath = '//p[@id="p3"]/text()'

# Create a CSS Locator string to the desired text.
css_locator = 'p#p3::text'

# Print the text from our selections
print_results(xpath, css_locator)
