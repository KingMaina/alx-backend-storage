-- SQL script that retrieves the lifespan of bands with Glam Rock as their style
SELECT band_name,
CASE
  WHEN split IS NULL THEN 2024 - formed
  ELSE split - formed
END AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
