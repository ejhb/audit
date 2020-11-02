#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
import pandas as pd
import time


engine = create_engine("mysql+pymysql://root@localhost/dataAi")

column = "Car_Name  Year    Selling_Price   Present_Price   Kms_Driven    Fuel_Type     Seller_Type     Transmission    Owner"

def chargement(x, link, table):
    
    print("Lecture des données")
    col = x.split()
    start_time = time.time()
    df = pd.read_csv(link, encoding="UTF-8")
    df.columns = col
    print("Données lu")
    df.to_sql(table, con = engine, if_exists='append', index=False)
    return print("Temps d execution : %s secondes ---" % (time.time() - start_time))


chargement(column,'2020-11-02-brief-car/carData.csv', 'cardata')



