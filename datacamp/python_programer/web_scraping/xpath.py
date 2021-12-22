from scrapy import Selector


def whats_my_class(html, xpath):
    sel = Selector(text=html)
    try:
        print("The element from the path={} is:".format(xpath),
              sel.xpath(xpath).extract())
    except:
        print("No second element from path={}found!".format(xpath))


html = '''
<html>
  <body>
    <div>
      <p>Good Luck!</p>
      <p>Not here...</p>
    </div>
    <div>
      <p>Where am I?</p>
    </div>
  </body>
</html>
'''

# Fill in the blank
xpath = '/html/body/div[2]/p'
whats_my_class(html, xpath)

# Fill in the blank
xpath = '//p'
whats_my_class(html, xpath)

# Fill in the blank
xpath = '//span[@class="span-class"]'
whats_my_class(html, xpath)
