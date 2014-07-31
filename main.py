__author__ = 'jj'

import numpy as np
from collections import OrderedDict
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from scipy import interpolate
import scipy


def fit_beta(xs, ps):
    xs = np.array(xs)
    ps = np.array(ps)

    mu = sum(xs * ps)
    s2 = sum(np.square(xs) * ps) - mu**2

    alpha = (1-mu) * mu**2 / s2 - mu
    beta = alpha*(1/mu - 1)

    return alpha, beta


FICO_groups = {1: '<=499', 2: '500-549', 3: '550-599', 4: '600-649', 5: '650-699', 6: '700-749', 7: '750-799', 8: '>=800'}

# Dec, 2012 data. for groups 1~8
FICO_distn = [0.02, 0.05, 0.08, 0.12, 0.15, 0.18, 0.28, 0.12]

# mid-2011 data. for groups 1~8
delinquency_by_FICO = [0.87, 0.71, 0.51, 0.31, 0.15, 0.05, 0.02, 0.01]

# key: deliquency rate; value: cdf
del_cdf = OrderedDict(zip([0] + delinquency_by_FICO[::-1], [0] + list(np.array(FICO_distn[::-1]).cumsum())))
del_pdf = OrderedDict(zip([0] + delinquency_by_FICO[::-1] + [1], [0] + FICO_distn[::-1] + [0]))

# plot del distribution
plt.step(del_cdf.keys(), del_cdf.values())
plt.title('CDF of Delinquency Rate')
plt.xlabel('Delinquency Rate')
plt.ylabel('Probability')
plt.show()

plt.step(del_pdf.keys(), del_pdf.values())
plt.title('PDF of Delinquency Rate')
plt.xlabel('Delinquency Rate')
plt.ylabel('Probability')
plt.show()

# figure out bankruptcy point
inflow = 0.07   # 3.5% x 2 feels from buyer and seller
outflow = 0.03   # 3% fixed cost (well, actually it's 2.9% + 30 cents)


x, y = np.array(del_pdf.keys()), np.array(del_pdf.values())
xnew = np.arange(0.001, 1, 0.001)
ynew = scipy.stats.beta.pdf(xnew, 1.1, 5.401)

plt.step(x, y)
plt.title('PDF of Delinquency Rate')
plt.xlabel('Delinquency Rate')
plt.ylabel('Probability')
plt.axvline(0, color='red')
plt.plot(xnew, ynew, 'g')
plt.show()


# tck = interpolate.splrep(del_pdf.keys(), del_pdf.values(), k=3)
# fit=scipy.interpolate.interp1d(x,y)
# ynew = fit(xnew)
# ynew = interpolate.splev(xnew, tck)
# plt.axvspan(-0.03, -0.02, ymax=0.2, color='blue', alpha=0.5)
# plt.add_patch(Rectangle((-0.03, 0), 0.01, 0.12))
# plt.broken_barh([(-0.03, -0.02)], (0, 0.12), facecolors='blue')





# figure out the mark where delinquency rate ==0.04 (i.e. inflow-outflow)
netinflow = inflow - outflow

if netinflow >= max(del_cdf.keys()):
    belowProb = 0   # will never go under in this case
else:
    for i, curKey in enumerate(del_cdf.keys()):
        nextKey = del_cdf.keys()[i+1]
        if curKey <= netinflow and netinflow <= nextKey:
            gap = nextKey - curKey
            belowProb = (nextKey - netinflow)/gap * (1-del_cdf[curKey]) + (netinflow - curKey)/gap * (1 - del_cdf[nextKey])   # interpolated survival probability
            break


# put mark on the plot

# TODO:

#   - scenario analysis: limit credit scores