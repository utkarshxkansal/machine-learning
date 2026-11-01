select 
studio,count(*) as cnt ,
round(avg(imdb_rating),1) as avg_rating
from movies
WHERE studio!=""
group by studio
order by avg_rating desc;
