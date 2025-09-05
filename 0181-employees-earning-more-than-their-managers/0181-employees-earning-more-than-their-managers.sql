# Write your MySQL query statement below
SELECT emp.Name Employee
FROM Employee emp INNER JOIN Employee manager
on emp.ManagerId = manager.Id
WHERE emp.Salary > manager.Salary;