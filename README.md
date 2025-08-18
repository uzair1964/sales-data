# Sales Data Analysis

This project demonstrates a complete workflow for exploring retail sales data. It begins with cleaning raw records in Python, continues with structured queries in SQL, and finishes with visualizations in Jupyter notebooks.

## Setup

### Requirements
- Python 3.x with `pip`
- Jupyter Notebook
- MySQL Server or MySQL Workbench
- Python libraries: `pandas`, `seaborn`, `matplotlib`, `mysql-connector-python`

### Install Python dependencies
```bash
pip install pandas seaborn matplotlib mysql-connector-python
```

## Data Source and Key Files
- **Retail_Sale** database: sample retail transactions used throughout the project.
- **Build_week.sql**: creates the `sales` table and contains example queries for common business questions.
- **SAL_BW_Project_3.ipynb**: Jupyter notebook that cleans the raw data and produces visualizations.
- **data/retail_sales_dataset.csv**: small sample dataset for quick experimentation. Replace this file with your own data or download a larger dataset and save it with the same name.

## Dataset

The repository includes a sample CSV at `data/retail_sales_dataset.csv` to illustrate the expected format. For a full analysis,
replace this file with your own retail sales data or download a dataset from a source such as Kaggle and save it to the `data/`
directory using the same filename.

## Running the Analysis
1. Open `SAL_BW_Project_3.ipynb` in Jupyter and execute the cells to clean the dataset and export it to MySQL.
2. In MySQL Workbench (or another SQL client), run the statements in `Build_week.sql` to create the table and explore the data.
3. Return to the notebook to run the visualization cells, which use Seaborn and Matplotlib to plot the results.

