import pandas as pd
import sqlite3

sales_df = pd.read_csv('task/sales_data.csv')

category_stats = sales_df.groupby('Category').agg(
    total_quantity_sold=('Quantity', 'sum'),
    avg_price_per_unit=('Price', 'mean'),
    max_quantity_single_txn=('Quantity', 'max')
).reset_index()

top_products = (
    sales_df.groupby(['Category', 'Product'])['Quantity'].sum()
    .reset_index()
    .sort_values(['Category', 'Quantity'], ascending=[True, False])
    .drop_duplicates('Category')
)

category_stats = pd.merge(category_stats, top_products[['Category', 'Product']], on='Category')
category_stats.rename(columns={'Product': 'top_selling_product'}, inplace=True)

sales_df['TotalSale'] = sales_df['Quantity'] * sales_df['Price']
highest_sales_date = (
    sales_df.groupby('Date')['TotalSale'].sum()
    .idxmax()
)

print("=== Sales Category Stats ===")
print(category_stats)
print("\nDate with highest total sales:", highest_sales_date)

orders_df = pd.read_csv('task/customer_orders.csv')

customer_order_counts = orders_df.groupby('CustomerID')['OrderID'].nunique()
qualified_customers = customer_order_counts[customer_order_counts >= 20].index
filtered_orders = orders_df[orders_df['CustomerID'].isin(qualified_customers)]

avg_price_per_customer = orders_df.groupby('CustomerID')['Price'].mean()
high_value_customers = avg_price_per_customer[avg_price_per_customer > 120].index

product_summary = orders_df.groupby('Product').agg(
    total_quantity=('Quantity', 'sum'),
    total_price=('Price', lambda x: (x * orders_df.loc[x.index, 'Quantity']).sum())
).reset_index()

filtered_product_summary = product_summary[product_summary['total_quantity'] >= 5]

print("\n=== Customers with >= 20 Orders ===")
print(filtered_orders['CustomerID'].unique())

print("\n=== Customers with Avg Price > $120 ===")
print(high_value_customers.tolist())

print("\n=== Filtered Product Summary (Quantity >= 5) ===")
print(filtered_product_summary)

salary_bands = pd.read_excel('task/population salary analysis.xlsx')

conn = sqlite3.connect('task/population.db')
population_df = pd.read_sql_query("SELECT * FROM population", conn)
conn.close()

def classify_salary(salary):
    row = salary_bands[(salary_bands['MinSalary'] <= salary) & (salary <= salary_bands['MaxSalary'])]
    return row['Band'].values[0] if not row.empty else 'Unknown'

population_df['SalaryBand'] = population_df['Salary'].apply(classify_salary)

band_stats = population_df.groupby('SalaryBand').agg(
    population_count=('Salary', 'count'),
    average_salary=('Salary', 'mean'),
    median_salary=('Salary', 'median')
)
band_stats['percentage_population'] = (band_stats['population_count'] / band_stats['population_count'].sum()) * 100

print("\n=== Salary Band Stats ===")
print(band_stats)

state_band_stats = population_df.groupby(['State', 'SalaryBand']).agg(
    population_count=('Salary', 'count'),
    average_salary=('Salary', 'mean'),
    median_salary=('Salary', 'median')
).reset_index()

total_per_state = population_df.groupby('State')['Salary'].count().to_dict()
state_band_stats['percentage_population'] = state_band_stats.apply(
    lambda row: (row['population_count'] / total_per_state[row['State']]) * 100, axis=1
)

print("\n=== Salary Band Stats per State ===")
print(state_band_stats)
