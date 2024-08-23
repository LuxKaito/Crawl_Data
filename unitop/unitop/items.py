# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class UnitopItem(scrapy.Item):
    coursename = scrapy.Field()
    lecturer = scrapy.Field()
    intro = scrapy.Field()
    describe = scrapy.Field()
    courseUrl = scrapy.Field()
    votenumber = scrapy.Field() # add new
    rating = scrapy.Field() # add new
    newfee = scrapy.Field() # add new
    oldfee = scrapy.Field() # add new
    lessonnum = scrapy.Field() # add new

