# Scrapy settings for devices project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'devices_jd'

SPIDER_MODULES = ['devices_jd.spiders']
NEWSPIDER_MODULE = 'devices_jd.spiders'


PROXY_URL = 'http://127.0.0.1:5000/proxy'

DOWNLOADER_MIDDLEWARES = {
  # 'devices_jd.middlewares.ProxyMiddleware': 543,
  'scrapy.downloadermiddleware.httpproxy.HttpProxyMiddleware': None
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'devices (+http://www.yourdomain.com)'
# USER_AGENTS = [
#     "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
#     "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
#     "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
#     "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
#     "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
#     "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
#     "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
#     "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
#     "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
#     "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
#     "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
#     "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
# ]

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1000

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# # 这里使用的代理IP，因为IP的存活期的限制，请定期更新下面的IP，可从https://www.kuaidaili.com/free/中找免费的代理IP
# PROXIES = [
#     '103.115.14.43',
#     '163.172.47.182',
#     '103.115.14.156',
#     '103.115.14.41',
#     '103.115.14.153',
#     '103.115.14.158',
# ]

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
  'Referer':'https://www.jd.com/',
  'COOKIE' : '__jdu=252503100; areaId=6; ipLoc-djd=6-303-36780-0; shshshfpa=77625852-4b03-606f-4d6f-eb974d199159-1608953520; shshshfpb=lAql4MJm9ZLMbEbPADBP78Q%3D%3D; user-key=7df32024-4870-4cb2-bed0-00476a3db800; PCSYCityID=CN_140000_140100_140105; pinId=JufNJ4gLn2H9zxtqkn3CX7V9-x-f3wj7; pin=jd_79d284d833bea; unick=jd_150253yht; _tp=jNZp8%2B2dFFEwQ1uH9YgoFovnYFj%2FpG1UVbBl3Fx7lfo%3D; _pst=jd_79d284d833bea; unpl=V2_ZzNtbUNURREgARFcLh1UDWIGQV1KV0tCdgtOXX4QVFJkBUBeclRCFnUUR1RnGF4UZwIZX0JcQRNFCEdkeB5fA2AFEFlBZxBFLV0CFi9JH1c%2bbRFdQlREHXMIRlN4HWw1ZAMiXUNnQBF2DEdWexhdNVcEIm1yX0MQcA9FZHopXTUlV05bSl9FEzgLQld%2fGF4FZgIiXHJU; TrackID=1mmlRXwj6xd_LP7JBmeztwkx_YIL2RdlK8BOLhDPiyvVyETG1BO1ykWKtw38zZ6SMGBY42O4xld8RM04oFk2NAHUCRu8zbQ0iNKiHqDWJmwndJdPhuaX_iv0FXYcWQRth; thor=D34F9C7C2E75A90F23CEEA00B1E588B72F8B919DA0EFB2C7BBB83F7B790363820B1F61F54691A3D7C907DA9F526F3DE1ABCDBE6AAD4505A49C6D9EF81FDD07C31B47475A55BE03D58D71C355E8D812F6B72B2E11DA130B130F09177CD3B1CB74EA92368749B49B99B949F6504BEA62D3D8959922A75D32A79B25E138234B5FC3ADF54C68916262289422358CC3CEB6A8C8D01AEF6177A54235E6359C9735E11F; ceshi3.com=103; __jdv=76161171|baidu-search|t_262767352_baidusearch|cpc|211269711625_0_0275d8f9d59944b1919f2298489f27c2|1609641124775; cn=1; __jda=122270672.252503100.1608953515.1609611159.1609641099.16; __jdc=122270672; shshshfp=a348f9ff1c23a5b17eb2f34d8fd715d5; shshshsID=72b00c39a62666e721e4ccc7b296131f_4_1609641159933; __jdb=122270672.7.252503100|16.1609641099; 3AB9D23F7A4B3C9B=3FZE5JLH4UNCQ2IWHLMRB57XHN44NXZZ54XHKA22NA6CGCMLVLKSMSCHVMCZEHOHF3TDGN7GOYHA7QBZP2MYDVO7GE'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
# #    'devices_jd.middlewares.DevicesJDSpiderMiddleware': 543,
#    'devices_jd.middlewares.ProxyMiddleware' : 125,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'devices.middlewares.DevicesDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'devices_jd.pipelines.DevicesJDPipeline': 300,
}
# DOWNLOADER_MIDDLEWARES = {
#     'devices_jd.middlewares.RandomUserAgent': 1,
#     'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
#     'devices_jd.middlewares.ProxyMiddleware': 100,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# # 是否开启重试
# RETRY_ENABLED:True
# # 重试次数
# RETRY_TIMES:5

