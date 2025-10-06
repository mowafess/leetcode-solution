# Write your MySQL query statement below
# Write your MySQL query statement below


WITH temp AS (
    SELECT *,
        LAG(w.temperature, 1) OVER (ORDER BY recordDate) AS prev_temp,
        LAG(w.recordDate, 1) OVER (ORDER BY recordDate) AS prev_date

    FROM weather w
)
SELECT Id
FROM temp
WHERE temperature > prev_temp AND recordDate = DATE_ADD(prev_date, INTERVAL 1 DAY)

