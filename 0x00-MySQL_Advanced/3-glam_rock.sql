-- Select the database
USE holberton;

-- Query to list all bands with Glam rock as their main style, ranked by their longevity
SELECT
    name AS band_name,
    IFNULL(LEAST(IFNULL(split, 2022), 2022) - formed, 0) AS lifespan
FROM
    metal_bands
WHERE
    main_style = 'Glam rock'
ORDER BY
    lifespan DESC;

