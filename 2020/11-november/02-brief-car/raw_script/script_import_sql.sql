use dataAi;

drop table if exists cardata;

create table cardata(
Car_Name VARCHAR(50)
,Year INT(4)
,Selling_Price FLOAT(4)
,Present_Price FLOAT(4)
,Kms_Driven INT(10)
,Fuel_Type VARCHAR(50) 
,Seller_Type VARCHAR(50)
,Transmission VARCHAR(50)
,Owner INT(5)
)
; 