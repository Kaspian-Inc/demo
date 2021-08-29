select
  name store_name,
  round(lat, 3) lat,
  round(lon, 3) lon
from data
where city = 'New York'
