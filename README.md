<!-- Project Logo (place your file at assets/logo.png) -->
<p align="center">
  <img src="assets/logo.png" alt="Sales Data Analysis Logo" width="320">
</p>

<h1 align="center">Sales Data Analysis</h1>

<p align="center">
  End-to-end workflow: clean raw records in Python ➜ explore with SQL ➜ visualize in Jupyter.
</p>

<p align="center">
  <!-- Tech Badges -->
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/pandas-%20-black?logo=pandas&labelColor=white" alt="pandas">
  <img src="https://img.shields.io/badge/NumPy-%20-black?logo=numpy&labelColor=white" alt="NumPy">
  <img src="https://img.shields.io/badge/Matplotlib-%20-black?logo=matplotlib&labelColor=white" alt="Matplotlib">
  <img src="https://img.shields.io/badge/Seaborn-%20-black" alt="Seaborn">
  <img src="https://img.shields.io/badge/MySQL-%20-black?logo=mysql&labelColor=white" alt="MySQL">
  <img src="https://img.shields.io/badge/Jupyter-Notebook-black?logo=jupyter&labelColor=white" alt="Jupyter">
</p>

---

## 🧭 Overview
This project demonstrates a complete workflow for exploring **retail sales data**.  
It starts by **cleaning** raw records in Python, continues with **structured queries** in SQL (MySQL), and finishes with **visualizations** in Jupyter notebooks (Seaborn/Matplotlib).

---

## 💡 Why this project?
- **Real-world pipeline:** Shows how messy CSVs become analysis-ready tables, then insights—exactly what most retail teams need.  
- **Separation of concerns:** Python for cleaning, SQL for business questions, notebooks for quick visuals—clear and reusable.  
- **Hiring-friendly:** Demonstrates skills used in analyst/data science roles (EDA, SQL queries, KPI reporting, basic ML-ready outputs).

### 📌 When this analysis helps (use cases)
- **Merchandising & assortment:** Identify top sellers/long-tail, category contribution, Pareto (80/20) for shelf/website placement.  
- **Inventory & demand planning:** Spot seasonality and MoM/YoY trends to adjust stock, lead times, and safety stock.  
- **Pricing & promotions:** Measure pre/post promo lift, discount effectiveness, and cannibalization across categories/channels.  
- **Store/channel performance:** Compare stores or online channels, monitor AOV, units/order, margin %, return rate.  
- **Operational monitoring:** Catch anomalies/outlier days and surface data quality issues early.

---

## 🧰 Tech Stack
- **Python:** pandas, seaborn, matplotlib, mysql-connector-python  
- **SQL:** MySQL Server / MySQL Workbench  
- **Environment:** Jupyter Notebook (Python 3.x)

---

## ⚙️ Setup

### Requirements
- Python 3.x with `pip`  
- Jupyter Notebook  
- MySQL Server or MySQL Workbench  
- Python libraries: `pandas`, `seaborn`, `matplotlib`, `mysql-connector-python`

### Install dependencies
```bash
pip install pandas seaborn matplotlib mysql-connector-python

## Running the Analysis
1. Open [SAL_BW_Project_3.ipynb](SAL_BW_Project_3.ipynb) in Jupyter and execute the cells to clean the dataset and export it to MySQL.
2. In MySQL Workbench (or another SQL client), run the statements in `Build_week.sql` to create the table and explore the data.
3. Return to the notebook to run the visualization cells, which use Seaborn and Matplotlib to plot the results.

