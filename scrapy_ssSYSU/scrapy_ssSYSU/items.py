# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapySssysuItem(scrapy.Item):
    
    # define the fields for your item here like:
    newCatalog = scrapy.Field()
    newTitle = scrapy.Field()
    newContent = scrapy.Field()
    newHref = scrapy.Field()
    newTime = scrapy.Field() 
    pass
