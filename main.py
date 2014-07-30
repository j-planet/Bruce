__author__ = 'jj'

import numpy as np
from collections import OrderedDict
import matplotlib.pyplot as plt

FICO_groups = {1: '<=499', 2: '500-549', 3: '550-599', 4: '600-649', 5: '650-699', 6: '700-749', 7: '750-799', 8: '>=800'}

# Dec, 2012 data. for groups 1~8
FICO_distn = [0.02, 0.05, 0.08, 0.12, 0.15, 0.18, 0.28, 0.12]

# mid-2011 data. for groups 1~8
delinquency_by_FICO = [0.87, 0.71, 0.51, 0.31, 0.15, 0.05, 0.02, 0.01]

# key: deliquency rate; value: cdf
mixed_del_distn = OrderedDict(zip(delinquency_by_FICO[::-1], np.array(FICO_distn[::-1]).cumsum()))

# plot del distribution
plt.step(mixed_del_distn.keys(), mixed_del_distn.values())
plt.title('CDF of Delinquency Rate')
plt.xlabel('Delinquency Rate')
plt.ylabel('Probability')
plt.show()

plt.step(delinquency_by_FICO, FICO_distn)
plt.title('PDF of Delinquency Rate')
plt.xlabel('Delinquency Rate')
plt.ylabel('Probability')
plt.show()

# figure out bankruptcy point
inflow = 0.07   # 3.5% x 2 feels from buyer and seller
outflow = 0.03   # 3% fixed cost (well, actually it's 2.9% + 30 cents)

# TODO:
#   - figureo out the mark where delinquency rate ==0.04 (i.e. inflow-outflow). put mark on the plot
#   - get correct delinquency rates for small loans only. rates are too high right now