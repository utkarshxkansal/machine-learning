select min(imdb_rating) as min_rating,
max(imdb_rating) as max_imdb ,
avg(imdb_rating) as avg_rating
from movies where studio='marvel studios';
select 
studio,count(*) as cnt ,
round(avg(imdb_rating),1) as avg_rating
from movies
WHERE studio!=""
group by studio
order by avg_rating desc;
