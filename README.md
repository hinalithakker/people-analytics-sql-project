# People Analytics: Employee Attrition & Engagement Analysis

## 📊 Project Overview

A comprehensive data analytics project analyzing employee data for a 3,000+ employee organization to identify attrition patterns, engagement drivers, and training effectiveness. This end-to-end analytics solution demonstrates the complete workflow from data ingestion to actionable business insights.

## 🎯 Business Impact

**Key Findings:**
- **12.9% overall attrition rate** with significant variation across departments
- **Software Engineering (17.4%)** and **Production (15.9%)** showed highest turnover
- **Executive Office** achieved zero attrition with highest engagement scores (3.38)
- **Engagement alone doesn't predict retention** - technical roles showed high attrition despite moderate engagement

**Business Recommendations:**
- Prioritize retention strategies for high-turnover technical departments
- Investigate non-engagement factors driving attrition (workload, compensation, career growth)
- Redesign training programs for department-specific needs rather than uniform distribution

## 🛠️ Technical Skills Demonstrated

### Data Engineering & Analysis
- **SQL Database Design**: Created normalized tables for employees, engagement surveys, and training data
- **Data Validation**: Implemented comprehensive join validation and row count checks
- **ETL Pipeline**: Built Python scripts for data loading and transformation

### Analytics & Visualization
- **Statistical Analysis**: Department-level attrition and engagement correlations
- **Interactive Dashboard**: Streamlit application with real-time data exploration
- **Export Functionality**: CSV downloads, PDF reports, and chart exports

### Tools & Technologies
- **SQL (SQLite)**: Complex queries, aggregations, and data relationships
- **Python**: Pandas for data manipulation, Streamlit for web applications
- **Data Visualization**: Plotly for interactive charts and business intelligence
- **Version Control**: Git workflow with professional documentation

## 📈 Key Results

### Attrition Analysis
```
Department              Attrition Rate
Software Engineering      17.4%
Production               15.9%
IT/IS                    13.2%
Sales                    12.1%
Admin Offices             1.3%
Executive Office          0.0%
```

### Engagement Insights
- **Executive Office**: Highest engagement (3.38) and zero attrition
- **Production**: Lowest engagement (2.91) with high attrition
- **Correlation Analysis**: Engagement explains only part of retention patterns

## 📁 Project Structure

```
├── data/                          # Raw HR datasets
│   ├── employee_data.csv         # Employee master data
│   ├── employee_engagement_survey_data.csv
│   └── training_and_development_data.csv
├── sql/                          # SQL analysis scripts
│   ├── 01_create_tables.sql      # Database schema
│   ├── 02_load_data.sql         # Data loading
│   ├── 03_validation_checks.sql # Data quality assurance
│   ├── 04_reset_tables.sql      # Database management
│   ├── 05_exploratory_checks.sql # Initial analysis
│   └── 06_attrition_analysis.sql # Core business analysis
├── dashboard.py                  # Interactive Streamlit application
├── load_data.py                  # Python ETL script
└── requirements.txt              # Python dependencies
```

## 🔍 Sample Analysis Query

```sql
SELECT
    e.department_type,
    ROUND(AVG(g.engagement_score), 2) AS avg_engagement,
    ROUND(
        COUNT(CASE WHEN e.employee_status LIKE '%Terminated%' THEN 1 END) * 1.0
        / COUNT(*), 3
    ) AS attrition_rate
FROM employees e
JOIN engagement g ON e.emp_id = g.emp_id
GROUP BY e.department_type
ORDER BY attrition_rate DESC;
```

## 💼 Business Intelligence Insights

This project demonstrates the ability to:
- Transform raw HR data into actionable business intelligence
- Identify retention risk factors across different employee segments
- Build scalable analytics solutions for organizational decision-making
- Communicate complex data insights to non-technical stakeholders

## 📊 Live Dashboard

An interactive dashboard is available showcasing all key metrics and visualizations. The dashboard includes export functionality for sharing insights with stakeholders.

---

*This project showcases end-to-end data analytics capabilities, from database design to business intelligence reporting.*
