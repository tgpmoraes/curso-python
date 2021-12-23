from scrapy import Selector
import os


curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\python_programer\\web_scraping'
os.chdir(data_dir)

# Open pickle file and load data: d
with open('all.html', 'rb') as file:
    html = file.read()


def how_many_elements(xpath):
    sel = Selector(text=html)
    print(len(sel.xpath(xpath)))


# Create an XPath string to direct to children of body element
xpath = '/html/body/*'

# Print out the number of elements selected
how_many_elements(xpath)
