import pandas as pd

df = pd.read_csv('retail_sales_dataset.csv')

print(df.isnull().sum())
print(df.dropna(inplace = True))

print(df.duplicated().sum())
print(df.drop_duplicates(inplace = True))

df['TotalPrice'] = df['Quantity'] * df['Price per Unit']
df.head()

df.to_csv('retail_sales_dataset_cln.csv', index=False)
print("Cleaned data exported to cleaned_retail_sales_dataset.csv")

# !pip install PyMySQL
# !pip install ipython-sql
# !pip install mysqlclient
# !pip install mysql
# !pip install mysql.connector

import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="Shailesh@06",
    database="Retail_Sale"
)

cursor = mydb.cursor()

df = pd.read_csv('retail_sales_dataset_cln.csv')
for _, row in df.iterrows():
    cursor.execute("""INSERT INTO sales(Transaction_ID, Date_, Customer_ID, Gender, Age, Product_Category, Quantity, Price_per_Unit, Total_Amount, TotalPrice)
    Values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (row["Transaction ID"], row["Date"], row["Customer ID"], row["Gender"], row["Age"], row["Product Category"], row["Quantity"], row["Price per Unit"], row["Total Amount"], row["TotalPrice"]))

mydb.commit()
print("Data Inserted Successfully")

querry = "SELECT * FROM Sales"
cursor.execute(querry)
rows = cursor.fetchall()
for row in rows:
    print(row)

import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month

plt.figure(figsize=(10, 6))
plt.plot(df['Month'], df['TotalPrice'], label='Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('TotalPrice')
plt.title('Monthly Sales Trend')
plt.legend()
plt.show()

category_revenue = df.groupby('Product Category')['TotalPrice'].sum().sort_values(ascending=False)

top_categories = category_revenue.head()

plt.figure(figsize=(12, 6))
top_categories.plot(kind='bar', color='lightcoral')
plt.xlabel('Product Category')
plt.ylabel('Revenue')
plt.title('Top Product Categories by Revenue')
plt.xticks(rotation=45)
plt.show()

customer_revenue = df.groupby('Customer ID')['TotalPrice'].sum().sort_values(ascending=False)

top_5_customers = customer_revenue.head(5)

others_revenue = customer_revenue[5:].sum()
top_5_customers['Others'] = others_revenue

plt.figure(figsize=(8, 8))
top_5_customers.plot(kind='pie', autopct='%1.1f%%', startangle=140, colormap='coolwarm')
plt.ylabel('') 
plt.title('Contribution of Top 5 Customers to Total Revenue')
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

heatmap_data = df.pivot_table(index='Month', columns='Product Category', values='TotalPrice', aggfunc='sum')

plt.figure(figsize=(12, 8))
sns.heatmap(heatmap_data, cmap='YlGnBu', annot=True, fmt='.1f', linewidths=0.5)
plt.title('Sales by Month and Product Category')
plt.xlabel('Product Category')
plt.ylabel('Month')
plt.show()

