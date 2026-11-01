select * from movies where imdb_rating>=9;
select * from movies where imdb_rating>=6 and imdb_rating<=8;
select * from movies where imdb_rating between 6 and 8;
select * from movies where release_year in (2007,2022);
select * from movies where studio = "";
select * from movies where industry in ('bollywood','hollywood');
select * from movies where imdb_rating is null;
select * from movies where industry = "bollywood" order by imdb_rating desc limit 5 offset 3

