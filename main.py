# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 17:32:50 2018

@author: xuexianju
"""

import scrapy.cmdline
import pandas as pd
import constants
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def get_first_arg(*args):
    return args[0]


if __name__ == '__main__':
    # scrapy.cmdline.execute(argv=['scrapy','crawl','fundInfoSpider'])

    # Fund Value
    process = CrawlerProcess(get_project_settings())
    process.crawl('fundValueSpider')
    process.start()
    fund_value = pd.read_csv(constants.OUTPUT_FILE_PATH)
    fund_value.to_csv(constants.FUND_VALUE)
    #Fund Info
    process.crawl('fundInfoSpider')
    fund_info = pd.read_csv(constants.OUTPUT_FILE_PATH)
    fund_info.to_csv(constants.FUND_INFO)

