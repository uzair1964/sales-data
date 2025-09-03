 ## 🧭 Introduction
This Python-based data analysis project uses Pandas and MySQL to explore and forecast retail sales price trends. It investigates how discounts, seasonal patterns, and product categories impact final prices and profitability, helping stakeholders make informed pricing decisions. It also includes interactive visualizations for deeper insight.

## 🛠️ Project Type
Backend (Python for analysis, SQL for data extraction)

## 🚀 Deployed App
Frontend: Not applicable
Backend: Jupyter Notebook / Python Script
Database: MySQL

## 📁 Directory Structure
price-trend-analysis/  
├─ data/  
│  ├─ retail_sales_dataset.csv  
│  ├─ SAL_BW_Project_3.sql  
├─ notebooks/  
│  ├─ SAL_BW_Project_3 (1).ipynb  
├─ visuals/    
├─ README.md  


## 🎥 Video Walkthrough of the Project
Attached a brief video showing key visualizations and insights.

## 🎥 Video Walkthrough of the Codebase
Walkthrough explaining SQL queries, Pandas workflows, and modeling logic.

## ✨ Features
- Aggregation of sales and pricing data using SQL
- Pandas-based data cleaning and transformation
- Forecasting price trends with rolling averages
- Seasonal comparison using month/year filters
- Visualizations (Matplotlib & Seaborn) for actionable insights
- Profit impact analysis from price fluctuations
  
## 🎯 Design Decisions & Assumptions
- Sales data ingested from MySQL tables
- Price prediction based on historical trends and discounts
- Data grouped by category, region, and time
- Assumed clean timestamp format for monthly analysis
- Outliers optionally trimmed for visualization clarity
  
## 🧪 Installation & Getting Started

bash
git clone https://github.com/Shaileshahire06/Price-Trend-Analysis  
cd Price-Trend-Analysis  
pip install -r requirements.txt  
jupyter notebook notebooks/SAL_BW_Project_3 (1).ipynb


To set up MySQL connection:
- Create and populate your database using SAL_BW_Project_3.sql
- Update connection details in the notebook config block
  
## 📌 Usage
Run the notebook to:
- Query and extract data from MySQL
- Perform group-by and pivot analysis in Pandas
- Visualize price trends and profitability metrics
Example SQL Query
SELECT category, AVG(final_price) FROM sales GROUP BY category;
Pandas Snippet
df.groupby(['Month'])['Final_Price'].mean().plot()

## 🔐 Credentials
Database credentials should be securely stored. Use .env or config file for production safety.
  
## 🌐 APIs Used
None – analysis is entirely local using SQL + Pandas

## 📮 API Endpoints
Not applicable – this is a non-service-based analytical project

## 🧰 Technology Stack
- Python: Data analysis with Pandas
- MySQL: Data storage & extraction
- Matplotlib / Seaborn: Visualizations
- Jupyter Notebook: Code, commentary, and charts
- SQL: Joins, filters, aggregations for multi-table analysis
🧰 Technology Stack
Python: Data analysis with Pandas
MySQL: Data storage & extraction
Matplotlib / Seaborn: Visualizations
Jupyter Notebook: Code, commentary, and charts
SQL: Joins, filters, aggregations for multi-table analysis
