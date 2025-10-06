# Write your MySQL query statement below

WITH temp AS (
    SELECT
        d.name AS Department,
        e.name AS Employee,
        e.salary AS Salary,
        DENSE_RANK() OVER (PARTITION BY d.name ORDER BY e.salary DESC) AS rn
    FROM employee e JOIN department d ON e.departmentID = d.id
)
SELECT Department, Employee, Salary
FROM temp
WHERE rn = 1