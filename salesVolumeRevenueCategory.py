import pandas as pd # for dataframe
import matplotlib.pyplot as plt # for visualization

#import data
olist_customer = pd.read_csv("C:\\Users\\olistCustomer.csv")
olist_geoloc = pd.read_csv("C:\\Users\\olistGeolocation.csv")
olist_order_items = pd.read_csv("C:\\Users\\olistOrderItems.csv")
olist_order_payments = pd.read_csv("C:\\Users\\olistOrderPayments.csv")
olist_order_review = pd.read_csv("C:\\Users\\olistOrderReview.csv")
olist_orders = pd.read_csv("C:\\Users\\olistOrders.csv")
olist_product = pd.read_csv("C:\\Users\\olistProducts.csv")
olist_sellers = pd.read_csv("C:\\Users\\olistSeller.csv")

# merge data into product ordered variable
product_ordered = olist_order_items.merge(olist_product, on='product_id', how='inner')
product_ordered

# add revenue collumn by multipling order item id and price
product_ordered['revenue'] = product_ordered['order_item_id'] * product_ordered['price']

# show missing value
product_ordered.isna().sum()

# chek data types
product_ordered.dtypes

# replace missing value with product_category_name mode
product_category_name_mod = product_ordered['product_category_name'].mode()[0]
product_ordered['product_category_name'] = product_ordered['product_category_name'].fillna(product_category_name_mod)

# cek outlier
product_ordered.describe()

# check outlier histogram in revenue collumn
sns.histplot(data=product_ordered, x="revenue", bins=100)

# cek outlier with boxplot revenue
sns.boxplot(data=product_ordered, x='revenue')

# change outlier value with median for revenue
upper_limit_revenue_product = product_ordered['revenue'].quantile(q=0.75) * 1.5
median_revenue_product = product_ordered['revenue'].median() # to find median
product_ordered.loc[product_ordered['revenue'] > upper_limit_revenue_product, 'revenue'] = median_revenue_product #replace new revenue
product_ordered

# to show how many item sold as per product category name by calcuulate order item id
product_cat = product_ordered.groupby('product_category_name')['order_item_id'].sum().reset_index()
product_cat = product_cat.sort_values(by='order_item_id', ascending=False)
product_cat

# visualize top 5 categories
top_5_categories = product_cat.head(5)
plt.figure(figsize=(10, 6))
plt.barh(top_5_categories['product_category_name'], top_5_categories['order_item_id'], color='skyblue')
plt.xlabel('Total Quantity Sold')
plt.ylabel('Product Category')
plt.title('Top 5 Product Categories by Total Quantity Sold')
plt.gca().invert_yaxis()  # Invert the y-axis for better readability
plt.show()

# to show revenue per product category
product_cat_revenue = product_ordered.groupby('product_category_name')['revenue'].sum().reset_index()
product_cat_revenue = product_cat_revenue.sort_values(by='revenue', ascending=False)
product_cat_revenue

# visualize top 5 revenue per product category

top_5_product_category_revenue = product_cat_revenue.head(5)
plt.figure(figsize=(10, 6))
plt.barh(top_5_product_category_revenue['product_category_name'], top_5_product_category_revenue['revenue'], color='skyblue')
plt.xlabel('Total Revenue')
plt.ylabel('Product Category')
plt.title('Top 5 Product Categories by Total Revenue')
plt.gca().invert_yaxis()  # Invert the y-axis for better readability
plt.show()