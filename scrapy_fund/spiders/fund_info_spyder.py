# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 17:32:50 2018

@author: xuexianju
"""
import scrapy
from items import FundInfoItems

class FundSpider(scrapy.Spider):
    name = 'fundInfoSpider'
    # start_urls = ['http://fund.eastmoney.com/000007.html']
    start_urls = ['http://fund.eastmoney.com/allfund.html']

    def parse(self, response):
        fund_info_list = response.css(".num_right>li>div")
        # f=open("/Users/user/Desktop/fund_info","w+")
        for fund in fund_info_list:
            # print(fund.css("a::attr(href)").extract_first())
            fund_detail_url = fund.css("a::attr(href)").extract_first()
            yield scrapy.Request(fund_detail_url,
                                 callback=self.pares_fund_detail)

    # def parse(self, response):
    #     start_urls = ['http://fund.eastmoney.com/000007.html']
    #     for url in start_urls:
    #         yield scrapy.Request(url=url, callback=self.pares_fund_detail)

    def pares_fund_detail(self, response):
        fundInfoItem = FundInfoItems()
        # 基金id和基金名称
        fundInfoItem['fund_id'] = response.css(".fundDetail-tit div span[class='ui-num']::text").extract_first()
        fundInfoItem['name'] = response.css(".fundDetail-tit div::text").extract_first()

        # 估值、净值、累计净值和6项增长率
        if len(response.css("div .dataOfFund"))==1:
            valueItems = response.css("div .dataOfFund")[0].css("dl dd span[class~='ui-num']::text").extract()
            fundInfoItem['estimate_value'] = valueItems[0]
            fundInfoItem['unit_value'] = valueItems[5]
            fundInfoItem['cumulative_value'] = valueItems[9]
            fundInfoItem['last_month'] = valueItems[3]
            fundInfoItem['last_3_month'] = valueItems[7]
            fundInfoItem['last_half_year'] = valueItems[10]
            fundInfoItem['last_year'] = valueItems[4]
            fundInfoItem['last_3_yesr'] = valueItems[8]
            fundInfoItem['set_up'] = valueItems[-1]
        else:
            valueItems = response.css("div .dataOfFund")[0].css("dl dd span[class~='ui-num']::text").extract()
            valueItems2 = response.css("div .dataOfFund")[1].css("dl dd span[class~='ui-num']::text").extract()
            fundInfoItem['estimate_value'] = valueItems[0]
            fundInfoItem['unit_value'] = valueItems[1]
            fundInfoItem['cumulative_value'] = valueItems[2]

            fundInfoItem['last_month'] = valueItems2[0]
            fundInfoItem['last_3_month'] = valueItems2[2]
            fundInfoItem['last_half_year'] = valueItems2[4]
            fundInfoItem['last_year'] = valueItems2[1]
            fundInfoItem['last_3_yesr'] = valueItems2[3]
            fundInfoItem['set_up'] = valueItems2[5]

        # 基金类型、规模、经理、成立日期等
        infoOfFund = response.css(".infoOfFund td")
        # 基金类型
        if len(infoOfFund[0].css("::text")) > 1:
            fundInfoItem['type'] = infoOfFund[0].css("::text")[1].extract()
        else:
            fundInfoItem['type'] = infoOfFund[0].css("::text")[0].extract().encode("utf-8").replace("基金类型：", "").split("|")[0].strip()
        fundInfoItem['scale'] = infoOfFund[1].css("::text").extract()[1].encode("utf-8").split("亿")[0].replace("：", "")
        if len(infoOfFund[2].css("::text").extract()) > 1:
            fundInfoItem['manager'] = infoOfFund[2].css("::text").extract()[1]
        else:
            fundInfoItem['manager'] = ''
        fundInfoItem['setup_date'] = infoOfFund[3].css("::text").extract()[1].encode("utf-8").split('：')[1]
        fundInfoItem['admin'] = infoOfFund[4].css("a::text").extract_first()
        fundInfoItem['grade'] = infoOfFund[5].css("div::attr(class)").extract_first()
        # 基金状态
        staticItems = response.css("div .staticItem")[0].css(".staticCell::text").extract()
        if len(staticItems) > 1:
            fundInfoItem['trade_first_status'] = staticItems[0]
            fundInfoItem['trade_sencond_status'] = staticItems[1]
        else:
            fundInfoItem['trade_first_status'] = staticItems[0]
            fundInfoItem['trade_sencond_status'] = staticItems[0]

        # 基金手续费
        fundInfoItem['fee'] = response.css("div .staticItem")[3].css(".nowPrice::text").extract()
        yield fundInfoItem



