# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Dogtopia1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    StoreID = scrapy.Field()
    StoreName = scrapy.Field()
    # Description = scrapy.Field()
    Street = scrapy.Field()
    City = scrapy.Field()
    State = scrapy.Field()
    StoreTiminings = scrapy.Field()
    Phone = scrapy.Field()
    Fax = scrapy.Field()
    Email = scrapy.Field()
    URL = scrapy.Field()
    Latitude = scrapy.Field()
    Longitude = scrapy.Field()

