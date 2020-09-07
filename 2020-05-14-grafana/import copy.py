#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 17:09:39 2020

@author: utilisateur
"""
import pandas as pd
from sqlalchemy import create_engine

table_sql = 'IstanbulSunrise'
engine = create_engine('mysql+pymysql://root@localhost/weather')

# mydateparser = lambda x: pd.datetime.strptime(x, "%Y %m %d %H:%M:%S")

df = pd.read_csv('~/Downloads/Istanbul_Weather_Data.csv', sep=",", parse_dates=["DateTime"])


# df['SunRise'] = pd.to_timedelta(df['SunRise'])
# df['SunRise_Time'] = df['SunRise'].dt.total_seconds()

# df['MoonRise'] = pd.to_timedelta(df['MoonRise'])
# df['MoonRise_Time'] = df['MoonRise'].dt.total_seconds()

# df['SunSet'] = pd.to_timedelta(df['SunSet'])
# df['SunSet_Time'] = df['SunSet'].dt.total_seconds()

# df['MoonSet'] = pd.to_timedelta(df['MoonSet'])
# df['MoonSet_Time'] = df['MoonSet'].dt.total_seconds()



df.to_sql(table_sql, con=engine, if_exists='append', index=False)
