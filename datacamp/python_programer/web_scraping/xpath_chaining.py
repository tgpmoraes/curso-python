from scrapy import Selector


html = '\n<html>\n<body>\n<div>HELLO</div>\n<div><p>GOODBYE</p></div>\n<div><span><p>NOPE</p><p>ALMOST</p><p>YOU GOT IT!</p></span></div>\n</body>\n</html>\n'

sel = Selector(text=html)

# Chain together xpath methods to select desired p element
sel.xpath('//div').xpath('./span/p[3]')
