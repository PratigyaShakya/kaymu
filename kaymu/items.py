# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KaymuItem(scrapy.Item):
    title = scrapy.Field()
    cost = scrapy.Field()
    product_location = scrapy.Field()
    seller = scrapy.Field()
    avg_rating_tot_reviews = scrapy.Field()
    age_group = scrapy.Field()
    gender = scrapy.Field()
    brand = scrapy.Field()
    material = scrapy.Field()
    weight = scrapy.Field()
    condition = scrapy.Field()
    occasion = scrapy.Field()
    stiched_unstiched = scrapy.Field()
    url = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
