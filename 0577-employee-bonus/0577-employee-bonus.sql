-- Write your PostgreSQL query statement below
SELECT e.name,b.bonus
FROM Employee e
LEFT JOIN Bonus b
ON e.empID = b.empID
WHERE Bonus < 1000 OR Bonus IS NULL;