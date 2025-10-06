CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
    WITH temp AS (
        SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) as rn
        FROM employee
    )
    SELECT MAx(salary)
    FROM temp
    WHERE rn = N
    LIMIT 1

  );
END