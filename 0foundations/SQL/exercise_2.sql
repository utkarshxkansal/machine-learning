select * from movies order by release_year desc;
select * from movies where release_year = 2022;
select * from movies where release_year > 2020;
select * from movies where imdb_rating > 8;
select * from movies where studio in ("marvel studios","hombale films");
select * from movies where title like "%thor%" order by release_year asc;
select * from movies where studio not in ("marvel studios","hombale films");
select * from movies where studio !="marvel studios";



