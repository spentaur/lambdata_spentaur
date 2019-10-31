import numpy as np
import pandas as pd

ONES = pd.Series(np.ones(20))
ZEROS = pd.Series(np.zeros(20))

# Check a dataframe for nulls, print/report them in a nice "pretty" format
def perc_missing(X):
    nulls = X.isna().sum()
    print("  % Missing  ")
    print("--------------")
    return (nulls[nulls > 0] / len(X) * 100).sort_values(ascending=False)

def split_date(X, time_intervals):
    '''
    X = DataFrame with Date column
    time_intervals = array of pandas time date components, stylized for the column name
    (capital and spaced)
    https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#time-date-components

    '''
    X = X.copy()

    X['Date'] = pd.to_datetime(X['Date'])

    for interval in time_intervals:
        X[interval] = getattr(X['Date'].dt, interval.replace(' ', '').lower())

    return X