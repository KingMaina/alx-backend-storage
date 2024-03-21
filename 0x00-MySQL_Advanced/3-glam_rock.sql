-- SQL script that retrieves the lifespan of bands with Glam Rock as their style
SELECT band_name,
CASE
  WHEN split IS NULL THEN YEAR(CURDATE()) - formed
  ELSE split - formed
END AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
