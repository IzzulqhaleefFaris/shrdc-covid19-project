import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('analysis.csv')

# Define the age bins
age_bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Create a new column 'Age Group' based on the bins
df['AGE GROUP'] = pd.cut(df['AGE'], bins=age_bins)

# Sidebar for interactive filters
st.sidebar.header("Filters")

# Filter by gender
selected_gender = st.sidebar.multiselect(
    "Select Gender",
    options=df['SEX'].unique(),
    default=df['SEX'].unique()
)

# Filter by outcome
selected_outcomes = st.sidebar.multiselect(
    "Select Outcomes",
    options=df['OUTCOME'].unique(),
    default=df['OUTCOME'].unique()
)

# Filter by intubation status
selected_intubation_status = st.sidebar.multiselect(
    "Select Intubation Status",
    options=['NO', 'YES', 'UNKNOWN'],
    default=['NO', 'YES', 'UNKNOWN']
)

# Filter the data based on selected parameters
filtered_data = df[
    (df['SEX'].isin(selected_gender)) &
    (df['OUTCOME'].isin(selected_outcomes))
]

st.header("Question 5 & Question 6")

tab1, tab2 = st.tabs(["Histogram", "Bar Chart"])

with tab1:
    st.subheader("Comparison of Positive Cases by Age Group and Sex")

    # Count positive cases, grouped by SEX
    age_group_data = filtered_data.groupby(['AGE GROUP', 'SEX']).agg(
        Positive_Cases=('OUTCOME', lambda x: (x == "POSITIVE").sum())
    ).reset_index()

    # Convert AGE GROUP to string format to avoid issues with Interval data type
    age_group_data['AGE GROUP'] = age_group_data['AGE GROUP'].apply(lambda x: f"{int(x.left)}-{int(x.right)}")

    # Rename columns for readability
    age_group_data.rename(columns={'Positive_Cases': 'Positive Cases'}, inplace=True)

    # Plot Histogram
    histogram = px.bar(
        age_group_data,
        x='AGE GROUP',
        y='Positive Cases',
        color='SEX',
        labels={'Positive Cases': 'Total Positive Cases', 'AGE GROUP': 'Age Group', 'SEX': 'Sex'},
        title=f"Positive Cases by Age Group and Sex (Gender: {', '.join(selected_gender)})",
        barmode='stack'
    )

    histogram.update_layout(
        bargap=0.1,
        bargroupgap=0.05,
        width=800,
        height=500
    )

    # Show chart
    st.plotly_chart(histogram)

with tab2:
    st.subheader("Bar Chart: Total Cases of Intubation Among Patients")

    # Filter data for intubation status
    intubation_filtered = df[df['INTUBATED'].isin(selected_intubation_status)]

    # Count the frequency of each unique value in the 'INTUBATED' column
    intubation_counts = intubation_filtered['INTUBATED'].value_counts().reset_index()

    # Rename the columns for better readability
    intubation_counts.columns = ['Intubation Status', 'Frequency']

    # Create the bar chart
    bar_chart = px.bar(
        intubation_counts,
        x='Intubation Status',
        y='Frequency',
        color='Intubation Status',
        labels={'Intubation Status': 'Intubation Status', 'Frequency': 'Count'},
        title=f"Number of Patients Required Intubation (Statuses: {', '.join(selected_intubation_status)})"
    )

    bar_chart.update_layout(
        bargap=0.1,
        bargroupgap=0.05,
        width=800,
        height=500,
        xaxis=dict(tickmode='linear'),
        title={'x': 0.5},
    )

    # Show chart
    st.plotly_chart(bar_chart, use_container_width=True)
