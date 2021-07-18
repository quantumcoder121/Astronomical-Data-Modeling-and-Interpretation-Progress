SELECT ROUND(AVG(P.t_eq), 1), MIN(S.t_eff), MAX(S.t_eff)
FROM Star S
JOIN Planet P USING(kepler_id)
WHERE S.t_eff > (
  SELECT AVG(t_eff) FROM Star
);