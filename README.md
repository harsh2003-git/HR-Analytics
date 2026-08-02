# HR Employee Attrition Analysis

## Project Overview

The **HR Employee Attrition Analysis** project is a Python-based data analysis application that analyzes employee information to generate meaningful business insights, visualizations, and an automated PDF report. The project helps HR professionals understand employee demographics, salary distribution, department-wise performance, attrition trends, and workforce analytics.

---

## Objectives

- Analyze employee salary and department statistics.
- Study employee experience and performance.
- Visualize HR data using charts and graphs.
- Generate business insights automatically.
- Create a professional PDF report containing analysis and visualizations.

---

## Dataset

The project uses the **IBM HR Employee Attrition Dataset**.

### Dataset Features

- Age
- Attrition
- BusinessTravel
- DailyRate
- Department
- DistanceFromHome
- Education
- EducationField
- EmployeeCount
- EmployeeNumber
- EnvironmentSatisfaction
- Gender
- HourlyRate
- JobInvolvement
- JobLevel
- JobRole
- JobSatisfaction
- MaritalStatus
- MonthlyIncome
- MonthlyRate
- NumCompaniesWorked
- Over18
- OverTime
- PercentSalaryHike
- PerformanceRating
- RelationshipSatisfaction
- StandardHours
- StockOptionLevel
- TotalWorkingYears
- TrainingTimesLastYear
- WorkLifeBalance
- YearsAtCompany
- YearsInCurrentRole
- YearsSinceLastPromotion
- YearsWithCurrManager

---

# Project Structure

```text
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
```

---

# Features

## Data Loading

- Load HR dataset
- Display dataset information
- Verify successful loading

---

## Data Preprocessing

- Dataset information
- Missing value analysis
- Duplicate value detection
- Duplicate removal
- Save cleaned dataset

---

## Data Analysis

The project performs the following analyses:

- Average Monthly Income
- Highest Monthly Income
- Lowest Monthly Income
- Department-wise Employee Count
- Department-wise Average Monthly Income
- Education-wise Salary Analysis
- Experience-wise Salary Analysis
- Gender-wise Salary Analysis
- Business Travel Analysis
- Job Role Salary Analysis
- Job Level Salary Analysis
- Years at Company Analysis
- Correlation between Total Working Years and Monthly Income
- Business Insights

---

## Visualizations

The project automatically generates the following visualizations:

- Monthly Income Distribution (Histogram)
- Age Distribution (Histogram)
- Monthly Income Box Plot
- Total Working Years Box Plot
- Department Count Plot
- Gender Count Plot
- Education Count Plot
- Average Monthly Income by Department
- Business Travel Distribution (Pie Chart)
- Experience vs Monthly Income (Scatter Plot)
- Correlation Heatmap
- Pair Plot

All charts are automatically saved inside the **images/** folder.

---

## Business Insights

The generated report includes:

- Total Employees
- Average Monthly Income
- Highest Monthly Income
- Lowest Monthly Income
- Highest Paid Department
- Largest Department
- Highest Paid Job Role
- Gender Distribution
- Business Travel Distribution
- Average Employee Experience
- Experience vs Salary Correlation
- Employee Attrition Count

---

## PDF Report

The project automatically generates a professional PDF report containing:

- Dataset Overview
- Data Cleaning Summary
- Statistical Summary
- Business Insights
- Charts and Visualizations
- Final Summary
- Business Recommendations

The report is saved in:

```text
reports/Final_Report.pdf
```

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- ReportLab

---

# Required Libraries

Install all dependencies using:

```bash
pip install pandas numpy matplotlib seaborn reportlab
```
