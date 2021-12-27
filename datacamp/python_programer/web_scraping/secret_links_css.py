from scrapy import Selector
import html_secret_v2


html = html_secret_v2.html

sel = Selector(text=html)


def how_many_elements(css):
    print(len(sel.css(css)))


# Fill in the blank
css_locator = '.course-block > a'

# Print the number of selected elements.
how_many_elements(css_locator)
