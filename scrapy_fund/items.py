# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
class FundInfoItems(scrapy.Item):
    # define the fields for your item here like:
    fund_id=scrapy.Field()
    name= scrapy.Field()
    name= scrapy.Field()
    estimate_value=scrapy.Field()
    unit_value=scrapy.Field()
    cumulative_value= scrapy.Field()
    last_month= scrapy.Field()
    last_3_month= scrapy.Field()
    last_half_year= scrapy.Field()
    last_year= scrapy.Field()
    last_3_yesr= scrapy.Field()
    set_up= scrapy.Field()
    type= scrapy.Field()
    scale= scrapy.Field()
    manager= scrapy.Field()
    setup_date= scrapy.Field()
    admin= scrapy.Field()
    grade= scrapy.Field()
    trade_first_status= scrapy.Field()
    trade_sencond_status= scrapy.Field()
    fee = scrapy.Field()
    pass
class FundValueItems(scrapy.Item):
    fund_id=scrapy.Field()
    name=scrapy.Field()
    netvalue_date=scrapy.Field()
    netvalue=scrapy.Field()
    cumulativevalue=scrapy.Field()
    daily_growth_rate=scrapy.Field()
    apply_status=scrapy.Field()
    redeem_status=scrapy.Field()
    bonus=scrapy.Field()
    pass
