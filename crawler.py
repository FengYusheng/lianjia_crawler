# -*- coding: utf-8 -*-


import urllib.request as Request
import urllib.parse as Parse
import os
import re
import csv

class LianjianCapture(object):
    def __init__(self, count):
        super(LianjianCapture, self).__init__()
        self.count = count
        self.re_list = r'<li class="clear">.*?</li>'
        self.re_link = r'<a class="img " href="(http://bj.lianjia.com/ershoufang/\d+\.html)" target="_blank"'
        self.re_info = r'<div class="houseInfo">.*?data-el="region">(.+?)</a> \| (.+?) \| (\d+).+? \|.*?</div>'
        self.re_subway = r'<span class="subway">距离(\d+号线)(.+?)站(\d+)米</span>'
        self.re_total = r'<div class="totalPrice"><span>(\d+)'
        self.re_unit = r'<span>单价(\d+)'
        self.re_star = r'<span class="starIcon"></span>\d+人关注 / 共(\d+)'

        self.fields = ('链接',
                       '小区',
                       '格局',
                       '面积（平方米）',
                       '地铁线路',
                       '地铁站',
                       '距地铁距离（米）',
                       '总价（万）',
                       '每平米价格（元）',
                       '看房次数')

        with open('crawler\lianjia.csv', 'w', encoding='utf-8', newline='') as f:
            c = csv.DictWriter(f, fieldnames=self.fields)
            c.writeheader()

    def get_house(self):
        house = {}
        for i in range(1, self.count + 1):
            path = 'crawler\\pages\\pg{0}.html'.format(i)
            if not os.path.exists(path):
                continue

            with open(path, 'r', encoding='utf-8') as f:
                page = f.read()
                pattern = re.compile(self.re_list, re.S|re.M|re.L)
                for m in re.finditer(pattern, page):
                    pattern1 = re.compile(self.re_link, re.S|re.M|re.L)
                    ret = re.search(pattern1, m.group(0))
                    house['链接'] = ret.group(1)

                    pattern1 = re.compile(self.re_info, re.S|re.M|re.L)
                    ret = re.search(pattern1, m.group(0))
                    house['小区'] = ret.group(1)
                    house['格局'] = ret.group(2)
                    house['面积（平方米）'] = ret.group(3)

                    pattern1 = re.compile(self.re_subway, re.S|re.M|re.L)
                    ret = re.search(pattern1, m.group(0))
                    house['地铁线路'] = ret.group(1)
                    house['地铁站'] = ret.group(2)
                    house['距地铁距离（米）'] = ret.group(3)

                    pattern1 = re.compile(self.re_total, re.S|re.M|re.L)
                    ret = re.search(pattern1, m.group(0))
                    house['总价（万）'] = ret.group(1)

                    pattern1 = re.compile(self.re_unit, re.S|re.M|re.L)
                    ret = re.search(pattern1, m.group(0))
                    house['每平米价格（元）'] = ret.group(1)

                    pattern1 = re.compile(self.re_star, re.S|re.M|re.L)
                    ret = re.search(pattern1, m.group(0))
                    house['看房次数'] = ret.group(1)

                    with open('crawler\\lianjia.csv', 'a', encoding='utf-8', newline='') as f:
                        c = csv.DictWriter(f, fieldnames=self.fields)
                        c.writerow(house)


class LianjiaRequest(object):
    def __init__(self, count = 1):
        super(LianjiaRequest, self).__init__()
        self.count = count # page count
        self.headers = {
            'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
            'Referer' : 'http://bj.lianjia.com/ditiefang/li648/pg1/'
        }

    def get_url(self):
        for i in range(1, self.count + 1):
            url = 'http://bj.lianjia.com/ditiefang/li648/pg{0}/'.format(i)
            url = Parse.quote_plus(url, ':/?=~_&')
            yield url

    def request(self, url):
        opener = Request.build_opener(Request.HTTPHandler)
        req = Request.Request(url, headers=self.headers)
        response = None
        try:
            response = opener.open(req, timeout=10)
        except Request.URLError as e:
            print('"{0}" ouccurs when requst url {1}.', e.reason, url)

        if response is not None:
            page = response.read().decode('utf-8')
            path = 'crawler\\pages\\' + url.split('/')[-2] + '.html'

            if not os.path.exists('crawler\\pages'):
                os.mkdir('crawler\\pages')

            with open(path, 'w', encoding='utf-8') as f:
                f.write(page)


if __name__ == '__main__':
    # lianjia = LianjiaRequest(47)
    # for url in lianjia.get_url():
    #     lianjia.request(url)

    capture = LianjianCapture(47)
    capture.get_house()
