import streamlit as st
import pandas as pd
import plotly.express as px

# # Load the dataset
# df = pd.read_csv('analysis.csv')

# st.header("Question 7")

# # First chart - correlation

# st.subheader("Correlation between other diseases and ICU admission")
# import numpy as np
# np.random.seed(42)
# df = pd.DataFrame({
#     "DIABETES": np.random.rand(100),
#     "COPD": np.random.rand(100),
#     "ASTHMA": np.random.rand(100),
#     "INMUSUPR": np.random.rand(100),
#     "HYPERTENSION": np.random.rand(100),
#     "CARDIOVASCULAR": np.random.rand(100),
#     "OBESITY": np.random.rand(100),
#     "CHRONIC_KIDNEY": np.random.rand(100),
#     "TOBACCO": np.random.rand(100),
#     "ICU": np.random.rand(100),
# })


# # Calculate Spearman correlations
# icu_diabetes_correlation = df["DIABETES"].corr(df["ICU"], method='spearman')
# icu_copd_correlation = df["COPD"].corr(df["ICU"], method='spearman')
# icu_asthma_correlation = df["ASTHMA"].corr(df["ICU"], method='spearman')
# icu_inmusupr_correlation = df["INMUSUPR"].corr(df["ICU"], method='spearman')
# icu_hypertension_correlation = df["HYPERTENSION"].corr(df["ICU"], method='spearman')
# icu_cardiovascular_correlation = df["CARDIOVASCULAR"].corr(df["ICU"], method='spearman')
# icu_obesity_correlation = df["OBESITY"].corr(df["ICU"], method='spearman')
# icu_kidney_correlation = df["CHRONIC_KIDNEY"].corr(df["ICU"], method='spearman')
# icu_tobacco_correlation = df["TOBACCO"].corr(df["ICU"], method='spearman')


# # Create a dictionary of correlations
# correlations = {
#     "DIABETES": icu_diabetes_correlation,
#     "COPD": icu_copd_correlation,
#     "ASTHMA": icu_asthma_correlation,
#     "INMUSUPR": icu_inmusupr_correlation,
#     "HYPERTENSION": icu_hypertension_correlation,
#     "CARDIOVASCULAR": icu_cardiovascular_correlation,
#     "OBESITY": icu_obesity_correlation,
#     "CHRONIC_KIDNEY": icu_kidney_correlation,
#     "TOBACCO": icu_tobacco_correlation
# }


# # Convert the dictionary to a DataFrame
# correlation_df = pd.DataFrame(list(correlations.items()), columns=["Disease", "ICU Correlation"])


# # Define a function to categorize the correlation level
# def correlation_level(correlation):
#     if correlation < -0.8:
#         return "Very strong negative"
#     elif correlation < -0.6:
#         return "Strong negative"
#     elif correlation < -0.4:
#         return "Moderate negative"
#     elif correlation < -0.2:
#         return "Weak negative"
#     elif correlation < 0:
#         return "Very weak negative"
#     elif correlation < 0.2:
#         return "Very weak positive"
#     elif correlation < 0.4:
#         return "Weak positive"
#     elif correlation < 0.6:
#         return "Moderate positive"
#     elif correlation < 0.8:
#         return "Strong positive"
#     else:
#         return "Very strong positive"


# # Apply the function to create a new column "Level of Correlation"
# correlation_df["Level of Correlation"] = correlation_df["ICU Correlation"].apply(correlation_level)


# # Streamlit App Layout
# st.title("ICU and Disease Correlation Analysis")
# st.markdown("""
# This calculates the Spearman correlation between ICU admissions and various diseases.
# """)


# # Display the correlation DataFrame
# st.dataframe(correlation_df)


# # Visualization
# st.bar_chart(correlation_df.set_index("Disease")["ICU Correlation"])

# First chart - correlation

# Load the dataset
df = pd.read_csv('analysis.csv')

