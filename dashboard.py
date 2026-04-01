import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
import plotly.graph_objects as go

# Set page config
st.set_page_config(page_title="People Analytics Dashboard", page_icon="📊", layout="wide")

# Connect to database
@st.cache_data
def load_data():
    conn = sqlite3.connect("database/people_analytics.db")

    # Load employees data
    employees = pd.read_sql_query("SELECT * FROM employees", conn)

    # Load engagement data
    engagement = pd.read_sql_query("SELECT * FROM engagement", conn)

    # Load training data
    training = pd.read_sql_query("SELECT * FROM training", conn)

    conn.close()
    return employees, engagement, training

# Load data
employees, engagement, training = load_data()

# Clean data
employees['department_type'] = employees['department_type'].str.strip()
employees['employee_status'] = employees['employee_status'].str.strip()

# Merge datasets
merged_data = employees.merge(engagement, on='emp_id', how='left').merge(training, on='emp_id', how='left')

# Title
st.title("📊 People Analytics Dashboard")

# KPIs
col1, col2, col3, col4 = st.columns(4)

with col1:
    total_employees = len(employees)
    st.metric("Total Employees", f"{total_employees:,}")

with col2:
    attrition_rate = (employees['employee_status'].str.lower() == 'terminated').mean() * 100
    st.metric("Overall Attrition Rate", f"{attrition_rate:.1f}%")

with col3:
    avg_engagement = engagement['engagement_score'].mean()
    st.metric("Avg Engagement Score", f"{avg_engagement:.2f}")

with col4:
    avg_satisfaction = engagement['satisfaction_score'].mean()
    st.metric("Avg Satisfaction Score", f"{avg_satisfaction:.2f}")

# Attrition Analysis
st.header("Attrition Analysis")

col1, col2 = st.columns(2)

with col1:
    # Attrition by Department
    attrition_by_dept = employees.groupby('department_type')['employee_status'].apply(
        lambda x: (x.str.lower() == 'terminated').mean() * 100
    ).sort_values(ascending=False).reset_index()

    fig_attrition = px.bar(
        attrition_by_dept,
        x='department_type',
        y='employee_status',
        title='Attrition Rate by Department (%)',
        labels={'employee_status': 'Attrition Rate (%)'},
        color='employee_status',
        color_continuous_scale='Reds'
    )
    fig_attrition.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig_attrition, use_container_width=True)

with col2:
    # Employee Status Distribution
    status_counts = employees['employee_status'].value_counts()
    fig_status = px.pie(
        values=status_counts.values,
        names=status_counts.index,
        title='Employee Status Distribution'
    )
    st.plotly_chart(fig_status, use_container_width=True)

# Engagement Analysis
st.header("Engagement Analysis")

col1, col2 = st.columns(2)

with col1:
    # Engagement by Department
    engagement_by_dept = merged_data.groupby('department_type')['engagement_score'].mean().sort_values(ascending=False).reset_index()

    fig_engagement = px.bar(
        engagement_by_dept,
        x='department_type',
        y='engagement_score',
        title='Average Engagement Score by Department',
        labels={'engagement_score': 'Engagement Score'},
        color='engagement_score',
        color_continuous_scale='Blues'
    )
    fig_engagement.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig_engagement, use_container_width=True)

with col2:
    # Satisfaction by Department
    satisfaction_by_dept = merged_data.groupby('department_type')['satisfaction_score'].mean().sort_values(ascending=False).reset_index()

    fig_satisfaction = px.bar(
        satisfaction_by_dept,
        x='department_type',
        y='satisfaction_score',
        title='Average Satisfaction Score by Department',
        labels={'satisfaction_score': 'Satisfaction Score'},
        color='satisfaction_score',
        color_continuous_scale='Greens'
    )
    fig_satisfaction.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig_satisfaction, use_container_width=True)

# Work Life Balance
st.subheader("Work Life Balance by Department")
wlb_by_dept = merged_data.groupby('department_type')['work_life_balance_score'].mean().sort_values(ascending=False).reset_index()

fig_wlb = px.bar(
    wlb_by_dept,
    x='department_type',
    y='work_life_balance_score',
    title='Average Work Life Balance Score by Department',
    labels={'work_life_balance_score': 'Work Life Balance Score'},
    color='work_life_balance_score',
    color_continuous_scale='Purples'
)
fig_wlb.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig_wlb, use_container_width=True)

# Training Analysis
st.header("Training Analysis")

col1, col2 = st.columns(2)

with col1:
    # Training Programs Distribution
    training_counts = training['training_program_name'].value_counts().head(10)
    fig_training = px.bar(
        x=training_counts.index,
        y=training_counts.values,
        title='Top 10 Training Programs',
        labels={'x': 'Training Program', 'y': 'Count'}
    )
    fig_training.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig_training, use_container_width=True)

with col2:
    # Training Cost Distribution
    fig_cost = px.histogram(
        training,
        x='training_cost',
        title='Training Cost Distribution',
        nbins=20
    )
    st.plotly_chart(fig_cost, use_container_width=True)

# Correlation Analysis
st.header("Correlation Analysis")

# Attrition vs Engagement
attrition_engagement = merged_data.groupby('department_type').agg({
    'engagement_score': 'mean',
    'employee_status': lambda x: (x.str.lower() == 'terminated').mean() * 100
}).reset_index()

fig_corr = px.scatter(
    attrition_engagement,
    x='engagement_score',
    y='employee_status',
    text='department_type',
    title='Attrition Rate vs Engagement Score by Department',
    labels={'engagement_score': 'Engagement Score', 'employee_status': 'Attrition Rate (%)'}
)
fig_corr.update_traces(textposition='top center')
st.plotly_chart(fig_corr, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("Dashboard created for People Analytics SQL Project")