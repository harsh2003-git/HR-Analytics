# ==========================================
# HR DATASET ANALYSIS FUNCTIONS
# ==========================================

# -----------------------------
# Monthly Income Analysis
# -----------------------------

def average_salary(df):
    print("\n===== Average Monthly Income =====")
    print(df["MonthlyIncome"].mean())


def highest_salary(df):
    print("\n===== Highest Monthly Income =====")
    print(df["MonthlyIncome"].max())


def lowest_salary(df):
    print("\n===== Lowest Monthly Income =====")
    print(df["MonthlyIncome"].min())


# -----------------------------
# Department Analysis
# -----------------------------

def department_salary(df):
    print("\n===== Average Monthly Income by Department =====")
    print(df.groupby("Department")["MonthlyIncome"].mean())


def department_count(df):
    print("\n===== Department Count =====")
    print(df["Department"].value_counts())


# -----------------------------
# Education Analysis
# -----------------------------

def education_wise_salary(df):
    print("\n===== Salary by Education =====")
    print(df.groupby("Education")["MonthlyIncome"].agg(
        Employee_Count="count",
        Average_Salary="mean",
        Minimum_Salary="min",
        Maximum_Salary="max"
    ))


# -----------------------------
# Experience Analysis
# -----------------------------

def experience_average_salary(df):
    print("\n===== Average Salary by Total Working Years =====")
    print(df.groupby("TotalWorkingYears")["MonthlyIncome"].mean())


def experience_highest_salary(df):
    print("\n===== Highest Salary by Total Working Years =====")
    print(df.groupby("TotalWorkingYears")["MonthlyIncome"].max())


def experience_lowest_salary(df):
    print("\n===== Lowest Salary by Total Working Years =====")
    print(df.groupby("TotalWorkingYears")["MonthlyIncome"].min())


# -----------------------------
# Gender Analysis
# -----------------------------

def gender_count(df):
    print("\n===== Gender Count =====")
    print(df["Gender"].value_counts())


def gender_wise_salary(df):
    print("\n===== Gender-wise Salary Analysis =====")
    print(df.groupby("Gender")["MonthlyIncome"].agg(
        Employee_Count="count",
        Average_Salary="mean",
        Minimum_Salary="min",
        Maximum_Salary="max"
    ))


# -----------------------------
# Business Travel Analysis
# -----------------------------

def business_travel_count(df):
    print("\n===== Employee Count by Business Travel =====")
    print(df["BusinessTravel"].value_counts())


def business_travel_salary(df):
    print("\n===== Salary Analysis by Business Travel =====")
    print(df.groupby("BusinessTravel")["MonthlyIncome"].agg(
        Employee_Count="count",
        Average_Salary="mean",
        Minimum_Salary="min",
        Maximum_Salary="max"
    ))


def business_travel_attrition(df):
    print("\n===== Attrition by Business Travel =====")
    print(df.groupby("BusinessTravel")["Attrition"].value_counts())


# -----------------------------
# Job Role Analysis
# -----------------------------

def jobrole_salary(df):
    print("\n===== Average Salary by Job Role =====")
    print(df.groupby("JobRole")["MonthlyIncome"].mean().sort_values(ascending=False))


# -----------------------------
# Job Level Analysis
# -----------------------------

def joblevel_salary(df):
    print("\n===== Average Salary by Job Level =====")
    print(df.groupby("JobLevel")["MonthlyIncome"].mean())


# -----------------------------
# Years at Company Analysis
# -----------------------------

def yearsatcompany_salary(df):
    print("\n===== Average Salary by Years at Company =====")
    print(df.groupby("YearsAtCompany")["MonthlyIncome"].mean())


# -----------------------------
# Correlation Analysis
# -----------------------------

def correlation_experience_salary(df):
    print("\n===== Correlation Between Experience and Salary =====")
    print(df["TotalWorkingYears"].corr(df["MonthlyIncome"]))


# -----------------------------
# Business Insights
# -----------------------------

def business_insights(df):

    print("\n===================================")
    print("       BUSINESS INSIGHTS")
    print("===================================")

    print("Total Employees :", len(df))

    print("Average Monthly Income :",
          round(df["MonthlyIncome"].mean(), 2))

    print("Highest Monthly Income :",
          df["MonthlyIncome"].max())

    print("Lowest Monthly Income :",
          df["MonthlyIncome"].min())

    highest_paid_dept = (
        df.groupby("Department")["MonthlyIncome"]
        .mean()
        .idxmax()
    )

    print("Highest Paid Department :", highest_paid_dept)

    largest_department = (
        df["Department"]
        .value_counts()
        .idxmax()
    )

    print("Largest Department :", largest_department)

    highest_paid_role = (
        df.groupby("JobRole")["MonthlyIncome"]
        .mean()
        .idxmax()
    )

    print("Highest Paid Job Role :", highest_paid_role)

    print("\nGender Distribution")
    print(df["Gender"].value_counts())

    print("\nBusiness Travel Distribution")
    print(df["BusinessTravel"].value_counts())

    print("\nAttrition")
    print(df["Attrition"].value_counts())

    print("\nAverage Total Working Years :",
          round(df["TotalWorkingYears"].mean(), 2))

    corr = df["TotalWorkingYears"].corr(df["MonthlyIncome"])

    print("Experience vs Salary Correlation :",
          round(corr, 2))

    print("\nAverage Salary by Department")
    print(df.groupby("Department")["MonthlyIncome"].mean())

    print("\nAverage Salary by Job Level")
    print(df.groupby("JobLevel")["MonthlyIncome"].mean())

    print("\nAverage Salary by Education")
    print(df.groupby("Education")["MonthlyIncome"].mean())

    print("\nAverage Salary by Business Travel")
    print(df.groupby("BusinessTravel")["MonthlyIncome"].mean())