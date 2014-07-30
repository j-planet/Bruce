__author__ = 'jj'

FICO_groups = {1: '<=499', 2: '500-549', 3: '550-599', 4: '600-649', 5: '650-699', 6: '700-749', 7: '750-799', 8: '>=800'}

# Dec, 2012 data
FICO_distn = dict(zip(range(1, len(FICO_groups)+1), [0.02, 0.05, 0.08, 0.12, 0.15, 0.18, 0.28, 0.12]))

# mid-2011 data
delinquency_by_FICO = dict(zip(range(1, len(FICO_groups)+1), [0.87, 0.71, 0.51, 0.31, 0.15, 0.05, 0.02, 0.01]))