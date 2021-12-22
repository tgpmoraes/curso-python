from scrapy import Selector


def whats_my_class(html):
    sel = Selector(text=html)
    try:
        print("The class you assigned to the second div element is:",
              sel.xpath('//div')[1].xpath('./@class')[0].extract())
    except:
        print("No second div element class found!")


# HTML code string
html = '''
<html>
  <body>
    <div class="class1" id="div1">
      <p class="class2">Visit DataCamp!</p>
    </div>
    <div class="you-are-classy">
      <p class="class2">Keep up the good work!</p>
    </div>
  </body>
</html>
'''
# Print out the class of the second div element
whats_my_class(html)
