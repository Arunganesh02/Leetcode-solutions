# Write your MySQL query statement below
Select max(salary) as SecondHighestSalary
From employee
where salary not in (
    Select max(salary)
    From employee
)
-- order by SecondHighestSalary desc
limit 1
