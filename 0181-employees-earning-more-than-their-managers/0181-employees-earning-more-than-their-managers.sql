# Write your MySQL query statement below
SELECT e.name as Employee
FROM employee e JOIN employee m ON m.id = e.managerId
WHERE e.salary > m.salary