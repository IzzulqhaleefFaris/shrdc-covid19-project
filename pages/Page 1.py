import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('analysis.csv')

# Define the age bins
age_bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Create a new column 'Age Group' based on the bins
df['AGE GROUP'] = pd.cut(df['AGE'], bins=age_bins)

# Sidebar for interactivity
st.sidebar.header("Filters")

# Slider for age range
age_min, age_max = st.sidebar.slider(
    "Select Age Range",
    min_value=int(df['AGE'].min()),
    max_value=int(df['AGE'].max()),
    value=(0, 100)
)

# Multi-select for outcomes
selected_outcomes = st.sidebar.multiselect(
    "Select Outcomes",
    options=df['OUTCOME'].unique(),
    default=df['OUTCOME'].unique()
)

# Filter dataset based on slider and multi-select
filtered_data = df[
    (df['AGE'] >= age_min) & (df['AGE'] <= age_max) & 
    (df['OUTCOME'].isin(selected_outcomes))
]

st.header("Question 3 & Question 4")

tab1, tab2 = st.tabs(["Bar Chart", "Histogram"])

with tab1:
    st.subheader("Comparison of Positive Cases and Hospitalized Cases by Age Group")

    # Count positive cases and hospitalized cases
    age_group_data = filtered_data.groupby('AGE GROUP').agg(
        Positive_Cases=('OUTCOME', lambda x: (x == "POSITIVE").sum()),
        Hospitalized_Cases=('HOSPITALIZED', lambda x: (x == "YES").sum())
    )

    # Convert index to readable age group labels
    age_group_data.index = age_group_data.index.map(lambda x: f"{int(x.left)}-{int(x.right)}")

    # Reset index for plotting
    age_group_data.reset_index(inplace=True)

    # Rename columns
    age_group_data.rename(columns={'Positive_Cases': 'Positive Cases', 'Hospitalized_Cases': 'Hospitalized Cases'}, inplace=True)

    # Plot Bar Chart
    grouped_barchart = px.bar(
        age_group_data,
        x='AGE GROUP',
        y=['Positive Cases', 'Hospitalized Cases'],
        labels={'value': 'Total Cases', 'AGE GROUP': 'Age Group', 'variable': 'Category'},
        title=f"Comparison of Positive and Hospitalized Cases by Age Group (Age {age_min}-{age_max})",
        barmode='group'
    )

    grouped_barchart.update_layout(
        bargap=0.1,
        bargroupgap=0.05,
        width=800,
        height=500
    )

    # Show chart
    st.plotly_chart(grouped_barchart)

with tab2:
    st.subheader("Distribution of Positive Cases by Age Group")
    
    # Count positive cases
    age_group_data = filtered_data.groupby('AGE GROUP').agg(
        Positive_Cases=('OUTCOME', lambda x: (x == "POSITIVE").sum())
    )

    # Convert index to readable age group labels
    age_group_data.index = age_group_data.index.map(lambda x: f"{int(x.left)}-{int(x.right)}")

    # Reset index for plotting
    age_group_data.reset_index(inplace=True)

    # Rename columns
    age_group_data.rename(columns={'Positive_Cases': 'Positive Cases'}, inplace=True)

    # Plot Histogram for Positive Cases
    histogram = px.histogram(
        age_group_data,
        x='AGE GROUP',
        y='Positive Cases',
        labels={'Positive Cases': 'Total Positive Cases', 'AGE GROUP': 'Age Group'},
        title=f"Distribution of Positive Cases by Age Group (Age {age_min}-{age_max})",
        histfunc='sum',
        nbins=len(age_group_data)
    )

    histogram.update_layout(
        bargap=0.1,
        bargroupgap=0.05,
        width=800,
        height=500
    )

    # Show chart
    st.plotly_chart(histogram)
