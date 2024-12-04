# question 1 & 2
import streamlit as st
import pandas as pd
import plotly.express as px




st.header("COVID 19 DATASET OVERVIEW AND SUMMARY😷")


st.subheader("This is the  top 5 view of dataset.csv dataset (before mapping) ❓:")
df = pd.read_csv('dataset.csv')
st.dataframe(df.head())


#Q1
st.subheader("This is the  top 5 view of analysis.csv dataset (after mapping) ✅:")
#Mapping the all data required from data_analysis.xlxs into dataset.csv
df["SEX"] = df["SEX"].map({1: "FEMALE", 2: "MALE", 99: "UNKNOWN"})
df["HOSPITALIZED"] = df["HOSPITALIZED"].map({1: "NO", 2: "YES", 99: "UNKNOWN"})
df["INTUBATED"] = df["INTUBATED"].map({1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"})
df["PNEUMONIA"] = df["PNEUMONIA"].map({1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"})
df["PREGNANCY"] = df["PREGNANCY"].map({1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"})
df["SPEAKS_NATIVE_LANGUAGE"] = df["SPEAKS_NATIVE_LANGUAGE"].map({1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"})
df["DIABETES"] = df["DIABETES"].map({1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"})
df["COPD"] = df["COPD"].map({1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"})
df["ASTHMA"] = df["ASTHMA"].map({1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"})
df["INMUSUPR"] = df["INMUSUPR"].map({1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"})
df["HYPERTENSION"] = df["HYPERTENSION"].map({1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"})
df["OTHER_DISEASE"] = df["OTHER_DISEASE"].map({1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"})
df["CARDIOVASCULAR"] = df["CARDIOVASCULAR"].map({1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"})
df["OBESITY"] = df["OBESITY"].map({1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"})
df["CHRONIC_KIDNEY"] = df["CHRONIC_KIDNEY"].map({1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"})
df["TOBACCO"] = df["TOBACCO"].map({1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"})
df["ANOTHER CASE"] = df["ANOTHER CASE"].map({1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"})
df["MIGRANT"] = df["MIGRANT"].map({1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"})
df["ICU"] = df["ICU"].map({1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"})
df["OUTCOME"] = df["OUTCOME"].map({1: "POSITIVE", 2: "NEGATIVE", 3: "PENDING"})
df["NATIONALITY"] = df["NATIONALITY"].map({1: "MEXICAN", 2: "FOREIGN", 99: "UNKNOWN"})


new_df = df.copy()
new_df.to_csv("analysis.csv", index=True)
analysis = pd.read_csv("analysis.csv")
st.dataframe(analysis.head())




st.subheader("Unique Values in Each Column 💯")


# Get unique values for each column
unique_values_per_column = analysis.apply(lambda col: col.unique())


# Create a DataFrame to display unique values, converting arrays to strings
unique_values_df = pd.DataFrame({
    'Column': unique_values_per_column.index,
    'Unique Values': unique_values_per_column.apply(lambda x: ', '.join(map(str, x)))
})


# Display the table of unique values
st.dataframe(unique_values_df)


#Q2


st.subheader("The Age Group which susceptible to Covid-19 🎯")


# Define the age bins
age_bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


# Create a new column 'Age Group' based on the bins
analysis['AGE GROUP'] = pd.cut(analysis['AGE'], bins=age_bins)


# Ensure the AGE GROUP column is properly displayed (as string if needed)
analysis['AGE GROUP'] = analysis['AGE GROUP'].astype(str)


# To see the counts of different outcomes for each age group
age_group_outcome = analysis.groupby('AGE GROUP')['OUTCOME'].value_counts().unstack().fillna(0)


st.write(age_group_outcome)


st.write("The most affected for age group towards covid-19 : 40-49 🥇")
st.write("The 2nd most affected for age group towards covid-19 : 30-39 🥈")
st.write("The 3rd most affected for age group towards covid-19 : 50-59 🥉")

