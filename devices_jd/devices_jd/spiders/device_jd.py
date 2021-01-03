# -*- coding: utf-8 -*-
import scrapy
from devices_jd.items import DevicesJdItem
import time

class DeviceJdSpider(scrapy.Spider):
    name = 'device_jd'
    allowed_domains = ['www.jd.com']
    url = 'https://search.jd.com/Search/s_new.php?keyword={keyword}&qrst=1&suggest=1.def.0.base&wq={keyword}&ev=exbrand_%E5%8D%8E%E4%B8%BA%EF%BC%88HUAWEI%EF%BC%89%5E&page={page}&s={s}&scrolling=y&log_id={time}&tpl=3_M&isList=0'
    keyword = iter([
        '手机',
        '智能设备',
        '电脑',
        '游戏设备',
        '外设产品',
        '网络产品',
        '办公设备',
        '智能家居',
        '生活电器',
        '电视',
        '空调',
        '洗衣机',
        '冰箱',
        '厨卫'
    ])
    
    def start_requests(self):
        for key in self.keyword:
            import time
            ti = time.time()
            keyword, page, s, time = next(self.keyword), 1, 1, '%.4f'%(ti*1000)
            urls = self.url.format(keyword=key, page=page, s=s, time=time)
            # print("搜索了" + keyword + "了哟！")
            yield scrapy.Request(url=urls, dont_filter=True, meta={'keyword' : keyword, 'page' : 1, 's' : 1})

    def parse(self, response):
        # 爬取当前页面每个商品的url
        producturls=response.selector.xpath('//div[@class="p-name p-name-type-2"]/a/@href').getall()
        for producturl in producturls:
            producturl = response.urljoin(producturl)
            yield scrapy.Request(url=producturl, callback=self.senditem, dont_filter=True) 
        page = response.meta['page'] + 1
        if response.meta['page'] <= 200:
            import time
            ti = time.time()
            keyword, s, time = response.meta['keyword'], response.meta['s']+28, '%.4f'%(ti*1000)
            urls = self.url.format(keyword=keyword, page=page, s=s, time=time)
            yield scrapy.Request(url=urls, callback=self.parse, dont_filter=True, meta={'keyword' : keyword, 'page' : page, 's' : s})
    
    def senditem(self, response):
        producttype = response.xpath('//div[@class="item"]/a/text()').extract()[0]
        brand = response.xpath('//ul[@id="parameter-brand"]/li/a/text()').extract()[0]
        product = response.xpath('//ul[@class="parameter2 p-parameter-list"]/li/text()').extract()
        productname = product[0][5:]
        productid = product[1][5:]
        item = DevicesJdItem()
        item['producttype'],item['brand'],item['productname'],item['productid'] = producttype,brand,productname,productid
        # print('类型：' + producttype)
        # print('品牌：' + brand)
        # print('名称：' + productname)
        # print('编号：' + productid)
        try:
            modlenumber = response.xpath('//dl[@class="clearfix"]/dd/text()').extract()[3]
            item['modlenumber'] = modlenumber
            # print('型号：' + modlenumber)
        except Exception as e:
            print(e)
            item['modlenumber'] = ''
        yield item
