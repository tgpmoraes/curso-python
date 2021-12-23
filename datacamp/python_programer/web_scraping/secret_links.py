from scrapy import Selector
import html_secret


html = html_secret.html

sel = Selector(text=html)


def how_many_elements(xpath):
    print("You've selected %d elements" % len(sel.xpath(xpath)))


def preview(xpath):
    els = sel.xpath(xpath).extract()
    n = len(els)
    for i, el in enumerate(els[:min(4, n)]):
        print("Element %d: %s" % (i+1, el))


# Create an xpath to the href attributes
xpath = '//a[contains(@class,"package-snippet")]/@href'

# Print out how many elements are selected
how_many_elements(xpath)
# Preview the selected elements
preview(xpath)
