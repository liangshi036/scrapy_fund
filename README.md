## Scrapy 爬去基金信息 ##



### 说明： ###

本程序从 [天天基金](http://fund.eastmoney.com/allfund.html) 中爬取了所有的基金信息，主要包括以下两方面：

- 基金基础信息 ：基金名称、基金代码、 基金经理、单位净值、累计净值、近一个月涨幅、近三个月涨幅、近六个月涨幅、近半年涨幅、自成立以来涨幅
- 基金每日净值：净值日期、单位净值、累计净值、日增长率、申购状态、赎回状态、分红送配

### 注意事项: ###

- fund_value_spyder.py中 修改 fund_value_url="http://fund.eastmoney.com/f10/F10DataApi.aspx?type=lsjz&code="+fund_id+"&page=1&per=10" 每页只取了十条记录，可按需增加这个值
- 默认生成的文件utf-8,如果中文乱码，用notepad++将其转码为ascii
