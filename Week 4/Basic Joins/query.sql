SELECT s.radius AS sun_radius,
  p.radius AS planet_radius
FROM Star AS s, Planet AS p
WHERE s.kepler_id = p.kepler_id AND
  s.radius > p.radius 
ORDER BY s.radius DESC;