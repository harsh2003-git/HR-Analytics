/*1. Retrieve the total number of employees in each department*/

SELECT Department, COUNT(*) AS Total_Employees
FROM employee_cleaned
GROUP BY Department;

/*2. Find the average salary department-wise*/

SELECT Department,
       AVG(MonthlyIncome) AS Average_Salary
FROM employee_cleaned
GROUP BY Department;

/*3. Identify the top 10 highest-paid employees*/

SELECT EmployeeNumber,
       Department,
       JobRole,
       MonthlyIncome
FROM employee_cleaned
ORDER BY MonthlyIncome DESC
LIMIT 10;

/*4. Calculate the average years of experience by department*/

SELECT Department,
       AVG(TotalWorkingYears) AS Average_Experience
FROM employee_cleaned
GROUP BY Department;

/*5. Find employees with the highest performance rating*/

SELECT EmployeeNumber,
       Department,
       JobRole,
       PerformanceRating,
       MonthlyIncome
FROM employee_cleaned
WHERE PerformanceRating = (
    SELECT MAX(PerformanceRating)
    FROM employee_cleaned
);

/*6. Count employees who travel the most*/

SELECT BusinessTravel,
       COUNT(*) AS Employee_Count
FROM employee_cleaned
GROUP BY BusinessTravel;

/*7. Identify departments with the highest employee attrition*/

SELECT Department,
       COUNT(*) AS Attrition_Count
FROM employee_cleaned
WHERE Attrition = 'Yes'
GROUP BY Department
ORDER BY Attrition_Count DESC;

/*8. Rank employees based on salary within each department*/

SELECT EmployeeNumber,
       Department,
       JobRole,
       MonthlyIncome,
       DENSE_RANK() OVER (
           PARTITION BY Department
           ORDER BY MonthlyIncome DESC
       ) AS Salary_Rank
FROM employee_cleaned;

/*9. Find employees earning above the company average salary*/

SELECT EmployeeNumber,
       Department,
       JobRole,
       MonthlyIncome
FROM employee_cleaned
WHERE MonthlyIncome >
(
    SELECT AVG(MonthlyIncome)
    FROM employee_cleaned
);

/*10. Calculate gender-wise employee distribution*/

SELECT Gender,
       COUNT(*) AS Employee_Count
FROM employee_cleaned
GROUP BY Gender;