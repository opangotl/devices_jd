# # -*- coding: utf-8 -*-

# # Define here the models for your spider middleware
# #
# # See documentation in:
# # https://docs.scrapy.org/en/latest/topics/spider-middleware.html

# from scrapy import signals
# from .settings import USER_AGENTS, PROXIES
# import json
# import requests
# import logging
# import random

# class ProxyMiddleware(object):
#     def __init__(self, proxy_url):
#         self.logger = logging.getLogger(__name__)
#         self.proxy_urls = proxy_url
#         self.proxy_url = random.choice(self.proxy_urls)

#     def get_proxy(self):
#         return requests.get("http://127.0.0.1:5010/get/")

#     def delete_proxy(self, proxy):
#         requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))

#     def get_random_proxy(self, request, spider):
#         # useragent = random.choice(USER_AGENTS)                  #随机选择一个代理
#         # request.headers.setdefault("User-Agent",useragent)      #代理

#         retry_count = 3
#         proxy = self.get_proxy().json().get("proxy")
#         print(proxy)
#         while retry_count > 0:
#             try:
#                 html = requests.get('http://www.baidu.com', proxies={"http": "http://{}".format(proxy)})
#                 # 使用代理访问
#                 if html.status_code == 200:
#                     return proxy
#             except Exception:
#                 retry_count -= 1
#         return self.get_random_proxy(request, spider)

#     def process_request(self, request, spider):
#             proxy = self.get_random_proxy(request, spider)
#             if proxy:
#                 self.logger.debug('======' + '使用代理 ' + str(proxy) + "======")
#                 request.meta['proxy'] = 'https://{proxy}'.format(proxy=proxy)

#     def process_response(self, request, response, spider):
#         if response.status != 200:
#             print("again response ip:")
#             request.meta['proxy'] = 'https://{proxy}'.format(proxy=self.get_random_proxy(request, spider))
#             return request
#         return response

#     @classmethod
#     def from_crawler(cls, crawler):
#         settings = crawler.settings
#         return cls(
#             proxy_url=settings.get('PROXIES')
#         )

# # # 主要用来动态获取user agent, user agent列表USER_AGENTS在setting.py中进行配置
# # class RandomUserAgent(object):
# #     """Randomly rotate user agents based on a list of predefined ones"""

# #     def __init__(self, agents):
# #         self.agents = agents

# #     @classmethod
# #     def from_crawler(cls, crawler):
# #         return cls(crawler.settings.getlist('USER_AGENTS'))

# #     def process_request(self, request, spider):
# #         #print "**************************" + random.choice(self.agents)
# #         request.headers.setdefault('User-Agent', random.choice(self.agents))


# # # 用来切换代理，proxy列表PROXIES也是在settings.py中进行配置
# # class ProxyMiddleware(object):
# #     def process_request(self, request, spider):
# #         proxy = random.choice(PROXIES)
# #         if proxy['user_pass'] is not None:
# #             request.meta['proxy'] = "http://%s" % proxy['ip_port']
# #             encoded_user_pass = base64.encodestring(proxy['user_pass'])
# #             request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
# #             print ("**************ProxyMiddleware have pass************" + proxy['ip_port'])
# #         else:
# #             print ("**************ProxyMiddleware no pass************" + proxy['ip_port'])
# #             request.meta['proxy'] = "http://%s" % proxy['ip_port']

# class DevicesJdSpiderMiddleware:
#     # Not all methods need to be defined. If a method is not defined,
#     # scrapy acts as if the spider middleware does not modify the
#     # passed objects.

#     @classmethod
#     def from_crawler(cls, crawler):
#         # This method is used by Scrapy to create your spiders.
#         s = cls()
#         crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
#         return s

#     def process_spider_input(self, response, spider):
#         # Called for each response that goes through the spider
#         # middleware and into the spider.

#         # Should return None or raise an exception.
#         return None

#     def process_spider_output(self, response, result, spider):
#         # Called with the results returned from the Spider, after
#         # it has processed the response.

#         # Must return an iterable of Request, dict or Item objects.
#         for i in result:
#             yield i

#     def process_spider_exception(self, response, exception, spider):
#         # Called when a spider or process_spider_input() method
#         # (from other spider middleware) raises an exception.

#         # Should return either None or an iterable of Request, dict
#         # or Item objects.
#         pass

#     def process_start_requests(self, start_requests, spider):
#         # Called with the start requests of the spider, and works
#         # similarly to the process_spider_output() method, except
#         # that it doesn’t have a response associated.

#         # Must return only requests (not items).
#         for r in start_requests:
#             yield r

#     def spider_opened(self, spider):
#         spider.logger.info('Spider opened: %s' % spider.name)


# class DevicesJdDownloaderMiddleware:
#     # Not all methods need to be defined. If a method is not defined,
#     # scrapy acts as if the downloader middleware does not modify the
#     # passed objects.

#     @classmethod
#     def from_crawler(cls, crawler):
#         # This method is used by Scrapy to create your spiders.
#         s = cls()
#         crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
#         return s

#     def process_request(self, request, spider):
#         # Called for each request that goes through the downloader
#         # middleware.

#         # Must either:
#         # - return None: continue processing this request
#         # - or return a Response object
#         # - or return a Request object
#         # - or raise IgnoreRequest: process_exception() methods of
#         #   installed downloader middleware will be called
#         return None

#     def process_response(self, request, response, spider):
#         # Called with the response returned from the downloader.

#         # Must either;
#         # - return a Response object
#         # - return a Request object
#         # - or raise IgnoreRequest
#         return response

#     def process_exception(self, request, exception, spider):
#         # Called when a download handler or a process_request()
#         # (from other downloader middleware) raises an exception.

#         # Must either:
#         # - return None: continue processing this exception
#         # - return a Response object: stops process_exception() chain
#         # - return a Request object: stops process_exception() chain
#         pass

#     def spider_opened(self, spider):
#         spider.logger.info('Spider opened: %s' % spider.name)
