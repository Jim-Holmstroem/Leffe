from __future__ import division, print_function

import pandas as pd

import ulmo

def main_data_df():
    STATION = 'SWM00002485'
    data = ulmo.ncdc.ghcn_daily.get_data(STATION, as_dataframe=True)

    tmax = data['TMAX']['value'] / 10.
    tmin = data['TMIN']['value'] / 10.
    prcp = data['PRCP']['value'] / 10.

    df = pd.DataFrame({
        'tmax': tmax,
        'tmin': tmin,
        'prcp': prcp,
    })

    return df
