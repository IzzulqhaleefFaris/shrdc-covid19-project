import streamlit as st
import pandas as pd
import plotly.express as px 

# Load the dataset
df = pd.read_csv('analysis.csv')

# Streamlit header and subheader
st.header("Question 8")
st.subheader("Bar Chart: Most Common Diseases Among Deceased Patients")

# Filter the data for deceased patients
deceased_patients = df[df['DATE_OF_DEATH'].notnull()]

# Select disease columns
disease_columns = [
    "DIABETES", "COPD", "ASTHMA", "INMUSUPR", "HYPERTENSION",
    "OTHER_DISEASE", "CARDIOVASCULAR", "OBESITY", "CHRONIC_KIDNEY", "TOBACCO"
]



# Multi-select for diseases
selected_diseases = st.sidebar.multiselect(
    "Select Diseases to Display:",
    options=disease_columns,
    default=disease_columns
)

# Gender filter
selected_gender = st.sidebar.selectbox(
    "Filter by Gender:",
    options=["All", "Male", "Female"],
    index=0
)

# Apply gender filter if not "All"
if selected_gender != "All":
    deceased_patients = deceased_patients[deceased_patients["SEX"] == selected_gender.upper()]

# Calculate counts for selected diseases
disease_counts = deceased_patients[selected_diseases].apply(lambda col: (col == "YES").sum())

# Create a bar chart using Plotly
fig = px.bar(
    x=disease_counts.index,
    y=disease_counts.values,
    color=disease_counts.index,
    labels={"x": "Disease", "y": "Number of Deceased Patients"},
    title="Common Diseases Among Deceased Patients"
)

# Add values on the bars
fig.update_traces(text=disease_counts.values, textposition="outside")

# Adjust layout for better visualization
fig.update_layout(
    bargap=0.1,  # Reduce the gap between bars for better zooming effect
    bargroupgap=0.05,  # Adjust group gap for visual improvement
    width=800,  # Increase width for a larger chart
    height=500,  # Increase height for a more zoomed-in view
    xaxis=dict(tickmode='linear'),  # Ensure x-axis is displayed linearly
    title={'x': 0.5},  # Center the title
)

# Display the chart in Streamlit
st.plotly_chart(fig)
