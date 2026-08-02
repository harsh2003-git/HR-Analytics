HR Employee Attrition Analysis
Project Overview

The HR Employee Attrition Analysis project is a Python-based data analysis application that analyzes employee information to generate meaningful business insights, visualizations, and an automated PDF report. The project helps HR professionals understand employee demographics, salary distribution, department-wise performance, attrition trends, and other workforce analytics.

Objectives
Analyze employee salary and department statistics.
Study employee experience and performance.
Visualize HR data using charts and graphs.
Generate business insights automatically.
Create a professional PDF report containing analysis and visualizations.
Dataset

The project uses the IBM HR Employee Attrition Dataset.

Dataset Features
Age
Attrition
BusinessTravel
Department
Education
EducationField
Gender
JobRole
JobLevel
MonthlyIncome
PerformanceRating
TotalWorkingYears
YearsAtCompany
WorkLifeBalance
OverTime
MaritalStatus
EnvironmentSatisfaction
JobSatisfaction
RelationshipSatisfaction
StockOptionLevel
TrainingTimesLastYear
YearsSinceLastPromotion
YearsWithCurrManager
and other HR-related attributes.
Project Structure
Final_Project/
│
├── data/
│   ├── HR data.csv
│   └── employee_cleaned.csv
│
├── images/
│   ├── monthly_income_distribution.png
│   ├── age_distribution.png
│   ├── monthly_income_boxplot.png
│   ├── experience_boxplot.png
│   ├── department_countplot.png
│   ├── gender_countplot.png
│   ├── education_countplot.png
│   ├── avg_salary_department.png
│   ├── business_travel_distribution.png
│   ├── experience_vs_salary.png
│   ├── correlation_heatmap.png
│   └── pair_plot.png
│
├── reports/
│   └── Final_Report.pdf
│
├── src/
│   ├── load_data.py
│   ├── preprocessing.py
│   ├── analysis.py
│   ├── visualization.py
│   └── report.py
│
├── main.py
├── requirements.txt
└── README.md
