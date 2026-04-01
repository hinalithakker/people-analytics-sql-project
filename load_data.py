import sqlite3
import pandas as pd

conn = sqlite3.connect("database/people_analytics.db")

employees = pd.read_csv("data/employee_data.csv")
engagement = pd.read_csv("data/employee_engagement_survey_data.csv")
training = pd.read_csv("data/training_and_development_data.csv")

employees.columns = employees.columns.str.strip().str.lower()
engagement.columns = engagement.columns.str.strip().str.lower()
training.columns = training.columns.str.strip().str.lower()

training = training.rename(columns={
    "training_duration(days)": "training_duration_days"
})

employees.to_sql("employees", conn, if_exists="replace", index=False)
engagement.to_sql("engagement", conn, if_exists="replace", index=False)
training.to_sql("training", conn, if_exists="replace", index=False)

print("Data loaded successfully!")

conn.close()