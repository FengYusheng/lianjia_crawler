import matplotlib.pyplot as plt
import numpy as np

# plt.plot([1,2,3,4], [1,4,9,16], 'ro')
# plt.axis([0, 6, 0, 20])
# plt.show()

# t = np.arange(0., 5., 0.2)
# plt.plot(t, t, 'r--', t, t*2, 'bs', t, t**2, 'g^')
# plt.show()

# plt.figure(1)
# plt.show()

# def f(t):
#     return np.exp(-t) * np.cos(2 * np.pi * t)
#
# t1 = np.arange(0.0, 5.0, 0.1)
# t2 = np.arange(0.0, 5.0, 0.02)
#
# plt.figure(1)
# plt.subplot(211)
# plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
# plt.subplot(212)
# plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
# plt.show()


# plt.figure(1)
# plt.subplot(211)
# plt.plot([1,2,3])
# plt.subplot(212)
# plt.plot([4,5,6])
#
# plt.figure(2)
# plt.plot([4,5,6])
#
# plt.figure(1)
# plt.subplot(211)
# plt.title('Easy as 1, 2, 3')
#
# plt.show()
# plt.close('all')



mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()
plt.close('all')
