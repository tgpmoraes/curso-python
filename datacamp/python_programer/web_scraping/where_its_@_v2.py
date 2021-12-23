from scrapy import Selector


html = '''
<html>
  <body>
    <div id="div1" class="class-1">
      <p class="class-1 class-2">Hello World!</p>
      <div id="div2">
        <p id="p2" class="class-2">Choose
            <a href="http://datacamp.com">DataCamp!</a>!
        </p>
      </div>
    </div>
    <div id="div3" class="class-2">
      <p class="class-2">Thanks for Watching!</p>
    </div>
  </body>
</html>
'''


def print_attribute(xpath):
    sel = Selector(text=html)
    print("You have selected:")
    for i, el in enumerate(sel.xpath(xpath).extract()):
        print("%d) %s" % (i+1, el))


# Create an xpath to the href attribute
xpath = '//p[@id="p2"]/a/@href'

# Print out the selection(s); there should be only one
print_attribute(xpath)
