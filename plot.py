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

block = [r[0] for r in l1]


plt.figure(1)
plt.subplot(211)
unit = [i[1] for i in l1[0:50]]
block_index = [i for i in xrange(1, 51)]
plt.xlabel('block index')
plt.ylabel('unit')
plt.plot(block_index, unit, 'b')

plt.annotate('MAI HAO SHI DAI({0})'.format(72032), xy=(20, 72032),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )


plt.grid(True)

plt.subplot(212)
star = [i[1] for i in l2[0:50]]
block_index = [i for i in xrange(1, 51)]
plt.xlabel('block index')
plt.ylabel('star')
plt.plot(block_index, star, 'g')

plt.annotate('MAI HAO SHI DAI({0})'.format(168), xy=(20, 168),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )

plt.grid(True)

plt.show()
plt.close('all')
