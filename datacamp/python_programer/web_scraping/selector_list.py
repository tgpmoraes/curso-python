from scrapy import Selector


html = '\n<html>\n<body>\n<div>Div 1: <p>paragraph 1</p></div>\n<div>Div 2: <p>paragraph 2</p> <p>paragraph 3</p> </div>\n<div>Div 3: <p>paragraph 4</p> <p>paragraph 5</p> <p>paragraph 6</p></div>\n<div>Div 4: <p>paragraph 7</p></div>\n<div>Div 5: <p>paragraph 8</p></div>\n</body>\n</html>\n'

# Create a Selector selecting html as the HTML document
sel = Selector(text=html)

# Create a SelectorList of all div elements in the HTML document
divs = sel.xpath('//div')
