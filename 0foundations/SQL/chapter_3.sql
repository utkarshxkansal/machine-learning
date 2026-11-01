select max(imdb_rating) from movies where industry ="bollywood";
select avg(imdb_rating) from movies where studio = "marvel studios";
select round(avg(imdb_rating),1) as avg_rating
select 
studio,count(*) as cnt ,
round(avg(imdb_rating),1) as avg_rating
from movies
WHERE studio!=""
group by studio
order by avg_rating desc;
