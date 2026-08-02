#import modules
from src.load_data import load_data
from src.preprocessing import*
from src.analysis import*
from src.visualization import*
from src.report import generate_report

#import data
print("="*60)
print("Loading Dataset")
print("="*60)
df= load_data("data/HR data.csv")

#data preprocessing
print("="*60)
print("Data Preprocessing")
print("="*60)

dataset_info(df)

check_missing_values(df)

check_duplicates(df)

remove_duplicates(df)

save_clean_data(df)

#Data Analysis
average_salary(df)
highest_salary(df)
lowest_salary(df)

    # -----------------------------
    # Department Analysis
    # -----------------------------
department_salary(df)
department_count(df)

    # -----------------------------
    # Education Analysis
    # -----------------------------
education_wise_salary(df)

    # -----------------------------
    # Experience Analysis
    # -----------------------------
experience_average_salary(df)
experience_highest_salary(df)
experience_lowest_salary(df)

    # -----------------------------
    # Gender Analysis
    # -----------------------------
gender_count(df)
gender_wise_salary(df)

    # -----------------------------
    # Business Travel Analysis
    # -----------------------------
business_travel_count(df)
business_travel_salary(df)
business_travel_attrition(df)

    # -----------------------------
    # Job Analysis
    # -----------------------------
jobrole_salary(df)
joblevel_salary(df)

    # -----------------------------
    # Company Experience Analysis
    # -----------------------------
yearsatcompany_salary(df)

    # -----------------------------
    # Correlation Analysis
    # -----------------------------
correlation_experience_salary(df)

    # -----------------------------
    # Business Insights
    # -----------------------------
business_insights(df)


#Visualization
salary_distribution(df)

age_distribution(df)

salary_boxplot(df)

experience_boxplot(df)

department_count(df)

gender_count(df)

education_count(df)

avg_salary_by_department(df)

business_travel_distribution(df)

experience_vs_salary(df)

correlation_heatmap(df)

pair_plot(df)

#Generate Report
print("Report Started")
generate_report(df)
print("Report Finished")
