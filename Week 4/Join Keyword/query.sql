SELECT Star.radius, COUNT(Planet.koi_name)
FROM Star
JOIN Planet USING (kepler_id)
WHERE Star.radius >= 1
GROUP BY Star.kepler_id
HAVING COUNT(Planet.koi_name) > 1
ORDER BY Star.radius DESC;