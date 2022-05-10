select
  starbucks.store_name,
  current_timestamp experiment_time,
  citibikes.avg_distance,
  citibikes.avg_duration
from citibikes c
join starbucks s
where 1=1
  and round(c.lat, 3) = round(s.lat, 3)
  and round(c.lon, 3) = round(s.lon, 3)
