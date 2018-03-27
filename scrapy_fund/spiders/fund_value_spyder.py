# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 17:32:50 2018

@author: xuexianju
"""
import scrapy
from items import FundValueItems
from log import get_logger

class FundValueSpider(scrapy.Spider):
    name = 'fundValueSpider'
    #start_urls = ['http://fund.eastmoney.com/000007.html']
    start_urls = ['http://fund.eastmoney.com/allfund.html']
    def parse(self, response):
        fund_info_list=response.css(".b>div")
        for fund in fund_info_list:
            fund_info= fund.css("a::text").extract_first()
            position = '）'.decode('utf8', 'ignore')
            fund_id=fund_info[1:fund_info.index(position)]
            name=fund_info[fund_info.index(position)+1:]
            fund_value_url="http://fund.eastmoney.com/f10/F10DataApi.aspx?type=lsjz&code="+fund_id+"&page=1&per=10"
            yield scrapy.Request(fund_value_url,meta={'fund_id':fund_id,'name':name},
                            callback=self.pares_fund_value_detail)

    def pares_fund_value_detail(self,response):
        fundValueItem=FundValueItems()
        fund_values_trs=response.css("tr")
        for i in range(1,len(fund_values_trs)):
           tds=fund_values_trs[i].css("td")
           if len(tds)==7:
            #print(tds)
            try:
                fundValueItem['fund_id']=response.meta['fund_id']
                fundValueItem['name']=response.meta['name']
                fundValueItem['netvalue_date']=tds[0].css("::text").extract_first()
                fundValueItem['netvalue']=tds[1].css("::text").extract_first()
                fundValueItem['cumulativevalue']=tds[2].css("::text").extract_first()
                fundValueItem['daily_growth_rate']=tds[3].css("::text").extract_first()
                fundValueItem['apply_status']=tds[4].css("::text").extract_first()
                fundValueItem['redeem_status']=tds[5].css("::text").extract_first()
                fundValueItem['bonus']=tds[6].css("::text").extract_first()
                #my_logger = get_logger('fundValueSpider','')
                #my_logger.info('Info logger')
                #my_logger.error('Error logger')
                yield fundValueItem
            except Exception as e:
              my_logger = get_logger('fundValueSpider','')
              my_logger.error(e+"#"+fundValueItem['fund_id'])
           #货币基金
           elif len(tds)==6:
            try:
                fundValueItem['fund_id']=response.meta['fund_id']
                fundValueItem['name']=response.meta['name']
                fundValueItem['netvalue_date']=tds[0].css("::text").extract_first()
                fundValueItem['netvalue']=tds[1].css("::text").extract_first()
                fundValueItem['cumulativevalue']=tds[1].css("::text").extract_first()
                fundValueItem['daily_growth_rate']=tds[2].css("::text").extract_first()
                fundValueItem['apply_status']=tds[3].css("::text").extract_first()
                fundValueItem['redeem_status']=tds[4].css("::text").extract_first()
                fundValueItem['bonus']=tds[5].css("::text").extract_first()
                yield fundValueItem
            except Exception as e:
                my_logger = get_logger('fundValueSpider','')
                my_logger.error(e+"#"+fundValueItem['fund_id'])