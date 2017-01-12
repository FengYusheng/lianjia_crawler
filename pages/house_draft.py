# -*-coding: utf-8-*-

import re

house = {}
re1 = r'<li class="clear">.*?</li>'
re_link = r'<a class="img " href="(http://bj.lianjia.com/ershoufang/\d+\.html)" target="_blank"'
pattern = re.compile(re1, flags=re.S|re.M|re.L)
link_pattern = re.compile(re_link, flags=re.S|re.M|re.L)

re_info = r'<div class="houseInfo">.*?data-el="region">(.+?)</a> \| (.+?) \| (\d+).+? \|.*?</div>'
info_pattern = re.compile(re_info, re.S|re.M|re.L)

re_subway = r'<span class="subway">距离(\d+号线)(.+?)站(\d+)米</span>'
subway_pattern = re.compile(re_subway, re.S|re.M|re.L)

re_total = r'<div class="totalPrice"><span>(\d+)'
total_pattern = re.compile(re_total, re.S|re.M|re.L)

re_unit = r'<span>单价(\d+)'
unit_pattern = re.compile(re_unit, re.S|re.M|re.L)

re_follow = r'<span class="starIcon"></span>\d+人关注 / 共(\d+)'
follow_pattern = re.compile(re_follow, re.S|re.M|re.L)

with open('crawler\\pages\\pg6.html', 'r', encoding='utf-8') as f:
    content = f.read()
    i = 0
    for m in re.finditer(pattern, content):
        # print(m.group(0).encode('utf-8'))
        # ret = re.search(link_pattern, m.group(0))
        # house['link'] = ret.group(1)

        ret = re.search(info_pattern, m.group(0))
        house['block'] = ret.group(1)
        house['layout'] = ret.group(2)
        house['area'] = ret.group(3)

        ret = re.search(subway_pattern, m.group(0))
        house['line'] = ret.group(1)
        house['station'] = ret.group(2)
        house['distance'] = ret.group(3)

        ret = re.search(total_pattern, m.group(0))
        house['total'] = ret.group(1)

        ret = re.search(unit_pattern, m.group(0))
        house['unit'] = ret.group(1)

        ret = re.search(follow_pattern, m.group(0))
        house['follow'] = ret.group(1)

        with open('crawler\\a.txt', 'w', encoding='utf-8') as f:
            f.write(house['follow'] + '\n')
