# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DevicesJdItem(scrapy.Item):
    # define the fields for your item here like:
    productid = scrapy.Field()
    productname = scrapy.Field()
    brand = scrapy.Field()
    modlenumber = scrapy.Field()
    producttype = scrapy.Field()
    
