__author__ = 'jj'

import numpy as np

FICO_groups = {1: '<=499', 2: '500-549', 3: '550-599', 4: '600-649', 5: '650-699', 6: '700-749', 7: '750-799', 8: '>=800'}

# Dec, 2012 data. for groups 1~8
FICO_distn = [0.02, 0.05, 0.08, 0.12, 0.15, 0.18, 0.28, 0.12]

# mid-2011 data. for groups 1~8
delinquency_by_FICO = [0.87, 0.71, 0.51, 0.31, 0.15, 0.05, 0.02, 0.01]

mixed_del_distn = dict(zip(delinquency_by_FICO[::-1], np.array(FICO_distn[::-1]).cumsum()))