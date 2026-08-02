import os
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Image,
    Spacer
)


def generate_report(df):
    print("Inside report function...")
    os.makedirs("reports", exist_ok=True)

    pdf = SimpleDocTemplate(
        "reports/Final_Report.pdf"
    )

    styles = getSampleStyleSheet()
    elements = []

    # Title
    elements.append(
        Paragraph(
            "HR Employee Attrition Analysis Report",
            styles["Title"]
        )
    )

    elements.append(Spacer(1, 20))

    # Business Insights
    elements.append(
        Paragraph(
            "<b>Business Insights</b>",
            styles["Heading2"]
        )
    )

    elements.append(
        Paragraph(
            f"Total Employees: {len(df)}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Average Monthly Income: {round(df['MonthlyIncome'].mean(),2)}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Highest Monthly Income: {df['MonthlyIncome'].max()}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Lowest Monthly Income: {df['MonthlyIncome'].min()}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Highest Paid Department: {df.groupby('Department')['MonthlyIncome'].mean().idxmax()}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Largest Department: {df['Department'].value_counts().idxmax()}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Highest Paid Job Role: {df.groupby('JobRole')['MonthlyIncome'].mean().idxmax()}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Average Total Working Years: {round(df['TotalWorkingYears'].mean(),2)}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Experience-Salary Correlation: {round(df['TotalWorkingYears'].corr(df['MonthlyIncome']),2)}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Most Common Business Travel: {df['BusinessTravel'].mode()[0]}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Attrition Count: {(df['Attrition']=='Yes').sum()}",
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1,20))

    # Charts
    elements.append(
        Paragraph(
            "<b>Charts</b>",
            styles["Heading2"]
        )
    )

    charts = [
        "monthly_income_distribution.png",
        "age_distribution.png",
        "monthly_income_boxplot.png",
        "experience_boxplot.png",
        "department_countplot.png",
        "gender_countplot.png",
        "education_countplot.png",
        "avg_salary_department.png",
        "business_travel_distribution.png",
        "experience_vs_salary.png",
        "correlation_heatmap.png",
        "pair_plot.png"
    ]

    for chart in charts:
        image_path = f"images/{chart}"
        if os.path.exists(image_path):
            elements.append(
                Image(
                    image_path,
                    width=400,
                    height=250
                )
            )
            elements.append(Spacer(1,10))

    # Final Summary
    elements.append(
        Paragraph(
            "<b>Final Summary</b>",
            styles["Heading2"]
        )
    )

    elements.append(
        Paragraph(
            f"Total Employees: {len(df)}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Average Monthly Income: {round(df['MonthlyIncome'].mean(),2)}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Highest Paid Department: {df.groupby('Department')['MonthlyIncome'].mean().idxmax()}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Largest Department: {df['Department'].value_counts().idxmax()}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Average Experience: {round(df['TotalWorkingYears'].mean(),2)} Years",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Employees Left Organization: {(df['Attrition']=='Yes').sum()}",
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1,20))

    # Recommendations
    elements.append(
        Paragraph(
            "<b>Recommendations</b>",
            styles["Heading2"]
        )
    )

    recommendations = [
        "1. Improve employee retention strategies to reduce attrition.",
        "2. Review salary structures across departments for fair compensation.",
        "3. Invest in employee training and career development programs.",
        "4. Focus on departments with higher attrition and lower satisfaction.",
        "5. Encourage work-life balance and employee engagement initiatives."
    ]

    for rec in recommendations:
        elements.append(
            Paragraph(
                rec,
                styles["BodyText"]
            )
        )

    print("Building PDF...")
    pdf.build(elements)
    print("PDF Generated Successfully!")