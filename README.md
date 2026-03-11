# AI Data Insight & Data Quality Agent

An AI-powered system that automatically analyzes datasets, detects data quality issues, and generates insights using a Large Language Model (LLM). The system helps users understand their data through automated profiling, validation, and interactive visualizations.

---

## Project Overview

The AI Data Insight & Data Quality Agent allows users to upload datasets and automatically perform:

- Data profiling
- Data validation
- Outlier detection
- AI-powered insights generation
- Interactive visualization dashboard

This project combines data analysis libraries with an LLM to convert raw data into meaningful insights and structured reports.

---

## System Architecture

User Upload CSV Dataset  
↓  
UI Layer (Streamlit) – File Upload & Preview  
↓  
Data Profiling Engine (Pandas) – Missing Values, Duplicates, Statistics  
↓  
Statistical Validation Layer (NumPy) – Outlier Detection using IQR  
↓  
LLM Insight Engine (Groq API + LLaMA 3.1) – Insights & Recommendations  
↓  
Structured Output Layer (JSON) – Reports & KPI Structure  
↓  
Visualization Layer (Streamlit Dashboard) – Display Insights

---

## Tech Stack

- Python  
- Pandas  
- NumPy  
- Streamlit  
- Groq API  
- LLaMA 3.1  
- JSON  

---

## Features

- Automatic data profiling
- Missing value detection
- Duplicate data detection
- Statistical outlier detection
- AI-generated insights
- Interactive data visualization dashboard
- Structured JSON output for reports

---

## Example Workflow

1. Upload a CSV dataset.
2. The system performs data profiling.
3. Outliers are detected using the IQR statistical method.
4. Dataset summary is sent to the LLM.
5. The AI generates insights and recommendations.
6. Results are displayed in the Streamlit dashboard.

---

## Future Improvements

- Support for Excel and SQL databases
- Advanced anomaly detection
- Natural language data queries
- Export reports as PDF
- Integration with business intelligence tools
