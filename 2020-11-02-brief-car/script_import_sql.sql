use dataAi;

drop table if exists cardata;

create table cardata(
Car_Name VARCHAR(100)
,Year INT(4)
,Selling_Price FLOAT(4)
,Present_Price FLOAT(4)
,Kms_Driven INT(10)
,Fuel_Type VARCHAR(100) 
,Seller_Type VARCHAR(100)
,Transmission VARCHAR(100)
,Owner INT(5)
)
; 