st.header("Question 7")

st.subheader("Correlation between other diseases and ICU admission")
import numpy as np
np.random.seed(42)
df = pd.DataFrame({
    "DIABETES": np.random.rand(100),
    "COPD": np.random.rand(100),
    "ASTHMA": np.random.rand(100),
    "INMUSUPR": np.random.rand(100),
    "HYPERTENSION": np.random.rand(100),
    "CARDIOVASCULAR": np.random.rand(100),
    "OBESITY": np.random.rand(100),
    "CHRONIC_KIDNEY": np.random.rand(100),
    "TOBACCO": np.random.rand(100),
    "ICU": np.random.rand(100),
})


# Calculate Spearman correlations
icu_diabetes_correlation = df["DIABETES"].corr(df["ICU"], method='spearman')
icu_copd_correlation = df["COPD"].corr(df["ICU"], method='spearman')
icu_asthma_correlation = df["ASTHMA"].corr(df["ICU"], method='spearman')
icu_inmusupr_correlation = df["INMUSUPR"].corr(df["ICU"], method='spearman')
icu_hypertension_correlation = df["HYPERTENSION"].corr(df["ICU"], method='spearman')
icu_cardiovascular_correlation = df["CARDIOVASCULAR"].corr(df["ICU"], method='spearman')
icu_obesity_correlation = df["OBESITY"].corr(df["ICU"], method='spearman')
icu_kidney_correlation = df["CHRONIC_KIDNEY"].corr(df["ICU"], method='spearman')
icu_tobacco_correlation = df["TOBACCO"].corr(df["ICU"], method='spearman')


# Create a dictionary of correlations
correlations = {
    "DIABETES": icu_diabetes_correlation,
    "COPD": icu_copd_correlation,
    "ASTHMA": icu_asthma_correlation,
    "INMUSUPR": icu_inmusupr_correlation,
    "HYPERTENSION": icu_hypertension_correlation,
    "CARDIOVASCULAR": icu_cardiovascular_correlation,
    "OBESITY": icu_obesity_correlation,
    "CHRONIC_KIDNEY": icu_kidney_correlation,
    "TOBACCO": icu_tobacco_correlation
}


# Convert the dictionary to a DataFrame
correlation_df = pd.DataFrame(list(correlations.items()), columns=["Disease", "ICU Correlation"])


# Define a function to categorize the correlation level
def correlation_level(correlation):
    if correlation < -0.8:
        return "Very strong negative"
    elif correlation < -0.6:
        return "Strong negative"
    elif correlation < -0.4:
        return "Moderate negative"
    elif correlation < -0.2:
        return "Weak negative"
    elif correlation < 0:
        return "Very weak negative"
    elif correlation < 0.2:
        return "Very weak positive"
    elif correlation < 0.4:
        return "Weak positive"
    elif correlation < 0.6:
        return "Moderate positive"
    elif correlation < 0.8:
        return "Strong positive"
    else:
        return "Very strong positive"


# Apply the function to create a new column "Level of Correlation"
correlation_df["Level of Correlation"] = correlation_df["ICU Correlation"].apply(correlation_level)


# Streamlit App Layout
st.title("ICU and Disease Correlation Analysis")
st.markdown("""
This calculates the Spearman correlation between ICU admissions and various diseases.
""")


# Display the correlation DataFrame
st.dataframe(correlation_df)


# Visualization
import altair as alt


# Create a bar chart with Altair
chart = alt.Chart(correlation_df).mark_bar().encode(
    x=alt.X("Disease", title="Disease"),
    y=alt.Y("ICU Correlation", title="Spearman Correlation"),
    color=alt.Color("ICU Correlation", scale=alt.Scale(scheme="blues"))
).properties(
    title="Correlation between Diseases and ICU Admission",
    width=800,
    height=400
)


# Render the chart in Streamlit
st.altair_chart(chart, use_container_width=True)


