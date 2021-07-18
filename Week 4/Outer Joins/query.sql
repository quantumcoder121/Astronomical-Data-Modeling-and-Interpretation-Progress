SELECT s.kepler_id, s.t_eff, s.radius
FROM Star AS s
LEFT OUTER JOIN Planet AS p USING (kepler_id)
WHERE p.koi_name is NULL
ORDER BY t_eff DESC;