-- Write your PostgreSQL query statement below
SELECT e.name AS Employee
FROM Employee e
JOIN Employee emp
ON e.managerId = emp.id
WHERE e.salary > emp.salary;