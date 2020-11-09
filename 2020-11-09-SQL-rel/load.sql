LOAD DATA LOCAL INFILE '/home/joshua/Documents/git-workspace/audit/2020-11-09-SQL-rel/data/netflix_shows.csv'
INTO TABLE netflix_shows
CHARACTER SET latin1
FIELDS TERMINATED BY ','
ENCLOSED BY '*'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;