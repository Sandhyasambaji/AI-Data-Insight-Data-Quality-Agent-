import streamlit as st
import pandas as pd
import numpy as np
import json
from groq import Groq

client = Groq(api_key="Your groq api key")

st.title("AI Data Insight & Data Quality Agent")

uploaded_file = st.file_uploader("Upload CSV Dataset", type=["csv"])

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    # -----------------------------
    # DATA PROFILING
    # -----------------------------

    missing = df.isnull().sum().to_dict()
    duplicates = int(df.duplicated().sum())

    numeric_cols = df.select_dtypes(include=np.number).columns
    outliers = {}

    for col in numeric_cols:

        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)

        IQR = Q3 - Q1

        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR

        count = df[(df[col] < lower) | (df[col] > upper)].shape[0]

        outliers[col] = int(count)

    # -----------------------------
    # AI ANALYSIS
    # -----------------------------

    dataset_info = f"""
Columns: {list(df.columns)}

Missing Values:
{missing}

Duplicate Rows: {duplicates}

Outliers:
{outliers}

Summary Statistics:
{df.describe().to_string()}
"""

    prompt = f"""
You are a data analyst.

Analyze the dataset and return STRICT JSON.

Format:

{{
"data_quality_report": "",
"top_business_insights": [],
"cleaning_recommendations": [],
"suggested_dashboard_kpis": []
}}

Dataset Information:
{dataset_info}
"""

    with st.spinner("Analyzing dataset..."):

        try:

            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[{"role": "user", "content": prompt}]
            )

            ai_output = response.choices[0].message.content

            ai_output = ai_output.replace("```json", "").replace("```", "").strip()

            data = json.loads(ai_output)

            # -----------------------------
            # UI OUTPUT
            # -----------------------------

            st.subheader("Data Quality Report")
            st.write(data["data_quality_report"])

            st.subheader("Top Business Insights")

            for insight in data["top_business_insights"]:
                st.write("•", insight)

            st.subheader("Cleaning Recommendations")

            for rec in data["cleaning_recommendations"]:
                st.write("•", rec)

            st.subheader("Suggested Dashboard KPIs")

            for kpi in data["suggested_dashboard_kpis"]:
                st.write("•", kpi)

        except Exception as e:

            st.error(f"AI analysis failed: {e}")