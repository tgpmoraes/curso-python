from scrapy import Selector


html = '''
<html>
  <body>
    <div id="div1" class="class-1">
      <p class="class-1 class-2">Hello World!</p>
      <div id="div2">
        <p id="p2" class="class-2">Choose DataCamp!</p>
      </div>
    </div>
    <div id="div3" class="class-2">
      <p class="class-2">Thanks for Watching!</p>
    </div>
  </body>
</html>
'''


def print_element_text(xpath):
    sel = Selector(text=html)
    text = ' '.join(sel.xpath(xpath).xpath('./text()').extract())
    print(text)


# Create an Xpath string to select desired p element
xpath = '//*[@id="div3"]/p'

# Print out selection text
print_element_text(xpath)

# Create an XPath string to select p element by class
xpath = '//p[@class="class-1 class-2"]'

# Print out select text
print_element_text(xpath)
