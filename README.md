# Customer Complaints Data Analytics Project

An end-to-end data analytics project demonstrating data processing, verification, and visualization using **Excel, SQL, and Python**.

## 📌 Project Overview
The goal of this project is to analyze a customer complaints dataset to track business performance, operational efficiency, and regional complaint distributions. This pipeline helps businesses identify bottleneck regions and understand customer satisfaction levels.

## 🛠️ Tech Stack Used
* **Excel:** Interactive Dashboards, Pivot Tables, Slicers, Conditional Formatting.
* **SQL:** Data aggregation, structural queries (`GROUP BY`, `COUNT`, `AVG`).
* **Python:** Data manipulation (**Pandas**) and Data Visualization (**Matplotlib**).

---

## 📊 Key Performance Indicators (KPIs)
The following core metrics were extracted and validated across all three platforms (Excel, SQL, and Python):
* **Total Complaints:** 10
* **Average Customer Rating:** 2.3 / 5.0
* **Maximum Resolution Time:** 8 Days

---

## 🚀 Implementation Steps

### 1. Excel Dashboard
* Imported the raw dataset and cleaned missing values.
* Created dynamic **Pivot Tables** to summarize complaints by state and resolution status.
* Embedded **KPI Cards** and interactive **Slicers** to allow stakeholders to filter data dynamically.

### 2. SQL Verification
* Wrote structured database queries to verify data integrity.
* Executed aggregation functions to ensure the metrics exactly matched the Excel dashboard outputs.
* Example Query Used:
  ```sql
  SELECT State, COUNT(Complaint_ID) AS Total_Complaints 
  FROM complaints_table 
  GROUP BY State;
