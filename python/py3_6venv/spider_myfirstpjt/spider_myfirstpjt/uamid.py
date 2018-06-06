# Author: Jason Lu
import random
from spider_myfirstpjt.settings import UAPOOL
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware

class Uamid(UserAgentMiddleware):
    def __init__(self, ua=''):
        self.ua = ua

    def process_request(self, request, spider):
        thisua = random.choice(UAPOOL)
        print("当前使用user-agent是：" + thisua)
        request.headers.setdefault('User-Agent', thisua)