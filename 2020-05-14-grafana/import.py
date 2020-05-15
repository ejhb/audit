#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 17:09:39 2020

@author: utilisateur
"""
import pandas as pd
from sqlalchemy import create_engine


engine = create_engine('mysql+pymysql://root@localhost/weather')

def load(fichier_csv, table_sql,rows_to_skip):
    mydateparser = lambda x: pd.datetime.strptime(x, "%Y %m %d %H:%M:%S")
    df = pd.read_csv(fichier_csv, delimiter='|', skiprows=rows_to_skip, parse_dates={'DateTime':[0, 1]}, date_parser=mydateparser, index_col='DateTime')
    
    df.to_sql(table_sql, con=engine, if_exists='append', index=False)
    
    return print('Table', table_sql, 'filled.')

weather = '/home/joshua/Downloads/Istanbul_Weather_Data.csv'

load(weather, 'IstanbulSunrise',0)
