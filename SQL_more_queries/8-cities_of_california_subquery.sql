-- List all cities of California sorted by cities.id without using JOIN
SELECT cities.id, cities.name, cities.state_id
FROM cities, states
WHERE states.name = 'California'
  AND cities.state_id = states.id
ORDER BY cities.id ASC;
