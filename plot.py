# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import csv

csv_path = 'lianjia2.csv'


with open(csv_path, 'r') as f:
    csv_reader = csv.reader(f)
    l1 = [(r[1], r[8]) for r in csv_reader] # 小区，单价

with open(csv_path, 'r') as f:
    csv_reader = csv.reader(f)
    l2 = [(r[1], r[9]) for r in csv_reader] # 小区, 看房次数

with open(csv_path, 'r') as f:
    csv_reader = csv.reader(f)
    l3 = [(r[1], r[6]) for r in csv_reader] # 小区, 到地铁距离

with open(csv_path, 'r') as f:
    csv_reader = csv.reader(f)
    l4 = [(r[1], r[3]) for r in csv_reader] # 到地铁距离，面积


block_index = [i for i in xrange(1, 51)]
unit = [i[1] for i in l1[0:50]]
star = [i[1] for i in l2[0:50]]
distance = [i[1] for i in l3[0:50]]
area = [i[1] for i in l4[0:50]]

plt.figure(1)
plt.subplot(211)
plt.xlabel('block index')
plt.ylabel('unit')
plt.plot(block_index, unit, 'b')

plt.annotate('MAI HAO SHI DAI({0})'.format(72032), xy=(20, 72032),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )

plt.grid(True)

plt.subplot(212)
plt.xlabel('block index')
plt.ylabel('star')
plt.plot(block_index, star, 'g')

plt.annotate('MAI HAO SHI DAI({0})'.format(168), xy=(20, 168),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )

plt.grid(True)

plt.figure(2)
plt.subplot(211)
plt.xlabel('distance from subway')
plt.ylabel('unit')
plt.plot(distance, unit, 'bo')

plt.annotate('LIU PU KENG ER QU({0})'.format(137436), xy=(445, 137436),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )

plt.grid(True)

plt.subplot(212)
plt.xlabel('distance from subway')
plt.ylabel('area')
plt.plot(distance, area, 'go')

plt.annotate('HE FENG XIANG FU({0})'.format(109932), xy=(329, 163),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )

plt.grid(True)

plt.show()
plt.close('all')
