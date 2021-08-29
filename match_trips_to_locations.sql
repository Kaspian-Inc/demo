select
  starbucks.store_name,
  current_timestamp experiment_time,
  citibikes.avg_distance,
  citibikes.avg_duration
from citibikes
join starbucks
using (lat, lon)
