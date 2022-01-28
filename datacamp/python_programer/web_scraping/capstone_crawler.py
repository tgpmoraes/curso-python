# Import scrapy
import scrapy

# Import the CrawlerProcess: for running the spider
from scrapy.crawler import CrawlerProcess

url_short = '''https://assets.datacamp.com/production/repositories/2560/
datasets/19a0a26daa8d9db1d920b5d5607c19d6d8094b3b/all_short'''


def previewCourses(dc_dict, n=3):
    crs_titles = list(dc_dict.keys())
    print("A preview of DataCamp Courses:")
    print("---------------------------------------\n")
    for t in crs_titles[:n]:
        print("TITLE: %s" % t)
        for i, ct in enumerate(dc_dict[t]):
            print("\tChapter %d: %s" % (i+1, ct))
        print("")

# Create the Spider class


class YourSpider(scrapy.Spider):
    name = 'yourspider'
    # start_requests method

    def start_requests(self):
        yield scrapy.Request(url=url_short, callback=self.parse)

    def parse(self, response):
        # My version of the parser you wrote in the previous part
        crs_titles = response.xpath(
            '//h4[contains(@class,"block__title")]/text()').extract()
        crs_descrs = response.xpath(
            '//p[contains(@class,"block__description")]/text()').extract()
        for crs_title, crs_descr in zip(crs_titles, crs_descrs):
            dc_dict[crs_title] = crs_descr


# Initialize the dictionary **outside** of the Spider class
dc_dict = dict()

# Run the Spider
process = CrawlerProcess()
process.crawl(YourSpider)
process.start()

# Print a preview of courses
previewCourses(dc_dict)
