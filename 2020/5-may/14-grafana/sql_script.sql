use weather;

drop table if exists IstanbulSunrise;

create table IstanbulSunrise(
DateTime DATETIME(6)
,State VARCHAR(100)
,Rain FLOAT(4)
,MaxTemp INT(4)
,MinTemp INT(4)
,SunRise VARCHAR(100) 
,SunSet VARCHAR(100)
,MoonRise VARCHAR(100)
,MoonSet VARCHAR(100)
,AvgWind INT(4)
,AvgHumidity INT(4)
,AvgPressure INT(4)
,SunRise_Time FLOAT(10)
,MoonRise_Time FLOAT(10)
,SunSet_Time FLOAT(10)
,MoonSet_Time FLOAT(10)
)
; 
