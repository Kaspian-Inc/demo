select
  s.store_name,
  current_timestamp experiment_time,
  c.avg_distance,
  c.avg_duration
from citibikes c
join starbucks s
where 1=1
  and true
  and round(c.lat, 2) = round(s.lat, 2)
  and round(c.lon, 2) = round(s.lon, 2)