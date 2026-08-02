import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create images folder automatically
os.makedirs("images", exist_ok=True)


# -----------------------------------------
# Monthly Income Distribution
# -----------------------------------------

def salary_distribution(df):
    plt.figure(figsize=(8,5))
    plt.hist(df["MonthlyIncome"], bins=10, edgecolor="black")
    plt.title("Monthly Income Distribution")
    plt.xlabel("Monthly Income")
    plt.ylabel("Frequency")

    plt.savefig("images/monthly_income_distribution.png")
    plt.show()


# -----------------------------------------
# Age Distribution
# -----------------------------------------

def age_distribution(df):
    plt.figure(figsize=(8,5))
    plt.hist(df["Age"], bins=10, edgecolor="black")
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Frequency")

    plt.savefig("images/age_distribution.png")
    plt.show()


# -----------------------------------------
# Monthly Income Box Plot
# -----------------------------------------

def salary_boxplot(df):
    plt.figure(figsize=(6,5))
    sns.boxplot(y=df["MonthlyIncome"])
    plt.title("Monthly Income Box Plot")

    plt.savefig("images/monthly_income_boxplot.png")
    plt.show()


# -----------------------------------------
# Total Working Years Box Plot
# -----------------------------------------

def experience_boxplot(df):
    plt.figure(figsize=(6,5))
    sns.boxplot(y=df["TotalWorkingYears"])
    plt.title("Total Working Years Box Plot")

    plt.savefig("images/experience_boxplot.png")
    plt.show()


# -----------------------------------------
# Department Count Plot
# -----------------------------------------

def department_count(df):
    plt.figure(figsize=(8,5))
    sns.countplot(x="Department", data=df)
    plt.title("Department Distribution")
    plt.xticks(rotation=30)

    plt.savefig("images/department_countplot.png")
    plt.show()


# -----------------------------------------
# Gender Count Plot
# -----------------------------------------

def gender_count(df):
    plt.figure(figsize=(6,5))
    sns.countplot(x="Gender", data=df)
    plt.title("Gender Distribution")

    plt.savefig("images/gender_countplot.png")
    plt.show()


# -----------------------------------------
# Education Count Plot
# -----------------------------------------

def education_count(df):
    plt.figure(figsize=(8,5))
    sns.countplot(x="Education", data=df)
    plt.title("Education Distribution")

    plt.savefig("images/education_countplot.png")
    plt.show()


# -----------------------------------------
# Average Monthly Income by Department
# -----------------------------------------

def avg_salary_by_department(df):

    avg_salary = (
        df.groupby("Department")["MonthlyIncome"]
        .mean()
        .reset_index()
    )

    plt.figure(figsize=(8,5))
    sns.barplot(
        x="Department",
        y="MonthlyIncome",
        data=avg_salary
    )

    plt.title("Average Monthly Income by Department")
    plt.xticks(rotation=30)

    plt.savefig("images/avg_salary_department.png")
    plt.show()


# -----------------------------------------
# Business Travel Distribution
# -----------------------------------------

def business_travel_distribution(df):

    travel = df["BusinessTravel"].value_counts()

    plt.figure(figsize=(6,6))
    plt.pie(
        travel,
        labels=travel.index,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Business Travel Distribution")

    plt.savefig("images/business_travel_distribution.png")
    plt.show()


# -----------------------------------------
# Experience vs Monthly Income
# -----------------------------------------

def experience_vs_salary(df):

    plt.figure(figsize=(8,5))
    plt.scatter(
        df["TotalWorkingYears"],
        df["MonthlyIncome"]
    )

    plt.title("Experience vs Monthly Income")
    plt.xlabel("Total Working Years")
    plt.ylabel("Monthly Income")

    plt.savefig("images/experience_vs_salary.png")
    plt.show()


# -----------------------------------------
# Correlation Heatmap
# -----------------------------------------

def correlation_heatmap(df):

    plt.figure(figsize=(12,8))

    sns.heatmap(
        df.corr(numeric_only=True),
        annot=True,
        cmap="coolwarm"
    )

    plt.title("Correlation Heatmap")

    plt.savefig("images/correlation_heatmap.png")
    plt.show()


# -----------------------------------------
# Pair Plot
# -----------------------------------------

def pair_plot(df):

    cols = [
        "Age",
        "MonthlyIncome",
        "TotalWorkingYears",
        "YearsAtCompany",
        "JobLevel"
    ]

    pair = sns.pairplot(df[cols])

    pair.savefig("images/pair_plot.png")
    plt.show()